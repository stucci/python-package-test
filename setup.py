import setuptools

setuptools.setup(
    name="corona",
    version="0.0.1",
    install_requires=[
        "requests",
    ],
    entry_points={
        'console_scripts': [
            'corona=corona:main',
        ],
    },
    description="A covoid-19 tracker",
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
