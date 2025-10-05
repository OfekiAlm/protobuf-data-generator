from protobuf_test_generator import DataGenerator

def main():
    # Create a data generator instance for a specific proto file
    gen = DataGenerator('path/to/your/proto_file.proto', include_paths=['path/to/include'])

    # Generate valid data
    valid_data = gen.generate_valid('YourMessageName', seed=42)
    print("Valid Data:", valid_data)

    # Generate invalid data by violating a specific constraint
    invalid_data = gen.generate_invalid('YourMessageName', violate_field='your_field', violate_rule='lte')
    print("Invalid Data:", invalid_data)

if __name__ == "__main__":
    main()