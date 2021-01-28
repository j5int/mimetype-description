from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="mimetype-description",
    description="Human readable MIME type descriptions",
    license="MIT",
    url="https://github.com/chesstrian/mimetype-description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    version="0.0.5",
    author="Christian Gutierrez",
    author_email="chesstrian@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*,!=3.4.*,!=3.5.*,!=3.6.*,>=3.7"
)
