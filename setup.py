from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str) -> List[str]:
    """
    This function will return list of requirements
    """
    requirements = []
    Hypen_e_dot = '-e .'
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
    return requirements


setup(
    name='ML Project',
    version='0.0.1',
    author='Krishnaraj',
    author_email='krishnarajp2015@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
