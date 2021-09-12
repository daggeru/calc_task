from distutils.core import setup
from setuptools import find_packages
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'Full_Stack_Recruitment_Task.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
    name='Recruitment task',
    packages=find_packages('.'),
    version='0.0.1',
    license='MIT',
    description='Recruitment task',

    long_description=long_description,
    long_description_context_type='text/markdown',

    author='Dagmara',
    author_email='',
    url='',
    download_url='',
    keywords=[],
    install_requires=['boto3', 'connexion'],

    classifiers=[]
)