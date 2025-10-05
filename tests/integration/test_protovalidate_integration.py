import pytest
from protobuf_test_generator import DataGenerator, validate_protovalidate


@pytest.fixture
def protovalidate_generator():
    return DataGenerator(
        "tests/fixtures/test_protovalidate.proto", include_paths=["tests/fixtures"]
    )


def test_valid_data_generation(protovalidate_generator):
    valid_data = protovalidate_generator.generate_valid("User", seed=42)
    assert valid_data["age"] >= 18
    assert valid_data["age"] <= 120
    assert "@" in valid_data["email"]
    assert len(valid_data["email"]) >= 5


def test_invalid_data_generation(protovalidate_generator):
    invalid_data = protovalidate_generator.generate_invalid(
        "User", violate_field="age", violate_rule="lte"
    )
    assert invalid_data["age"] > 120

    invalid_data = protovalidate_generator.generate_invalid(
        "User", violate_field="email", violate_rule="min_len"
    )
    assert len(invalid_data["email"]) < 5


def test_integration_with_protovalidate(protovalidate_generator):
    valid_data = protovalidate_generator.generate_valid("User", seed=42)
    binary_data = protovalidate_generator.encode_to_binary("User", valid_data)

    # Assuming a validate function exists in the protovalidate library
    assert validate_protovalidate(binary_data)

    invalid_data = protovalidate_generator.generate_invalid(
        "User", violate_field="tags", violate_rule="min_items"
    )
    binary_invalid_data = protovalidate_generator.encode_to_binary("User", invalid_data)

    # Validate that the invalid data fails validation
    assert not validate_protovalidate(binary_invalid_data)
