import os
import re

from setuptools import find_packages, setup

HERE = os.path.dirname(os.path.abspath(__file__))


def get_version() -> str:
    contents = open(os.path.join(HERE, "netvisor_api_client", "__init__.py")).read()
    pattern = r"^__version__ = \"(.*?)\"$"

    return re.search(pattern, contents, re.MULTILINE).group(1)


def get_install_requires():
    with open(os.path.join(HERE, "requirements.txt"), "r") as requirements_file:
        return requirements_file.read().splitlines()


setup(
    name="netvisor-api-client",
    version=get_version(),
    description=open("README.md").read(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Heltti Oy",
    author_email="dev@heltti.fi",
    url="https://github.com/Heltti/netvisor-api-client",
    install_requires=get_install_requires(),
    packages=find_packages(exclude=["junit", "tests"]),
    package_data={"": ["LICENSE"]},
    license=open("LICENSE").read(),
    platforms="any",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
