from setuptools import setup, find_packages




# MAKE CHANGES HERE
AUTHOR_USER_NAME = "prtk1729"
SRC_REPO = "Repo Analyser"
AUTHOR_EMAIL = "prateek.pani4243@gmail.com"
__version__ = "0.0.0" # required to make changes (add features etc)



setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    packages = find_packages(where="src")
)

