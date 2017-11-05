#!/usr/bin/env python3

# engineer_number module
#
# Copyright (c) 2012-2017 梅濁酒(umedoblock)
#
# This software is released under the MIT License.
# https://github.com/umedoblock/engineer_number

from distutils.core import setup

setup(
    name='engineer_number',
    packages=
        ['engineer_number', 'engineer_number.test', 'engineer_number.scripts'],
    version='1.0.5',
    description='Engineer Number calculate',
    package_dir={'engineer_number': 'engineer_number'},
    package_data={'engineer_number': [
                        'locale/engineer_number.pot',
                        'locale/engineer_number.*.po',
                        'locale/*/LC_MESSAGES/engineer_number.mo'
                   ]},
    author='梅濁酒(umedoblock)',
    author_email='umedoblock@gmail.com',
    url='https://github.com/umedoblock/engineer_number',
    download_url='',
    keywords=['engineer', 'SI'],
    license='MIT License',
    platforms=['unix', 'linux', 'osx', 'cygwin', 'win32'],
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Japanese',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    options = {
        'sdist': {
            'formats': ['gztar','zip'],
            'force_manifest': True,
        },
    },

    long_description = '''\
| Engineer Number calculate
| -------------------------
| 
| This module can easily calculate Engineer Number.
| 
| This version requires Python 3 or later.
| Python 2 version may be available but no support Python 2 version.
| 
| for example.
| 
| 0.
| >>> from engineer_number import EngineerNumber
| 
| 1.
| >>> nano470 = EngineerNumber("470n")
| >>> nano470
| EngineerNumber("470.000n")
| >>> nano470["u"]
| '0.470u'
| 
| 2.
| >>> c104 = EngineerNumber("10p") * 10 ** 4
| >>> c104 = EngineerNumber("10p", 4) # equal to above line
| >>> c104
| EngineerNumber("0.100u")
| >>> c104["u"]
| '0.100u'
| >>> c104["n"]
| '100.000n'
| 
| 3.
| >>> G1 = EngineerNumber("1G")
| >>> M103 = EngineerNumber("103M")
| >>> G1 / M103
| '9.709'
| 
| 4.
| >>> Vcc = 5
| >>> k47 = EngineerNumber("47k")
| >>> Ibeo = Vcc / k47
| >>> Ibeo
| EngineerNumber("106.383u")
| >>> Ibeo["m"]
| '0.106m'
| >>> Iceo = Ibeo * 140
| >>> Iceo["m"]
| '14.894m'
| >>> Io = Ibeo + Iceo
| >>> Io
| EngineerNumber("15.000m")
| >>> Io[""]
| '0.015'
| 
| 5.
| >>> kx = EngineerNumber("47", 2)
| >>> kx
| EngineerNumber("4.700k")
| >>> kx[""]
| '4700.000'
| 
| 6.
| >>> ENM("1%")
| EngineerNumber("10.000m")
| >>> ENM("1")["%"]
| '100.000%'
| >>> ENM("1%")[""]
| '0.010'
| >>> (ENM("17m") / ENM("30m"))["%"]
| '56.667%'
''',
     )
