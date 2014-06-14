from setuptools import setup, find_packages


setup(
    name='geodis',
    version='0.1',
    description='Geodis - a Redis based geo resolving library',
    packages=['geodis'],
    package_dir={'geodis': 'src'},
    install_requires=[
        'redis',
        'geohasher==0.1dev',
    ],
)
