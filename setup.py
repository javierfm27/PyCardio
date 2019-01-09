import setuptools

with open("README.md","r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="PyCardio",
    version="0.0.1",
    author="Oscar Barquero",
    author_email="oscar.barquero@urjc.es",
    install_requires=["numpy","matplotlib","scipy"],
    description="Package for heart analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/javierfm27/PyCardio",
    packages=setuptools.find_packages(),
    classifiers= [
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Indepedent",
        "Topic :: Scientific/Engineering :: Medical Science Apps",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ""
    ]
)
