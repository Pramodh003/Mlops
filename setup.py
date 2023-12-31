from setuptools import find_packages,setup
from typing import List


HYPHON_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    
    '''
    requirements = []
    
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","")for req in requirements]
        
        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)
            
    return requirements
        
    

setup(
    name="Mlproject",
    version="0.0.1",
    author="pramodh",
    author_email="pramodhbr29@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)