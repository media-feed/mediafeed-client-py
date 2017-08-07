from setuptools import find_packages, setup


version = __import__('mediafeed_cli').__version__
with open('README.rst', 'rb') as f:
    long_description = f.read().decode('utf-8')


setup(
    name='MediaFeed-CLI',
    version=version,
    packages=find_packages(),

    install_requires=[
        'requests',
        'tabulate',
    ],

    author='Eduardo Klosowski',
    author_email='eduardo_klosowski@yahoo.com',

    description='Download de arquivos de fonte de mídias',
    long_description=long_description,
    license='MIT',
    url='https://github.com/eduardoklosowski/mediafeed-cli',

    entry_points={
        'console_scripts': [
            'mediafeed = mediafeed_cli:main',
        ],
    },
)
