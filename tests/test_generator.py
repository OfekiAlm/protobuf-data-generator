import pytest
from protobuf_test_generator.core.generator import DataGenerator
from protobuf_test_generator.utils.proto_utils import load_proto_file


@pytest.fixture
def basic_validation_proto():
    return load_proto_file("tests/fixtures/test_basic.proto")


@pytest.fixture
def protovalidate_proto():
    return load_proto_file("tests/fixtures/test_protovalidate.proto")


def test_generate_valid_data(basic_validation_proto):
    gen = DataGenerator(basic_validation_proto)
    valid_data = gen.generate_valid("BasicValidation", seed=42)

    assert valid_data is not None
    assert "age" in valid_data
    assert valid_data["age"] >= 18 and valid_data["age"] <= 120


def test_generate_invalid_data(basic_validation_proto):
    gen = DataGenerator(basic_validation_proto)
    invalid_data = gen.generate_invalid(
        "BasicValidation", violate_field="age", violate_rule="lte"
    )

    assert invalid_data is not None
    assert invalid_data["age"] > 120


def test_generate_protovalidate_data(protovalidate_proto):
    gen = DataGenerator(protovalidate_proto)
    valid_data = gen.generate_valid("User", seed=42)

    assert valid_data is not None
    assert "email" in valid_data
    assert "@" in valid_data["email"]


def test_invalid_protovalidate_data(protovalidate_proto):
    gen = DataGenerator(protovalidate_proto)
    invalid_data = gen.generate_invalid(
        "User", violate_field="email", violate_rule="min_len"
    )

    assert invalid_data is not None
    assert len(invalid_data["email"]) < 5


def test_generate_repeated_field_data(basic_validation_proto):
    gen = DataGenerator(basic_validation_proto)
    valid_data = gen.generate_valid("BasicValidation", seed=42)

    assert "tags" in valid_data
    assert isinstance(valid_data["tags"], list)
    assert len(valid_data["tags"]) >= 1 and len(valid_data["tags"]) <= 10


def test_generate_enum_data(basic_validation_proto):
    gen = DataGenerator(basic_validation_proto)
    valid_data = gen.generate_valid("BasicValidation", seed=42)

    assert "status" in valid_data
    assert valid_data["status"] in [
        "ACTIVE",
        "INACTIVE",
        "PENDING",
    ]  # Assuming these are valid enum values
