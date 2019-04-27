import pytest
from package import functions
import json
import pandas as pd
import pandas.util.testing as tm
import inspect


####### Preparation

# Define fixtures

@pytest.fixture
def load_json(request):
    with open("./tests/json/" + request.param + ".json", 'r') as f:
        dict_json = json.load(f)
    return dict_json


# Load test_functions_parameters.json containing the scenarios for the tests

with open("./tests/json/test_functions_parameters.json", 'r') as f:
    dictionary_json = json.load(f)

# Define some useful functions

def get_dataframe_from_csv(file):
    i = pd.read_csv("./tests/csv/input_" + file + ".csv")
    o = pd.read_csv("./tests/csv/output_" + file + ".csv")
    return i, o


####### Tests


### Simple Objects

arguments, values = dictionary_json["function_simple_objects"].values()
@pytest.mark.parametrize(arguments, values)
def test_function_simple_objects(x,y,element,result):

    '''
        Test function of function_simple_objects. This test is able
        to handle any function taking any number of the following
        simple objects as inputs and outputs :
            - integers
            - strings
            - floats
            - booleans

        To do :
            1 - Relate it to the right function by replacing the names
            2 - Give the right elements as input and parameters in "test_functions_parameters".
    '''

    function = inspect.getframeinfo(inspect.currentframe()).function.replace("test_","") # Get the name of the current function
    method = getattr(functions, function)

    output = method(x,y,element)

    assert output == result


### Lists

arguments, values = dictionary_json["function_list"].values()
@pytest.mark.parametrize(arguments, values, indirect=["load_json"])
def test_function_list(load_json, case):

    '''
        Test function of function_list. This test shows an example of how to
        handle a function taking a list as input and outputs.

        To customize it :
            1 - Relate it to the right function by replacing the names
            2 - Give the right elements as input and parameters in "test_functions_parameters".
            3 - Add the right json file in the /json folder to generate your list inputs and outputs.
    '''

    function = inspect.getframeinfo(inspect.currentframe()).function.replace("test_","") # Get the name of the current function
    method = getattr(functions, function)

    l, l_result = tuple(load_json[case].values())
    l_output = method(l)

    assert l_output == l_result


### Pandas Dataframes

arguments, values = dictionary_json["function_dataframe"].values()
@pytest.mark.parametrize(arguments, values)
def test_function_dataframe(df,df_result):

    '''
        Test function of function_dataframe. This test shows an
        example of how to handle a function taking a pandas dataframe as input
        and output.

        To customize it :
            1 - Relate it to the right function by replacing the names
            2 - Give the right elements as input and parameters in "test_functions_parameters".
            3 - Add the right csv files in the /csv folder to generate your dataframe inputs and outputs.
    '''

    function = inspect.getframeinfo(inspect.currentframe()).function.replace("test_","") # Get the name of the current function
    method = getattr(functions, function)

    df, df_result = get_dataframe_from_csv(function)
    df_output = method(df)

    tm.assert_frame_equal(df_output, df_result)


### Global Example (Simple Objects + Lists + Dataframes)

arguments, values = dictionary_json["function_complex"].values()
@pytest.mark.parametrize(arguments, values, indirect=["load_json"])
def test_function_complex(df, load_json, case, x, s, df_result, arg_1_result):

    '''
        Test function of function_complex. This test shows an
        example of how to handle a complex combination of inputs and outpus.
        This test is a simple combination of the three test presented above.

        To customize it :
            1 - Relate it to the right function by replacing the names
            2 - Give the right elements as input and parameters in "test_functions_parameters".
            3 - Add the right csv files in the /csv folder to generate your dataframe inputs and outputs.
            3 - Add the right json files in the /json folder to generate your list inputs and outputs.
    '''

    function = inspect.getframeinfo(inspect.currentframe()).function.replace("test_","") # Get the name of the current function
    method = getattr(functions, function)

    df, df_result = get_dataframe_from_csv(function)
    l = list(load_json[case].values())[0]

    df_output, arg_1_output = method(df, l, x, s)

    tm.assert_frame_equal(df_output, df_result)
    assert arg_1_output == arg_1_result


# Create a case for arrays
