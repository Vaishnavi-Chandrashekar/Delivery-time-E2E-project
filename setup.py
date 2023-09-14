from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "Machine Learning Project"
VERSION = "0.0.1"
DESCRIPTION = "Machine learning project - modular coding"
AUTHOR_NAME = "Vaishnavi Chandrashekar"
AUTHOR_EMAIL = "vcyadav2k@gmail.com"

REQUIRMENTS_FILE_NAME = "requirments.txt"

HYPEN_E_DOT = "-e ."
# requiremnts.txt file open
# read
# \n ""
def get_requirments_list()->List[str]:
    with open(REQUIRMENTS_FILE_NAME) as requirement_file:
        requirment_list = requirement_file.readlines()
        requirment_list = [requirment_name.replace("\n","") for requirment_name in requirment_list]
    
        if HYPEN_E_DOT in requirment_list:
            requirment_list.remove(HYPEN_E_DOT)
            
        return requirment_list
    

setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=AUTHOR_EMAIL,
      packages=find_packages(),
      install_requires = get_requirments_list()
     )



