from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["aiogram==3.0.0b6"]

setup(
    name="aiocalendar",
    version="0.0.1",
    author="Anton Tarasov",
    author_email="huseeads@gmail.com",
    description="Easy calendar for aiogram v3",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/aiocalendar/homepage/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
    ],
)
