import pytest
import json
import pandas as pd
import pandas.util.testing as tm

from conftest import package
from conftest import load_json, load_csv

####### Preparation

# Load test_functions_parameters.json containing the scenarios for the tests
dictionary_json = load_json("test_functions_parameters.json")


####### Tests


### Simple Objects

arguments, values = dictionary_json["function_simple_objects"].values()
@pytest.mark.parametrize(arguments, values)
def test_function_simple_objects(x, y, element, result):
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

    output = package.function_simple_objects(x,y,element)

    assert output == result


### Lists

arguments, values = dictionary_json["function_list"].values()
@pytest.mark.parametrize(arguments, values)
def test_function_list(filename, case):
    '''
        Test function of function_list. This test shows an example of how to
        handle a function taking a list as input and outputs.

        To customize it :
            1 - Relate it to the right function by replacing the names
            2 - Give the right elements as input and parameters in "test_functions_parameters".
            3 - Add the right json file in the /json folder to generate your list inputs and outputs.
    '''

    l, l_result = load_json(filename, case)
    l_output = package.function_list(l)

    assert l_output == l_result


### Pandas Dataframes

arguments, values = dictionary_json["function_dataframe"].values()
@pytest.mark.parametrize(arguments, values)
def test_function_dataframe(df_filename, df_result_filename):
    '''
        Test function of function_dataframe. This test shows an
        example of how to handle a function taking a pandas dataframe as input
        and output.

        To customize it :
            1 - Relate it to the right function by replacing the names
            2 - Give the right elements as input and parameters in "test_functions_parameters".
            3 - Add the right csv files in the /csv folder to generate your dataframe inputs and outputs.
    '''

    df, df_result = load_csv(df_filename), load_csv(df_filename)
    df_output = package.function_dataframe(df)

    tm.assert_frame_equal(df_output, df_result)


### Global Example (Simple Objects + Lists + Dataframes)

arguments, values = dictionary_json["function_complex"].values()
@pytest.mark.parametrize(arguments, values)
def test_function_complex(df_filename, l_filename, case, x, s, df_result_filename, arg_1_result):
    '''
        Test function of function_complex. This test shows an
        example of how to handle a complex combination of inputs and outpus.
        This test is a simple combination of the three test presented above.

        To customize it :
            1 - Relate it to the right function by replacing the names
            2 - Give the right elements as input and parameters in "test_functions_parameters".
            3 - Add the right csv files in the /csv folder to generate your dataframe inputs and outputs.
            4 - Add the right json files in the /json folder to generate your list inputs and outputs.
    '''

    df, df_result = load_csv(df_filename), load_csv(df_result_filename)
    l = load_json(l_filename, case)

    df_output, arg_1_output = package.function_complex(df, l, x, s)

    tm.assert_frame_equal(df_output, df_result)
    assert arg_1_output == arg_1_result
