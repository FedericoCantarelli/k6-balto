#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Federico cantarelli",
    author_email='fede.cantarelli98@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Package to visualize and analyze K6 API load testing results.",
    entry_points={
        'console_scripts': [
            'k6_malinois=k6_malinois.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='k6_malinois',
    name='k6_malinois',
    packages=find_packages(include=['k6_malinois', 'k6_malinois.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/FedericoCantarelli/k6-malinois.git',
    version='0.1.0',
    zip_safe=False,
)
