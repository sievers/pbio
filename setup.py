import setuptools

with open("README.md","r",encoding="utf-8") as fh:
    long_description=fh.read()

setuptools.setup(
    name="pbio",
    version="0.0.1",
    author="Jonathan Sievers",
    autho_email="jonathan.sievers@mcgill.ca",
    description="I/O routines for streaming data from radio telescopes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
