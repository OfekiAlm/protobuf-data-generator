from protobuf_test_generator import DataGenerator

def main():
    # Create a generator instance for a specific .proto file
    generator = DataGenerator('path/to/your/proto_file.proto', include_paths=['path/to/include'])

    # Generate valid data for a specific message
    valid_data = generator.generate_valid('YourMessageName', seed=42)
    print("Valid Data:", valid_data)

    # Generate invalid data for a specific message
    invalid_data = generator.generate_invalid('YourMessageName', violate_field='your_field', violate_rule='lte')
    print("Invalid Data:", invalid_data)

    # Encode valid data to binary format
    binary_data = generator.encode_to_binary('YourMessageName', valid_data)
    print("Binary Data:", binary_data)

    # Format output as C array
    c_array_output = generator.format_output(binary_data, 'c_array', 'test_data')
    print("C Array Output:", c_array_output)

if __name__ == "__main__":
    main()