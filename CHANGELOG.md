# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-10-05

### Added
- Initial public release of `protobuf-data-generator`.
- Lightweight proto parser capable of extracting message metadata, enums, and validation rules.
- Constraint handlers for Protovalidate and Nanopb rule sets.
- Deterministic data generator producing valid and deliberately invalid payloads, plus binary envelope encoding.
- Formatting utilities for C arrays, hex, JSON, and binary outputs.
- Showcase test suite and sample protos demonstrating end-to-end usage.
