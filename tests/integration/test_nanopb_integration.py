import pytest
from protobuf_test_generator import DataGenerator


@pytest.fixture
def setup_nanopb_generator():
    # Initialize the DataGenerator with a sample nanopb proto file
    generator = DataGenerator(
        "tests/fixtures/test_nanopb.proto", include_paths=["tests/fixtures"]
    )
    return generator


def test_generate_valid_data(setup_nanopb_generator):
    generator = setup_nanopb_generator
    valid_data = generator.generate_valid("BasicValidation", seed=42)
    assert valid_data is not None
    assert "age" in valid_data
    assert 18 <= valid_data["age"] <= 120  # Assuming age constraints


def test_generate_invalid_data(setup_nanopb_generator):
    generator = setup_nanopb_generator
    invalid_data = generator.generate_invalid(
        "BasicValidation", violate_field="age", violate_rule="lte"
    )
    assert invalid_data is not None
    assert invalid_data["age"] > 120  # Assuming age constraints


def test_encode_to_binary(setup_nanopb_generator):
    generator = setup_nanopb_generator
    valid_data = generator.generate_valid("BasicValidation", seed=42)
    binary_data = generator.encode_to_binary("BasicValidation", valid_data)
    assert binary_data is not None
    assert isinstance(binary_data, bytes)


def test_format_output(setup_nanopb_generator):
    generator = setup_nanopb_generator
    valid_data = generator.generate_valid("BasicValidation", seed=42)
    binary_data = generator.encode_to_binary("BasicValidation", valid_data)
    c_array_output = generator.format_output(binary_data, "c_array", "test_data")
    assert c_array_output.startswith("const uint8_t test_data[] = {")
    assert "};" in c_array_output


def test_integration_with_nanopb_validation(setup_nanopb_generator):
    generator = setup_nanopb_generator
    valid_data = generator.generate_valid("BasicValidation", seed=42)
    binary_data = generator.encode_to_binary("BasicValidation", valid_data)

    # Here you would integrate with the actual nanopb validation logic
    # For example, using pb_decode and pb_validate functions
    # assert pb_validate_BasicValidation(decoded_message) is True

    assert len(binary_data) > 0
    # This is a placeholder for the actual validation check
    assert True  # Replace with actual validation logic
