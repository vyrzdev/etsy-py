import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    readme = fh.read()

setuptools.setup(
    name="etsy-py-dev",
    version="0.0.2",
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