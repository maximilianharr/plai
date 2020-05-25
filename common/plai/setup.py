import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plai",
    version="0.0.1",
    author="Maximilian Harr",
    author_email="maximilian.harr@gmail.com",
    description="PLAI: Playground Library for Artificial Intelligence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maximilianharr/plai",
    packages=['visualization', 'workspace', 'interfaces', 'yolo'],
    package_dir={'': 'plai'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: BSD 3-Clause License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
