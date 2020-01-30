import sys

_minimum_version = (3, 7)

if sys.version_info < _minimum_version:
    raise RuntimeError('Required Python {}'.format(
        '.'.join([str(i) for i in _minimum_version])
    ))

version = '0.1.0'
from distutils.core import setup

setup(
    name='gallium',
    version=version,
    description='A micro CLI development framework',
    license='MIT',
    author='Juti Noppornpitak',
    author_email='juti_n@yahoo.co.jp',
    url='https://github.com/shiroyuki/gallium',
    packages=[
        'keymaster',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'gallium>=1.5.1',
        'imagination>=3.0.0',
        'kotoba',
        'cryptography',
    ],
    python_requires='>=3.7',
)
