# DevOps Exercise


### Test Badge
![sortLib Test](https://github.com/K-Hannan12/COS-397-Assignment-5/actions/workflows/main.yml/badge.svg?event=push)

This is a skeleton repository for your exercise. 
The goal of this exercise is to implement a Python package for sorting integer 
lists using the DevOps software development approach.

> **Warning**: If working on windows, some directories and files in this archive
will not be visible because they start with a '.'. In the file browser, change 
the View to display "Hidden items".

You will need to:
1. Add .pre-commit-config.yml which:  
    1. Limits maximal file size.
    1. Runs the black and flake8 linters.
    1. Detect presence of aws credentials private keys.    
1. Implement the algorithms for bubble, quick and insertion sort, see sort_lib directory,
code should be documented using standard Python practices (there are several [docstring 
styles](https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format)
select one and be consistent).
1. Implement testing using the [pytest](https://docs.pytest.org/en/6.2.x/) framework, see test directory.
1. Implement linting, style checking using both [flake8](https://flake8.pycqa.org/en/latest/) and 
[black](https://black.readthedocs.io/en/stable/). 
1. Modify the GitHub actions workflow so that it tests and builds the package for all 
three operating systems (OSX/Linux/Win) and for Python versions 3.9 and 3.10. Read more about [Distributing Python packages](https://docs.python.org/3/distributing/index.html).
1. Modify this file to describe this repository and the DevOps workflow you implemented (add badges to this file showing testing status).
1. **Optional**: Add a job to the workflow which uploads the wheel to [TestPyPI](https://test.pypi.org/). As every package on TestPyPI is required to have a unique name you need to update the UNIQUE_SUFFIX both in the directory name and in the .toml file. Possibly use your team number.
    >**Warning**: Do not upload to the authoritative Python Package Index (PyPI).  


Possible work division, three sub-teams:
1. Adding pre-commit and implementing algorithm code and documentation (tasks 1,2,6).
1. Implementing testing code, mastering pytest, black, flake8 (tasks 3,4,6).
1. Understanding pytest, black, flake8 and mastering GitHub workflows (tasks 5,6).

---------------------------------------------------------------------------------------------------------------------------------------

1. Project Overview

    This project implements a python pachake for sorting integer lists using popular sorting algorithms such as bubblesort, quicksort, and insertion sort. The goal is to apply DevOps practices, including continuous integration and continuous delivery, using tools like github Actions, pytest, flake8, and black.

2. Installation Instructions

    STEP ONE: Clone the GitHub repository
    git clone https://github.com/yourteam/repository-name.git

    STEP TWO: Install required dependencies
    pip install -r requirements.txt

    STEP THREE: Install the sorting package
    python steup.py install

Prerequisites:
python 3.9 or 3.10
package managers: pip
GitHub account to access the repository

3. Usage Guide

    After installation you may use the sorting algorithm as follows
    
    from sort_lib import bubble_sort, quick_sort, insertion_sort
    
    Example usage:
    numbers = [34, 7, 23, 32, 5, 62]
    sorted_numbers = bubble_sort(numbers)
    print(sorted_numbers)

4. Configuration

    Sorting Algorithm does not require any additional configuration

5. Contributing Guidelines (Who did what)

???

6. License

???
