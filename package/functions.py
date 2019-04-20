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
