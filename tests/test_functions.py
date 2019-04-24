import pytest
from package import functions
import json
import pandas as pd
import pandas.util.testing as tm

### Preparation

# Load test_functions_parameters.json containing the scenarios for the tests
with open("./tests/json/test_functions_parameters.json", 'r') as f:
    dictionary_json = json.load(f)

# Function returning the arguments and the values for each scenario given a certain function to test (arg = key)
def get_from_json(dictionary,key):
    parameters = dictionary[key]
    return parameters["arguments"],parameters["values"]

def get_from_csv(file):
    i = pd.read_csv("./tests/csv/input_" + file + ".csv")
    o = pd.read_csv("./tests/csv/output_" + file + ".csv")
    return i, o

### Tests

# Test of the test_concatenate function
function = "concatenate"
arguments, values = get_from_json(dictionary_json,function)
@pytest.mark.parametrize(arguments, values)
def test_concatenate(x,y,element,result):
    assert functions.concatenate(x,y,element) == result

# Test of the test_insertion function
function = "insertion"
arguments, values = get_from_json(dictionary_json,function)
@pytest.mark.parametrize(arguments, values)
def test_insertion(string, element, result):
    assert functions.insertion(string, element) == result

# Test of the df_multiplication function
function = "df_multiplication"
arguments, values = get_from_json(dictionary_json,function)
@pytest.mark.parametrize(arguments, values)
def test_df_multiplication(df,x,y,df_result,x_result,y_result):
    df, df_result = get_from_csv(function)
    df_output, x_output, y_output = functions.df_multiplication(df,x,y)
    assert x_result == x_output
    assert y_result == y_output
    tm.assert_frame_equal(df_output, df_result)
