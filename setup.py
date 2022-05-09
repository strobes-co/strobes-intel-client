""" __Doc__ File handle class """
from setuptools import find_packages, setup
from strobes_intel_client.__version__ import __version__


def dependencies(imported_file):
    """ __Doc__ Handles dependencies """
    with open(imported_file) as file:
        return file.read().splitlines()


with open("README.md") as file:
    setup(
        name="Strobes Intel Client",
        license="GPLv3",
        description="Strobes Intel Client is a service which communicates with strobes intel and fetches cve data in pydantic model.",
        long_description=file.read(),
        long_description_content_type="text/markdown",
        url="https://github.com/strobes-co/strobes-intel-client",
        author="Akhil Reni",
        version=__version__,
        author_email="akhil@wesecureapp.com",
        packages=find_packages(
            exclude=('tests')),
        package_data={
            'strobes_intel_client': [
                '*.txt',
                '*.json']},
        python_requires=">=3.6",
        install_requires=dependencies("requirements.txt"),
        entry_points={
            'console_scripts': ['strobes_intel = strobes_intel_client.main:main']},
        include_package_data=True)
