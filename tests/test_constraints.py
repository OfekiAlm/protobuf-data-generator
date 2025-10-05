import pytest
from protobuf_test_generator.core.generator import DataGenerator
from protobuf_test_generator.constraints.protovalidate import ProtoValidateConstraints


@pytest.fixture
def data_generator():
    return DataGenerator(
        "tests/fixtures/test_protovalidate.proto", include_paths=["tests/fixtures"]
    )


def test_valid_data_generation(data_generator):
    valid_data = data_generator.generate_valid("User")
    assert valid_data["age"] >= 18
    assert valid_data["age"] <= 120
    assert "@" in valid_data["email"]
    assert len(valid_data["email"]) >= 5


def test_invalid_data_generation(data_generator):
    invalid_data = data_generator.generate_invalid(
        "User", violate_field="age", violate_rule="lte"
    )
    assert invalid_data["age"] > 120

    invalid_data = data_generator.generate_invalid(
        "User", violate_field="email", violate_rule="min_len"
    )
    assert len(invalid_data["email"]) < 5


def test_constraint_application(data_generator):
    constraints = ProtoValidateConstraints("tests/fixtures/test_protovalidate.proto")
    all_fields = data_generator.get_all_fields("User")

    for field_name, field_info in all_fields.items():
        for constraint in field_info.constraints:
            invalid_data = data_generator.generate_invalid(
                "User", violate_field=field_name, violate_rule=constraint.rule_type
            )
            assert not constraints.validate(
                field_name, invalid_data[field_name]
            )  # Ensure validation fails for invalid data


def test_edge_cases(data_generator):
    edge_case_data = data_generator.generate_valid("User", seed=42)
    assert edge_case_data["age"] == 18  # Test lower boundary
    edge_case_data["age"] = 120
    assert edge_case_data["age"] == 120  # Test upper boundary

    invalid_edge_case_data = data_generator.generate_invalid(
        "User", violate_field="age", violate_rule="gte"
    )
    assert (
        invalid_edge_case_data["age"] < 18
    )  # Ensure it violates the lower boundary constraint

    invalid_edge_case_data = data_generator.generate_invalid(
        "User", violate_field="age", violate_rule="lte"
    )
    assert (
        invalid_edge_case_data["age"] > 120
    )  # Ensure it violates the upper boundary constraint
