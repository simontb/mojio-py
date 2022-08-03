import setuptools

setuptools.setup(
    name="mojio_sdk",
    version="0.5.0",
    author="Simon Tenbeitel",
    author_email="open-source@simontb.de",
    description="Moj.io API Python SDK",
    long_description="Moj.io API Python SDK",
    url="https://github.com/simontb/mojio-py",
    packages=['mojio_sdk'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests'
    ],
    python_requires='>=3.6',
)
