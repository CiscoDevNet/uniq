import sys
from datetime import date
import subprocess

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
    """ Returns the version of apic-em.

    Example:
        '1.2.0.x', 1.2.0 is the version number of APIC-EM, and x is the number of pull requests
        since 1.2.0 released.
    """

    with open('__init__.py') as f:
        for line in f.readlines():
            if '__version__' in line:
                apicem_version = line.strip().split("=")[-1].strip(" '")
            if '__first_release_date__' in line:
                first_release_data_str = line.strip().split("=")[-1].strip(" '")
                first_release_data = date(*[int(num) for num in first_release_data_str.split('.')])
                num_commits = get_cr_num(first_release_data)
        return '{apicem_version}.{num_commits}'.format(
            apicem_version=apicem_version, num_commits=num_commits)

    raise ValueError("could not read version")

def get_cr_num(start_date):
    """ Calculate number of PRs since start date.

    Args:
        start_date (datetime.date): Date to calculate CRs number from.

    Returns:
        Number of Crs since start date. (int)
    """

    command = ['git', 'log', '--oneline', '--since="{} 00:00:00"'.format(start_date.isoformat())]
    process = subprocess.Popen(command, stdout=subprocess.PIPE)
    outputs = process.stdout.readlines()
    print("Change log: {}".format(outputs[0]))
    return len(outputs)

def get_packages():
    """ Returns all packages of uniq. """

    packages = find_packages()
    packages = ['{}.{}'.format('uniq', package) for package in packages]
    packages.append('uniq')
    return packages

if __name__ == '__main__':
    with open('README.rst') as file_readme:
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
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: Apache Software License',
            'Programming Language :: Python :: 3 :: Only',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Topic :: Utilities'
        ]
        )
