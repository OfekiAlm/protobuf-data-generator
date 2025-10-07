# Protobuf Test Data Generator - Quick Start

## Overview

The **Protobuf Test Data Generator** is a Python package designed to generate valid and invalid protobuf test data based on validation constraints defined in `.proto` files. This tool is useful for testing your protobuf-generated code, validation logic, and creating test vectors for various protobuf implementations, including those used by ProtoValidate.

## Installation

To install the package, ensure you have Python and pip installed, then run:

```bash
pip install .
```

This will install the package along with its dependencies.

## Quick Examples

### 1. Generate Valid Data (C Array)

```bash
protobuf-data-generator --proto-file test_basic.proto --message BasicValidation
```

Output:
```c
const uint8_t basicvalidation_data[] = {0x08, 0x40, 0x10, 0xad, ...};
const size_t basicvalidation_data_size = 252;
```

### 2. Generate Invalid Data (Violating a Specific Rule)

```bash
protobuf-data-generator --proto-file test_basic.proto --message BasicValidation \
  --invalid --field age --rule lte
```

This generates data where `age > 150`, violating the `lte = 150` constraint.

### 3. Generate Hex Output

```bash
protobuf-data-generator --proto-file test_basic.proto --message BasicValidation \
  --format hex
```

Output:
```
084b10321801b6a503ba...
```

### 4. Save to Binary File

```bash
protobuf-data-generator --proto-file test_basic.proto --message BasicValidation \
  --format binary -o test_data.bin
```

## Python API Usage

### Basic Generation

```python
from protobuf_test_generator import DataGenerator

# Create generator
gen = DataGenerator('test_basic.proto')

# Generate valid data
valid_data = gen.generate_valid('BasicValidation', seed=42)
print(valid_data)
# {'age': 75, 'username': 'john_doe', ...}

# Encode to binary
binary = gen.encode_to_binary('BasicValidation', valid_data)

# Format as C array
c_code = gen.format_output(binary, 'c_array', 'test_data')
print(c_code)
```

### Generate Invalid Data

```python
# Random violation
invalid_data = gen.generate_invalid('BasicValidation')

# Specific violation
invalid_data = gen.generate_invalid(
    'BasicValidation',
    violate_field='age',
    violate_rule='lte'
)
print(invalid_data['age'])  # Will be > 150
```

## Supported Validation Rules

### Numeric (int32, int64, uint32, uint64, float, double)
- `gt`, `gte`, `lt`, `lte` - Range constraints
- `const` - Exact value
- `in`, `not_in` - Allowed/forbidden values

### String
- `min_len`, `max_len` - Length constraints
- `prefix`, `suffix` - Required prefix/suffix
- `contains` - Required substring
- `ascii` - ASCII-only characters
- `in`, `not_in` - Allowed/forbidden values

### Repeated Fields
- `min_items`, `max_items` - Count constraints
- `unique` - All items must be unique

### Boolean
- `const` - Exact value

## Example Proto File

```protobuf
syntax = "proto3";
import "validate.proto";

message User {
  int32 age = 1 [
    (validate.rules).int32.gte = 18,
    (validate.rules).int32.lte = 120
  ];
  
  string email = 2 [
    (validate.rules).string.contains = "@",
    (validate.rules).string.min_len = 5
  ];
  
  repeated string tags = 3 [
    (validate.rules).repeated.min_items = 1,
    (validate.rules).repeated.max_items = 10
  ];
}
```

## Output Formats

| Format | Description | Use Case |
|--------|-------------|----------|
| `c_array` | C array with size | Embed in C test files |
| `binary` | Raw bytes | Save to file for testing |
| `hex` | Hex string | Debugging, documentation |
| `json` | JSON format | Inspection, debugging |

## CLI Options Reference

```
usage: protobuf-data-generator [-h] [--invalid] [--field FIELD] [--rule RULE]
                               [--format {binary,c_array,hex,json}] [--output OUTPUT]
                               [--seed SEED] [-I INCLUDE] [--proto-file PROTO_FILE]
                               [--message MESSAGE]
                               [proto_file] [message]

positional arguments:
  proto_file            Path to .proto file
  message               Message name to generate data for

optional arguments:
  -h, --help            Show help message
  --proto-file PROTO_FILE, --proto_file PROTO_FILE
                        Proto file path (alternative to positional argument)
  --message MESSAGE     Message name (alternative to positional argument)
  --invalid             Generate invalid data
  --field FIELD         Field to violate (for invalid data)
  --rule RULE           Rule to violate (for invalid data)
  --format FORMAT       Output format (default: c_array)
  --output FILE, -o     Output file (default: stdout)
  --seed SEED           Random seed for reproducibility
  -I INCLUDE, --include INCLUDE
                        Include path for proto files
```

## Integration with ProtoValidate

The Protobuf Test Data Generator can be easily adapted to work with ProtoValidate by defining appropriate constraints in the `constraints/protovalidate.py` file. This allows users to generate test data that adheres to the validation rules specified in ProtoValidate.

## Tips & Best Practices

1. **Use Seeds**: Always use a seed for reproducible test data.
2. **Test Boundaries**: Focus on edge cases (min/max values).
3. **Systematic Coverage**: Test all validation rules for each field.
4. **Version Control**: Check in generated test data for regression testing.
5. **Document Violations**: Add comments explaining what each invalid test case violates.

## Limitations

- Nested messages not fully supported yet.
- Enum validation limited.
- Map fields have basic support only.
- Some complex rules may need custom handling.

## Example Script

See `examples/basic_usage.py` for a complete example of generating test data.

## Contributing

Found a bug or want to add a feature? Contributions are welcome! Areas for improvement include nested message support, enum validation, and performance optimizations.

## See Also

- [Full Documentation](api_reference.md)
- [ProtoValidate Project](https://github.com/bufbuild/protoc-gen-validate)