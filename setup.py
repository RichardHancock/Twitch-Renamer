import setuptools

__version__ = "0.0.0"  # Stops missing variable errors, next call assigns it
exec(compile(
    open("twitch_renamer/version.py").read(),
    "twitch_renamer/version.py",
    "exec"
))

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="twitch_renamer",
    version=__version__,
    author="Richard Hancock",
    author_email="me@richardhancock.co.uk",
    description="Twitch Renamer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.trixie.cloud/python-scripts/Twitch-Renamer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
