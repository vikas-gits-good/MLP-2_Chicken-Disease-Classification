from setuptools import find_packages, setup
from typing import List

Run_text = "-e ."


def get_requirements(File_path: str) -> List[str]:
    """This function returns the list of requirements

    Args:
        File_path (str): File path to 'requirements.txt'

    Returns:
        List[str]: list of libraries and their version number if specified
    """
    requirements = []
    with open(File_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if Run_text in requirements:
            requirements.remove(Run_text)

    return requirements


with open("README.md", "r", encoding="utf-8") as f:
    long_desc = f.read()

__version__ = "0.0.1"
Repo_name = "MLP-2_Chicken-Disease-Classification"
Author_name = "vikas-gits-good"
SRC_Repo = "cnnClassifier"
Author_email = "vikas.c.conappa@protonmail.com"

setup(
    name=SRC_Repo,
    version=__version__,
    author=Author_name,
    author_email=Author_email,
    description="CNN app for image classification",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{Author_name}/{Repo_name}",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    requires=get_requirements(File_path="requirements.txt"),
)
