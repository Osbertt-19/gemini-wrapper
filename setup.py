from setuptools import setup, find_packages

setup(
    name="geminiwrapper",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "google-generativeai",
    ],
    description="Library for generating consistent Gemini API outputs and wrapping them with json and python objects",
    author="Min Htet Naing",
    author_email="minhtetnaing25mhn@gmail.com",
    url="https://github.com/Osbertt-19/gemini-wrapper",
    keywords=["gemini", "object", "json", "wrapper", "consistent"],
)
