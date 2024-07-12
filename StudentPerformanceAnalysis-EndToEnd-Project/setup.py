from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]: 
    '''
    It will take the libraries stored in requirement.txt file

    Returns the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='Student Performance Analysis Project',
version='0.0.1',
author='Sottim',
author_email='santosottim@gmail.com',
packages=find_packages(),
install_requires= get_requirements('requirements.txt')
)