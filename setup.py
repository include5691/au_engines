from setuptools import setup, find_packages

setup(
    name='au_engines',
    version='0.1.0',
    author='Andrey Pshenitsyn',
    description='E5 communication engines repo',
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv',
        'pyotp',
        'pyrogram',
        'pydantic'
    ],
)