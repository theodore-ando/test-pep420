import os
from setuptools import setup, find_packages

version_ns = {}
with open(os.path.join("funcx", "ep_version.py")) as f:
    exec(f.read(), version_ns)
version = version_ns['VERSION']

with open('requirements.txt') as f:
    install_requires = f.readlines()

setup(
    name='funcx-endpoint-tando-test',
    version=version,
    packages=find_packages(),
    description='test funcx endpoint submodule',
    install_requires=install_requires,
    python_requires=">=3.6.0",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering"
    ],
    keywords=[
        "funcX",
        "FaaS",
        "Function Serving"
    ],
    entry_points={},
    author='funcX team',
    author_email='labs@globus.org',
    license="Apache License, Version 2.0",
    url="https://github.com/theodore-ando/test-pep420"
)
