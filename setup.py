from setuptools import setup, find_packages
import sys

__version__ = "0.1.0"

# setup(
#     name="prophecy-libs",
#     version=__version__,
#     url="https://github.com/SimpleDataLabsInc/prophecy-python-libs",
#     packages=find_packages(exclude=["test.*", "test"]),
#     description="Helper library for prophecy generated code",
#     long_description=open("README.md").read(),
#     install_requires=[],
#     keywords=["python", "prophecy"],
#     classifiers=[],
#     zip_safe=False,
#     license="GPL-3.0",
# )
try:
    from semantic_release import setup_hook
    setup_hook(sys.argv)
except ImportError:
    pass