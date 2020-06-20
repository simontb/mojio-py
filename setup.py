import setuptools

setuptools.setup(
    name="mojio-py",
    version="0.0.1",
    author="Simon Tenbeitel",
    # author_email="author@example.com",
    description="Moj.io API Python SDK",
    # url="https://github.com/pypa/sampleproject",
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
