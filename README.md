# Test Driven Development Template Folder

The current project is designed to provide a simple folder structure template for writing code in Python and testing it using PyTest.

The folder provides the following elements :
- main.py : file at the root of the directory
- functions.py : file in the package directory to write functions to use in the main or to be tested
- test_functions.py : file to test the functions available in the functions.py file
- test_functions.json : file to store scenarios to test. The JSON file is then imported in test_functions.py the @pytest.mark.parametrize decorator is ultimately used to pass the scenarios the each test function.

We provide a simple testing example based on the insertion of characters in a string.

## Requirements

```console
pip3 install pytest
pip3 install json
```

## Usage

Run the following command in the test folder to see the results of the tests.

```console
py.test -v
```

In order to have the results of the test saved in a log file, run the following command.

```console
py.test -v > tests.log
```
