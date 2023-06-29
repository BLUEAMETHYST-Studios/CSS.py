from setuptools import setup, find_packages
from sys import argv

with open("README.md", "r") as file:
    readme = file.read()
    file.close()

with open("VERSION", "r") as file2:
    ver = file2.read()
    file2.close()

setup(
    name="CSSdotPy",
    version=ver,
    description="A way of writing CSS with a Python library.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="BLUEAMETHYST Studios",
    url="https://github.com/BLUEAMETHYST-Studios/CSS.py",
    packages=find_packages(),
    keywords=["css", "open-source"],
    license="GNU GENERAL PUBLIC LICENSE VERSION 3",
)