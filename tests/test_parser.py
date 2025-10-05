import pytest
from protobuf_test_generator.core.parser import ProtoParser


@pytest.fixture
def parser():
    return ProtoParser()


def test_parse_valid_proto(parser):
    proto_file = "tests/fixtures/test_basic.proto"
    messages = parser.parse(proto_file)
    assert "User" in messages
    assert "age" in messages["User"].fields
    assert "email" in messages["User"].fields
    assert "tags" in messages["User"].fields


def test_parse_invalid_proto(parser):
    proto_file = "tests/fixtures/invalid.proto"
    with pytest.raises(Exception):
        parser.parse(proto_file)


def test_parse_protovalidate_proto(parser):
    proto_file = "tests/fixtures/test_protovalidate.proto"
    messages = parser.parse(proto_file)
    assert "ApiRequest" in messages
    assert "user_id" in messages["ApiRequest"].fields
    assert "email" in messages["ApiRequest"].fields


def test_parse_nanopb_proto(parser):
    proto_file = "tests/fixtures/test_nanopb.proto"
    messages = parser.parse(proto_file)
    assert "BasicValidation" in messages
    assert "age" in messages["BasicValidation"].fields
    assert "username" in messages["BasicValidation"].fields


def test_parse_empty_proto(parser):
    proto_file = "tests/fixtures/empty.proto"
    messages = parser.parse(proto_file)
    assert messages == {}
