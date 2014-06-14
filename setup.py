from setuptools import setup, find_packages


setup(
    name='geodis',
    version='0.1',
    description='Geodis - a Redis based geo resolving library',
    packages=['geodis'],
    package_dir={'geodis': 'src'},
    scripts=['scripts/geodis.py'],
    install_requires=[
        'redis',
        'geohasher==0.1dev',
    ],
)
