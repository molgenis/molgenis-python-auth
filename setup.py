from setuptools import setup, find_packages

setup(
    name="molgenis_auth",
    version="0.1.0",
    description="OAuth Device Flow client for Molgenis authentication",
    author="Your Name",
    author_email="you@example.com",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "molgenis-auth = molgenis_auth.cli:main",
        ],
    },
)
