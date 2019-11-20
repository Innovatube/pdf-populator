import setuptools

import pdf_populator

with open("README.md", "r") as file:
    long_description = file.read()

with open('requirements.txt') as file:
    install_requires = file.read()

setuptools.setup(
    name=pdf_populator.__name__,
    version=pdf_populator.__version__,
    packages=setuptools.find_packages(),
    description="PDF Populator",
    long_description=long_description,
    install_requires=install_requires,
    python_requires='>=3.6',
    include_package_data=True,
    package_data={'pdf_populator': []},
)
