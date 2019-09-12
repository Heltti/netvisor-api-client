import os
import re

from setuptools import find_packages, setup

HERE = os.path.dirname(os.path.abspath(__file__))


def get_version():
    filename = os.path.join(HERE, 'netvisor_api_client', '__init__.py')
    contents = open(filename).read()
    pattern = r"^__version__ = '(.*?)'$"

    return re.search(pattern, contents, re.MULTILINE).group(1)


setup(
    name='netvisor-api-client',
    version=get_version(),
    description='Python client for the Netvisor API',
    long_description="",
    author='Heltti Oy',
    author_email='dev@heltti.fi',
    url='https://github.com/Heltti/netvisor-api-client',
    packages=find_packages(),
    package_data={
        '': ['LICENSE']
    },
    license=open('LICENSE').read(),
    platforms='any',
    install_requires=[
        'inflection',
        'marshmallow<3.0.0',
        'requests',
        'xmltodict>=0.10.1',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
