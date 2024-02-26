import setuptools

def readme():
    try:
        with open("README.md") as f:
            return f.read()
    except IOError:
        return ""


setuptools.setup(
    name="psgreddit",
    version="5.0.0",
    author="PySimpleSoft Inc.",
    description="A GUI app made with PySimpleGUI used to search through Reddit and Subreddits using praw module",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="GUI UI PySimpleGUI tkinter psgreddit reddit",
    url="https://github.com/PySimpleGUI/psgreddit",
    packages=["psgreddit"],
    license="Free To Use But Restricted",
    install_requires=["praw","PySimpleGUI>=5"],
    python_requires=">=3.6",
    classifiers=(
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: Free To Use But Restricted",
        "Operating System :: OS Independent",
        "Framework :: PySimpleGUI",
        "Framework :: PySimpleGUI :: 5",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Software Development :: User Interfaces",
    ),
    package_data={"":
                      ["*","*.*"]
                  },
    entry_points={"gui_scripts": [
        "psgreddit=psgreddit.psgreddit:main"
    ], },
)
