# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='liqpay-python3',
    version='1.1.2',
    author='PaulGregor',
    description='LiqPay SDK for Python 3',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    install_requires=['requests']
)
