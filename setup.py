from setuptools import setup, find_packages,Extension


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='flask-validate-json',
    version='0.0.1',
    description='This is a Flask Plugin to be used for Validate JSON request data.',
    long_description=readme(),
    url='https://github.com/machine-w/flask-validate-json',
    author='machine-w',
    author_email='steve2008.ma@gmail.com',
    license='MIT',
    classifiers=[
        'Framework :: Flask',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    keywords=['flask', 'json', 'validation', 'schema', 'jsonschema'],
    packages=find_packages(exclude=['tests.*', 'tests']),
    install_requires=[
        'flask>=0.12.2',
        'jsonschema>=2.6.0'
    ],
    test_suite='tests.test_suite'
)
