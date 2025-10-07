import importlib
import sys
from pathlib import Path

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

cli_module = importlib.import_module("protobuf_test_generator.cli")
importlib.reload(cli_module)
main = cli_module.main


@pytest.mark.parametrize(
    "argv",
    [
        [
            "protobuf-data-generator",
            "tests/fixtures/showcase.proto",
            "Showcase",
            "--format",
            "json",
            "--seed",
            "1",
        ],
        [
            "protobuf-data-generator",
            "--proto-file",
            "tests/fixtures/showcase.proto",
            "--message",
            "Showcase",
            "--format",
            "json",
            "--seed",
            "1",
            "--include",
            "tests/fixtures",
        ],
        [
            "protobuf-data-generator",
            "--proto_file",
            "tests/fixtures/showcase.proto",
            "--message",
            "Showcase",
            "--format",
            "json",
            "--seed",
            "1",
        ],
    ],
)
def test_cli_supports_positional_and_optional_arguments(monkeypatch, capsys, argv):
    monkeypatch.setattr(sys, "argv", argv)

    main()

    captured = capsys.readouterr()
    assert '"message": "Showcase"' in captured.out
    assert captured.err == ""


def test_cli_rejects_conflicting_arguments(monkeypatch):
    argv = [
        "protobuf-data-generator",
        "tests/fixtures/showcase.proto",
        "Showcase",
        "--proto-file",
        "tests/fixtures/test_basic.proto",
    ]
    monkeypatch.setattr(sys, "argv", argv)

    with pytest.raises(SystemExit) as exc:
        main()

    assert exc.value.code == 2
