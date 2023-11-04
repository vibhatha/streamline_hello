from setuptools import find_packages, setup

setup(
    name="gymcana",
    version="0.1",
    packages=find_packages(),
    description="A simple app for Gym lovers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Vibhatha Lakmal Abeykoon",
    author_email="vibhatha@gmail.com",
    install_requires=[
        "numpy",
        "requests",
        "pandas",
        "pyarrow",
        "mysql-connector-python",
        "pytest",
        "streamlit",
    ],
    extras_require={
        "dev": [
            "black",  # Code formatter
            "flake8",  # Code style checker
            "isort",  # Import sorter
            "pre-commit",  # pre commit checks
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
