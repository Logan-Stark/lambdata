"""
lambdata - a Collection of Data Science Functions
"""


import setuptools

REQUIRED = [
    "numpy",
    "pandas"

]

with open("README.md", "r") as file:
    LONG_DESCRIPTION =  file.read()

setuptools.setup(
    name = "lambdata_logstar",
    version = "0.0.2",
    author = "logan_stark",
    description = 'a Collection of Data Science Functions',
    long_description = LONG_DESCRIPTION,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/Logan-Stark/lambdata',
    packages = setuptools.find_packages(),
    python_requires = '>=3.6',
    install_requires = REQUIRED,
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

)