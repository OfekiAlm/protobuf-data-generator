from protobuf_test_generator import (
    DataGenerator,
    NanopbConstraints,
    ProtoParser,
    validate_protovalidate,
)
from protobuf_test_generator.formatters.binary import BinaryFormatter
from protobuf_test_generator.formatters.hex import HexFormatter
from protobuf_test_generator.formatters.json import JSONFormatter


def test_full_feature_showcase():
    proto_path = "tests/fixtures/showcase.proto"
    include_paths = ["tests/fixtures"]

    # Parse proto definitions from file path and raw text
    path_parser = ProtoParser()
    messages_from_path = path_parser.parse(proto_path)
    assert {"Showcase", "NestedProfile"}.issubset(messages_from_path.keys())

    text_parser = ProtoParser()
    with open(proto_path, "r", encoding="utf-8") as handle:
        proto_text = handle.read()
    messages_from_text = text_parser.parse(proto_text)
    showcase_fields = messages_from_text["Showcase"].fields
    assert showcase_fields["status"].enum_values == [
        "STATUS_UNSPECIFIED",
        "ACTIVE",
        "INACTIVE",
        "PENDING",
    ]
    assert (
        showcase_fields["history"].enum_values == showcase_fields["status"].enum_values
    )

    # Generate valid and invalid payloads using protovalidate constraints
    generator = DataGenerator(
        proto_path,
        include_paths=include_paths,
        constraints_type="protovalidate",
    )
    showcase_field_map = generator.get_all_fields("Showcase")
    assert set(showcase_field_map) == {
        "age",
        "email",
        "username",
        "tags",
        "status",
        "history",
        "keywords",
        "profile",
    }

    valid_payload = generator.generate_valid("Showcase", seed=42)
    assert valid_payload["age"] == showcase_field_map["age"].get_constraint_value("gte")
    assert "@" in valid_payload["email"]
    assert valid_payload["username"] == "aaa"
    assert len(valid_payload["tags"]) == showcase_field_map[
        "tags"
    ].get_constraint_value("min_items")
    assert len(valid_payload["keywords"]) == showcase_field_map[
        "keywords"
    ].get_constraint_value("min_items")
    assert valid_payload["status"] == showcase_field_map["status"].enum_values[0]
    assert valid_payload["history"] == [showcase_field_map["history"].enum_values[0]]
    assert valid_payload["profile"] is None

    invalid_age = generator.generate_invalid(
        "Showcase", violate_field="age", violate_rule="lte", seed=42
    )
    assert invalid_age["age"] > showcase_field_map["age"].get_constraint_value("lte")

    invalid_email = generator.generate_invalid(
        "Showcase", violate_field="email", violate_rule="min_len", seed=42
    )
    assert len(invalid_email["email"]) < showcase_field_map[
        "email"
    ].get_constraint_value("min_len")

    invalid_tags = generator.generate_invalid(
        "Showcase", violate_field="tags", violate_rule="unique", seed=42
    )
    assert len(set(invalid_tags["tags"])) < len(invalid_tags["tags"])

    invalid_history = generator.generate_invalid(
        "Showcase", violate_field="history", violate_rule="max_items", seed=42
    )
    assert len(invalid_history["history"]) > showcase_field_map[
        "history"
    ].get_constraint_value("max_items")

    invalid_keywords = generator.generate_invalid(
        "Showcase", violate_field="keywords", violate_rule="min_items", seed=42
    )
    assert len(invalid_keywords["keywords"]) < showcase_field_map[
        "keywords"
    ].get_constraint_value("min_items")

    # Encode payloads and validate them with the protovalidate shim
    valid_binary = generator.encode_to_binary("Showcase", valid_payload)
    assert validate_protovalidate(valid_binary)

    invalid_binary = generator.encode_to_binary("Showcase", invalid_email)
    assert not validate_protovalidate(invalid_binary)

    # Showcase output formats
    c_array_output = generator.format_output(
        valid_binary, "c_array", "showcase_payload"
    )
    assert "const uint8_t showcase_payload[]" in c_array_output

    json_output = JSONFormatter.format(valid_payload)
    assert '"age": 18' in json_output

    hex_output = HexFormatter.format(valid_binary)
    assert isinstance(hex_output, str) and len(hex_output) > 0

    binary_output = BinaryFormatter().format(valid_binary)
    assert binary_output == valid_binary

    # Demonstrate nanopb constraints support
    nanopb_generator = DataGenerator(
        proto_path,
        include_paths=include_paths,
        constraints_type="nanopb",
    )
    nanopb_valid = nanopb_generator.generate_valid("Showcase", seed=7)
    nanopb_constraints = NanopbConstraints(proto_path, include_paths=include_paths)
    assert nanopb_constraints.validate_message("Showcase", nanopb_valid)

    nanopb_invalid = nanopb_generator.generate_invalid(
        "Showcase",
        violate_field="age",
        violate_rule="gte",
        seed=7,
    )
    assert nanopb_invalid["age"] < nanopb_generator.get_all_fields("Showcase")[
        "age"
    ].get_constraint_value("gte")
