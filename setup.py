from setuptools import setup, find_packages

setup(
    name='pyop',
    version='0.1.0',
    description='pyop: mis-use python in a useful way',
    packages=find_packages(include=['pyop']),
    url='https://github.com/guanyilun/pyop',
    author='Yilun Guan',
    author_email='zoom.aaron@gmail.com',
    license='GPLv3+',
    install_requires=['fn'],
)
