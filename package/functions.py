from functools import reduce

def concatenate(x,y,element):
    if x[-1] == " " and y == " ":
        return x
    if y == " ":
        return x + y
    elif x[-1] == " ":
        return x + y
    else :
        return x + element + y

def insertion(string,element):
    string_s = string.strip()
    return reduce(lambda x,y : concatenate(x,y,element), list(string_s))

def df_multiplication(df,x,y):
    df["column_2"] = 2*df["column_2"]
    x = 2*x
    y = 2*y
    return df, x, y
