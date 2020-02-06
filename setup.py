import os
import sys
from distutils.core import setup
from typing import List

_minimum_version = (3, 7)

if sys.version_info < _minimum_version:
    raise RuntimeError('Required Python {}'.format(
        '.'.join([str(i) for i in _minimum_version])
    ))

version = '0.1.0'

def list_packages(path: str = None) -> List[str]:
    actual_path = path
    package_list = []

    if not actual_path:
        actual_path = 'keymaster'
        package_list.append(actual_path)

    for node_name in os.listdir(actual_path):
        if node_name[0] in ['.', '_']:
            continue

        sub_path = os.path.join(actual_path, node_name)
        print(sub_path)

        if not os.path.isdir(sub_path):
            print(' - skipped (not dir)')
            continue

        print(' - included')

        package_list.append(sub_path)
        package_list.extend(list_packages(sub_path))

    return [
        pkg_path.replace(r'/', '.')
        for pkg_path in package_list
    ]

package_list = list_packages()

setup(
    name='keymaster',
    version=version,
    description='Key/Secret Management System',
    license='Apache 2.0',
    author='Juti Noppornpitak',
    author_email='juti_n@yahoo.co.jp',
    url='https://github.com/shiroyuki/gallium',
    packages=['keymaster_pb2', 'keymaster_pb2_grpc'] + package_list,
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
        'keyring',
        'pyperclip',
    ],
    python_requires='>=3.7',
    entry_points = {
        'console_scripts': [
            'keymaster=keymaster.client.starter:activate',
            'km=keymaster.client.starter:activate',
        ],
    }
)
