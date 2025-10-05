from protobuf_test_generator.formatters.c_array import CArrayFormatter
from protobuf_test_generator.formatters.hex import HexFormatter
from protobuf_test_generator.formatters.binary import BinaryFormatter
from protobuf_test_generator.formatters.json import JSONFormatter


def test_c_array_formatter():
    formatter = CArrayFormatter()
    data = b"\x08\x40\x10\xad"
    expected_output = (
        "const uint8_t data[] = {0x08, 0x40, 0xad};\nconst size_t data_size = 4;"
    )
    output = formatter.format(data, "data")
    assert output == expected_output


def test_hex_formatter():
    formatter = HexFormatter()
    data = b"\x08\x40\x10\xad"
    expected_output = "084010ad"
    output = formatter.format(data)
    assert output == expected_output


def test_binary_formatter():
    formatter = BinaryFormatter()
    data = b"\x08\x40\x10\xad"
    expected_output = b"\x08\x40\x10\xad"
    output = formatter.format(data)
    assert output == expected_output


def test_json_formatter():
    formatter = JSONFormatter()
    data = {"age": 75, "username": "john_doe"}
    expected_output = '{"age": 75, "username": "john_doe"}'
    output = formatter.format(data)
    assert output == expected_output
