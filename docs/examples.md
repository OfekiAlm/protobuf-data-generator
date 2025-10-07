# Examples of Using the Protobuf Test Data Generator

This document provides various examples of how to use the Protobuf Test Data Generator for generating valid and invalid protobuf test data. The generator can be applied to different protobuf files, including those used by ProtoValidate.

## Basic Usage

To generate valid protobuf data, you can use the following command:

```bash
protobuf-data-generator --proto-file path/to/your.proto --message YourMessage
```

This command will generate valid data for the specified message type in the provided protobuf file.

## Generating Invalid Data

To generate invalid data that violates specific constraints, you can use the `--invalid` flag along with the `--field` and `--rule` options:

```bash
protobuf-data-generator --proto-file path/to/your.proto --message YourMessage --invalid --field age --rule lte
```

This command generates data where the `age` field violates the `lte` constraint.

## Example with ProtoValidate

For protobuf files that utilize ProtoValidate, you can specify the appropriate message and constraints. Here’s an example command:

```bash
protobuf-data-generator --proto-file path/to/protovalidate.proto --message User --invalid --field email --rule min_len
```

This generates invalid data for the `email` field, ensuring it does not meet the minimum length requirement.

## Output Formats

The generator supports various output formats. You can specify the desired format using the `--format` option. For example, to get the output in JSON format:

```bash
protobuf-data-generator --proto-file path/to/your.proto --message YourMessage --format json
```

## Custom Constraints

You can also define custom constraints in your protobuf files and use the generator to test them. For example, if you have a custom constraint for a field, you can generate data that adheres to or violates that constraint:

```bash
protobuf-data-generator --proto-file path/to/your.proto --message YourMessage --invalid --field customField --rule customRule
```

## Conclusion

The Protobuf Test Data Generator is a versatile tool that can be used to generate both valid and invalid test data for various protobuf files, including those used with ProtoValidate. By utilizing the command-line interface, you can easily customize the data generation process to suit your testing needs.