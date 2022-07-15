"""
    Cohesity REST API

    Cohesity API provides a RESTful interface to access the various data management operations on Cohesity cluster and Helios.  # noqa: E501

"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "cohesity-sdk"
VERSION = "1.0.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
]

# Try to convert markdown README to rst format for PyPI.
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
    long_description_content_type='text/x-rst'
except(IOError, ImportError):
    long_description = open('README.md').read()
    long_description_content_type='text/markdown'

setup(
    name=NAME,
    description='This SDK provides operations for interfacing with the Cohesity Cluster.',
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    author='Cohesity Inc.',
    author_email='cohesity-api-sdks@cohesity.com',
    url='https://github.com/cohesity/cohesity_sdk',
    version=VERSION,
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
)

