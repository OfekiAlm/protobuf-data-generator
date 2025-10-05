# API Reference for Protobuf Test Data Generator

## Overview

The Protobuf Test Data Generator is a Python package designed to facilitate the generation of valid and invalid test data for Protocol Buffers (protobuf). This package is particularly useful for testing protobuf implementations, validation logic, and creating test vectors for various protobuf files, including those used by ProtoValidate.

## Installation

To install the Protobuf Test Data Generator, ensure you have Python and pip installed, then run:

```bash
pip install protobuf-test-data-generator
```

## Usage

### Command-Line Interface

You can use the command-line interface to generate test data directly from the terminal. The basic syntax is:

```bash
python -m protobuf_test_generator <options> <proto_file> <message>
```

#### Options

- `--invalid`: Generate invalid data.
- `--field FIELD`: Specify the field to violate (for invalid data).
- `--rule RULE`: Specify the rule to violate (for invalid data).
- `--format FORMAT`: Specify the output format (default: `c_array`).
- `--output FILE`: Specify the output file (default: stdout).
- `--seed SEED`: Set a random seed for reproducibility.
- `-I DIR`: Include path for proto files.

### Python API

You can also use the package programmatically in your Python scripts. Here’s a basic example:

```python
from protobuf_test_generator import DataGenerator

# Initialize the generator
gen = DataGenerator('path/to/proto_file.proto', include_paths=['path/to/includes'])

# Generate valid data
valid_data = gen.generate_valid('MessageName', seed=42)

# Generate invalid data
invalid_data = gen.generate_invalid('MessageName', violate_field='field_name', violate_rule='rule_name')

# Encode to binary
binary_data = gen.encode_to_binary('MessageName', valid_data)
```

## Supported Formats

The generated test data can be formatted in various ways:

- **C Array**: Output as a C array for embedding in C code.
- **Binary**: Raw binary format for direct use.
- **Hex**: Hexadecimal string for debugging.
- **JSON**: JSON format for easy inspection.

## Constraint Systems

The Protobuf Test Data Generator supports multiple constraint systems, including:

- **Nanopb**: Constraints specific to nanopb.
- **ProtoValidate**: Constraints specific to ProtoValidate.
- **BufValidate**: Constraints specific to BufValidate.

Each constraint system has its own set of rules and validation logic, allowing for flexible test data generation.

## Examples

### Generating Valid Data

```bash
python -m protobuf_test_generator --format json my_proto.proto MyMessage
```

### Generating Invalid Data

```bash
python -m protobuf_test_generator --invalid --field age --rule lte my_proto.proto MyMessage
```

## Integration with Other Libraries

The Protobuf Test Data Generator can be integrated with other libraries and frameworks for testing, such as pytest. You can create fixtures that utilize the generator to produce test data for your unit tests.

## Contributing

Contributions to the Protobuf Test Data Generator are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request on the project's GitHub repository.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.