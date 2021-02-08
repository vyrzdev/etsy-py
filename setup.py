import setuptools
import json

with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()

with open("current_release.json", "r") as release_info_file:
    release_info: dict = json.loads(release_info_file.read())

setuptools.setup(
    name="etsy-py-dev",
    version=release_info.get("version_tag"),
    author="vyrzdev",
    author_email="ben@vyrz.dev",
    description="An auto-updating Etsy Wrapper",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/vyrzdev/etsy-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)