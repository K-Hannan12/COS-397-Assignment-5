# DevOps Exercise


### Test Badge
![sortLib Test](https://github.com/K-Hannan12/COS-397-Assignment-5/actions/workflows/main.yml/badge.svg?event=push)

1. Project Overview

    This project implements a Python package for sorting integer lists using popular algorithms such as bubble sort, quicksort, and insertion sort. The goal is to apply DevOps practices, including continuous integration and continuous delivery, using tools like GitHub Actions, pytest, flake8, black, and the [pre-commit](https://pre-commit.com/) Python hook framework.

3. Installation Instructions

    STEP ONE: install/ Upgrade pip
       - python -m pip install --upgrade pip

    STEP TWO: Install python package
       - pip install -i https://test.pypi.org/simple/ basic-sort-UMaine-Fike

Prerequisites:
Python 3.9 or 3.10
package managers: pip
GitHub account to access the repository.

3. Usage Guide

    After installation, you may use the sorting algorithm as follows:
    
        from basic_sort_UMaine_Fike.int_sort import bubble, quick insertion
        
        Example usage:
        numbers = [34, 7, 23, 32, 5, 62]
        sorted_numbers = bubble_sort(numbers)
        print(sorted_numbers)

5. Configuration

    Sorting Algorithm does not require any additional configuration.

6. Contributing Guidelines (Who did what)

Johnny - Sorting Algorithms & Tests 

Odin - README Description 

Kaleb - YML & Linting Implementation 

Clark - Reading & Understanding 

Seth - Reading & Understanding

