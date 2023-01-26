#!/usr/bin/env python3

from setuptools import setup

setup(
    name="niconico_honsha",
    version="9.9.9",
    description='Explode Niconico Honsha [DEVELOPMENT VERSION]',
    author='okaits#7534',
    author_email='okaits7534@gmail.com',
    packages=["niconico_honsha"],
    install_requires=["setuptools"],
    entry_points={
        'console_scripts': [
            'honsha_explode = niconico_honsha.commands:show',
            'honsha_rm = niconico_honsha.commands:remove_file'
        ]
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities'
    ]
)