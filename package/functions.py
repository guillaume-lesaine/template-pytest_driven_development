def function_simple_objects(x,y,element):
    if x[-1] == " " and y == " ":
        return x
    if y == " ":
        return x + y
    elif x[-1] == " ":
        return x + y
    else :
        return x + element + y

def function_dataframe(df):
    df["column_2"] = 2*df["column_2"]
    return df

def function_list(l):
    l_map = list(map(lambda x: x**2,l))
    return l_map

def function_complex(df,l,x,s):
    for column in l :
        df[column] = df[s] * x
    arg_1 = df.iloc[0,0]
    return df, arg_1
