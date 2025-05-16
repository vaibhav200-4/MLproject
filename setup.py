from setuptools import find_packages, setup
from typing import List
def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements
    """
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements


setup(

    name="mlproject",
    version="0.0.1",
    author="vaibhav soni",
    description="A small example package",
    author_email="vaibhavsoni2004v@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    )

