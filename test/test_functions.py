import pytest
from package import functions
import json

### Preparation

# Load test_functions_parameters.json containing the scenarios for the tests
with open("test_functions_parameters.json", 'r') as f:
    dictionary_json = json.load(f)

# Function returning the arguments and the values for each scenario given a certain function to test (arg = key)
def get_from_json(dictionary,key):
    parameters = dictionary[key]
    return parameters["arguments"],parameters["values"]

### Tests

# Test of the test_concatenate function
function = "test_concatenate"
arguments, values = get_from_json(dictionary_json,function)
@pytest.mark.parametrize(arguments, values)
def test_concatenate(x,y,element,result):
    assert functions.concatenate(x,y,element) == result

# Test of the test_insertion function
function = "test_insertion"
arguments, values = get_from_json(dictionary_json,function)
@pytest.mark.parametrize(arguments, values)
def test_insertion(string, element, result):
    assert functions.insertion(string, element) == result
