from setuptools import setup, find_packages

setup(
    # pending https://github.com/paul-nameless/pyfswatch/issues/9
    name="fswatch",
    version="0.1",
    description="Python bindings for libfswatch.",
    packages=find_packages(),
)
