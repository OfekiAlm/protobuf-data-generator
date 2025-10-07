from pathlib import Path

from setuptools import find_packages, setup

BASE_DIR = Path(__file__).parent

with (BASE_DIR / "README.md").open(encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="protobuf-data-generator",
    version="1.1.0",
    author="Ofek Almog",
    author_email="ofekalm100@gmail.com",
    description="Generate valid and invalid protobuf payloads for comprehensive testing.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OfekiAlm/protobuf-data-generator",
    project_urls={
        "Source": "https://github.com/OfekiAlm/protobuf-data-generator",
        "Bug Tracker": "https://github.com/OfekiAlm/protobuf-data-generator/issues",
        "Documentation": "https://github.com/OfekiAlm/protobuf-data-generator#readme",
    },
    license="MIT",
    keywords=["protobuf", "testing", "nanopb", "data generator", "validation"],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8,<3.14",
    install_requires=[
        "protobuf>=6.31.1,<7.0.0",
        "grpcio-tools>=1.75.1,<2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.2",
            "black",
            "flake8",
            "mypy",
        ],
    },
    entry_points={
        "console_scripts": [
            "protobuf-test-data-generator=protobuf_test_generator.cli:main",
            "protobuf-data-generator=protobuf_test_generator.cli:main",
        ],
    },
)