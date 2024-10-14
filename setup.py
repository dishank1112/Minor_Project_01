from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_req(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='Ml_minor',
    version='0.0.1',
    author='Dishank Jain',
    author_email='jainbharti9382@gmail.com',
    packages=find_packages(),
    install_requires=get_req('requirements.txt')  
)
