from setuptools import setup

setup(
    name='Piggy Server',
    version='1.0',
    long_description=__doc__,
    packages=['pigserver'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask']
)