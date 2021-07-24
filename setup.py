from setuptools import find_packages, setup

setup(
    name='tossip',
    packages=find_packages(include=['tossip']),
    version='0.1.0',
    description='A library to easily communicate with iOS Devices.',
    author='LiquidDevelopment',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)