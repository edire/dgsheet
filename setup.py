# setup.py placed at root directory
from setuptools import setup
setup(
    name='dgsheet',
    version='0.1.1',
    author='Eric Di Re',
    description='Custom GSheet and Pandas Communication',
    url='https://github.com/edire/dgsheet.git',
    python_requires='>=3.9',
    packages=['dgsheet'],
    install_requires=['gspread', 'pandas']
)