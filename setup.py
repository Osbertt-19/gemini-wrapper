import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="geminiwrapper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "google-generativeai",
    ],
    description="Library for generating consistent Gemini API outputs and wrapping them with json and python objects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Min Htet Naing",
    author_email="minhtetnaing25mhn@gmail.com",
    url="https://github.com/Osbertt-19/gemini-wrapper",
    keywords="gemini, object, json, wrapper, consistent",
    classifiers=[
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python",
    ],
)
