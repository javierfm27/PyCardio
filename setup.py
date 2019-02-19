import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()

# with open("requirements.txt","r") as fr:
#     requirements = fr.read().splitlines()

setuptools.setup(
    name="PyCardioTest",
    version="0.0.6",
    author="Oscar Barquero",
    author_email="oscar.barquero@urjc.es",
    install_requires= [
        'numpy',
        'scipy',
        'matplotlib'
    ],
    description="Package for heart analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/javierfm27/PyCardio",
    packages=setuptools.find_packages(),
    classifiers= [
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
    ]
)
