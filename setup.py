"""hodor"""

from setuptools import setup

setup(
    name="hodor",
    version="2!0",
    description="hodor!",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[],
    author="Buck Evan",
    author_email="buck.2019@gmail.com",
    url="http://github.com/bukzor/hodor",
    license="hodor",
    py_modules=["hodor"],
    platforms=["hodor"],
    entry_points={
        "console_scripts": [
            "hodor = hodor:hodor",
        ],
    },
)
