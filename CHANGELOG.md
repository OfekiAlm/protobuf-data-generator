# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2025-10-07

### Added
- Official support for Python 3.13, including refreshed protobuf/grpc wheels.
- Second console entry point `protobuf-data-generator` alongside the existing hyphenated name for easier discovery.

### Changed
- Bumped minimum versions of `protobuf` and `grpcio-tools` to pick up Python 3.13-compatible builds.
- Updated packaging metadata and documentation to reflect the broader Python support window.

## [0.1.0] - 2025-10-05

### Added
- Initial public release of `protobuf-data-generator`.
- Lightweight proto parser capable of extracting message metadata, enums, and validation rules.
- Constraint handlers for Protovalidate and Nanopb rule sets.
- Deterministic data generator producing valid and deliberately invalid payloads, plus binary envelope encoding.
- Formatting utilities for C arrays, hex, JSON, and binary outputs.
- Showcase test suite and sample protos demonstrating end-to-end usage.
