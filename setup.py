from setuptools import setup, find_packages
from typing import List


HYPE_E_DOT = "-e ."


def get_requirements(file_path: str) -> list[str]:
    """
    Return the list of requirements from a requirements file.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = [req.strip() for req in file_obj.readlines() if req.strip()]

        # remove editable install marker if present
        if HYPE_E_DOT in requirements:
            requirements.remove(HYPE_E_DOT)

    return requirements


# Use a src/ layout: packages live under the `src` directory.
setup(
    name="mlproject_1",
    version="0.1.0",
    author="Richard Obeng",
    author_email="richardkwabenaobeng17@gmail.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements("requirements.txt"),
)
