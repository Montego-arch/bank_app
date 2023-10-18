from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in bank_app/__init__.py
from bank_app import __version__ as version

setup(
	name="bank_app",
	version=version,
	description="It is a bank app",
	author="Montego-arch",
	author_email="okekeemmanuelomolola@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
