import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ['-sv', 'tests']

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

def get_requirements():
    """ Returns the requirements of libs. """

    with open('requirements.txt', 'r') as f:
        requirements = f.readlines()
    requires = []
    for require in requirements:
        if require.startswith("#") or require.startswith("\n"):
            continue
        else:
            requires.append(require.replace("\n", ""))
    return requires

def get_version():
    with open('__init__.py') as f:
        for line in f.readlines():
            if "__version__" in line:
                return line.strip().split("=")[-1].strip(" '")
    raise ValueError("could not read version")

def get_packages():
    packages = find_packages()
    packages = ['{}.{}'.format('uniq', package) for package in packages]
    packages.append('uniq')
    return packages

with open('README.md') as file_readme:
    readme = file_readme.read()

setup(
    name='uniq',
    version=get_version(),
    description="A Python API client library for Cisco's Application Policy "
                "Infrastructure Controller Enterprise Module (APIC-EM) Northbound APIs.",
    long_description=readme,
    packages=get_packages(),
    package_dir={'uniq': ''},
    install_requires=get_requirements(),
    include_package_data=True,
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    license='Apache License 2.0',
    platforms=['unix', 'linux', 'osx'],
    author='Amey Patil, Li Feng',
    author_email='ameyspatil@gmail.com, fengli616@gmail.com',
    )

