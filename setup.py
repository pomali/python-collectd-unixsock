import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="collectd-unixsock",
    version="0.0.1",
    author="pom",
    author_email="author@example.com",
    description="CollectD unixsock client",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pomali/python-collectd-unixsock",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
    ],
    #python_requires='>=3.6',
)
