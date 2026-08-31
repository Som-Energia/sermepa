from setuptools import find_packages, setup


setup(
    name='sermepa',
    version='1.2.2',
    description='A client to submit payment orders to the Sermepa service.',
    author='Som Energia, Gisce SL',
    author_email='itcrowd@somenergia.coop, devel@gisce.net',
    url='https://somenergia.coop',
    license='GNU General Public License v3 or later (GPLv3+)',
    packages=find_packages(exclude=['sermepa.config', 'sermepa.config.*']),
    install_requires=[
        'pyDes',
        'requests',
    ],
    python_requires='>=2.7',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Topic :: Office/Business :: Financial',
        'Operating System :: OS Independent',
    ],
)
