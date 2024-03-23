from setuptools import find_packages, setup

setup(
    name='tr34-sdk',
    packages=find_packages(),
    version='0.1.0dev1',
    description='Asynchronous sdk for top-rule34 api',
    author='StarMan',
    install_requires=["aiohttp"],
)