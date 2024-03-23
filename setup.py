from setuptools import find_packages, setup

setup(
    name='tr34_sdk',
    packages=find_packages(),
    description='Asynchronous sdk for top-rule34 api',
    author='StarMan12',
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)