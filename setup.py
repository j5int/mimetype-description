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
    version="0.0.2",
    author="Christian Gutierrez",
    author_email="chesstrian@gmail.com",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=["cached-property==1.5.1"]
)