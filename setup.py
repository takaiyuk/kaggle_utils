from setuptools import find_packages, setup


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="kaggle_utils",
    version="0.0.2",
    packages=find_packages(),
    install_requires=_requires_from_file("requirements.txt"),
    description="utility scripts for kaggle",
    author="Yuki Nakatsuka",
)
