from setuptools import setup, find_packages

setup(
    name = "mathematics",                  # Package name
    version = "1.0",                     # Version number
    packages = find_packages(),            # Automatically finds all packages
    install_requires = [                   # Dependencies
        "decimal",
        "turtle"
    ],
    author = "Viraj Sharma",               # Your name
    description = "A cool Python mathematical package, which arithmatic functions + some constants + geometry functions + advanced math + algebra, has grade 8 till 12th maths with some crazy features.", # Short description
    long_description = open("README.md").read(),  # Readme file
    long_description_content_type = "text/markdown",
    url = "https://github.com/yourusername/mathematics",  # GitHub repo
    classifiers = [                         # Metadata for PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.6",              # Minimum Python version
)
