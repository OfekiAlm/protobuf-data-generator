from protobuf_test_generator import DataGenerator

def main():
    # Create a data generator instance for a nanopb protobuf file
    gen = DataGenerator('path/to/test_nanopb.proto', include_paths=['path/to/proto'])

    # Generate valid data
    valid_data = gen.generate_valid('BasicValidation', seed=42)
    print("Valid Data:", valid_data)

    # Generate invalid data (violating a specific rule)
    invalid_data = gen.generate_invalid('BasicValidation', violate_field='age', violate_rule='lte')
    print("Invalid Data (age > 150):", invalid_data)

    # Encode valid data to binary
    binary_data = gen.encode_to_binary('BasicValidation', valid_data)
    print("Binary Data:", binary_data)

    # Format output as C array
    c_array_output = gen.format_output(binary_data, 'c_array', 'test_data')
    print("C Array Output:", c_array_output)

if __name__ == "__main__":
    main()