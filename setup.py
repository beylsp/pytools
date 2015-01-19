try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

package_name = 'pytools'
description = 'a collection of various useful python scripts.'
package = __import__(package_name)
requirements = []

setup(
    name = package_name,
    version = package.__version__,
    author = package.__author__,
    url = package.__url__,
    description = description,
    packages = ['pytools'],
    install_requires = requirements,
)
