from setuptools import setup, find_packages

setup(
    name='test_package',
    packages=find_packages(),
    version='0.2',
    package_data={'test_package': ['data/**/*']},
)