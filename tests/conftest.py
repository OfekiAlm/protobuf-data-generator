from pytest import fixture


@fixture(scope="session")
def proto_file_paths():
    return {
        "basic": "tests/fixtures/test_basic.proto",
        "nanopb": "tests/fixtures/test_nanopb.proto",
        "protovalidate": "tests/fixtures/test_protovalidate.proto",
    }


@fixture
def valid_data_generator(proto_file_paths):
    from protobuf_test_generator.core.generator import DataGenerator

    return DataGenerator(proto_file_paths["basic"])


@fixture
def invalid_data_generator(proto_file_paths):
    from protobuf_test_generator.core.generator import DataGenerator

    return DataGenerator(proto_file_paths["basic"], invalid=True)
