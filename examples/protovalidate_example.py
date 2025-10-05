from protobuf_test_generator import DataGenerator

def main():
    # Initialize the data generator for a ProtoValidate .proto file
    proto_file = 'path/to/your/protovalidate.proto'  # Update with your actual proto file path
    message_name = 'YourMessage'  # Update with the actual message name you want to test

    # Create a generator instance
    generator = DataGenerator(proto_file)

    # Generate valid data
    valid_data = generator.generate_valid(message_name)
    print("Valid Data:", valid_data)

    # Generate invalid data (example: violating a specific rule)
    invalid_data = generator.generate_invalid(message_name, violate_field='your_field', violate_rule='lte')
    print("Invalid Data:", invalid_data)

    # Encode valid data to binary format
    binary_data = generator.encode_to_binary(message_name, valid_data)
    print("Binary Data:", binary_data)

if __name__ == "__main__":
    main()