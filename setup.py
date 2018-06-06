from setuptools import setup

setup(
    name='py-sds011',
    description='Python interface to the SDS011 air quality sensor.',
    author='Ivan Kalchev',
    version='0.9',
    url='https://github.com/ikalchev/py-sds011',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Operating System :: Linux',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
    ],
    license='Apache-2.0',
    packages=[
        'sds011',
    ],
    install_requires=[
        'pyserial',
    ],
)
