import setuptools

setuptools.setup(
    name="mojio-py",
    version="0.0.2",
    author="Simon Tenbeitel",
    author_email="open-source@simontb.de",
    description="Moj.io API Python SDK",
    url="https://github.com/simontb/mojio-py",
    packages=['mojio-py'],
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
