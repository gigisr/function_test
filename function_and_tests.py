# Setup
from datetime import datetime
import pandas as pd


# Define function & alternative
## No error checking on the inputs as the problem stipulates very specific 
## inputs with no room for deviation
def func_slow(list_vals):
    """
    This function works well if there are very few individual values
    """
    list_solutions = [x for x in set(list_vals) if list_vals.count(x) % 2 == 1]
    return list_solutions[0]


def func_fast(list_vals):
    """
    This works well regardless of the individual values count
    """
    s = pd.Series(list_vals).value_counts()
    s = s.loc[s % 2 == 1].index.tolist()
    return s[0]


# Tests
print('Slow implementation')

list_vals = [11, 11, 22, 22, 22, 33, 33]
print(
    'The list vals is {} long, and the first 6 values are {} and there are {} '
    'unique values present'.format(
        len(list_vals), list_vals[:6], len(set(list_vals)))
)
print('The value we want is ', end = '')
start = datetime.now()
print(func_slow(list_vals))
print('The funnction took {}'.format(datetime.now() - start))

list_vals = (
    [1 for _ in range(0, 1000)] + 
    [2 for _ in range(0, 67)] + 
    [3 for _ in range(0, 6000)]
)
print(
    'The list vals is {} long, and the first 6 values are {} and there are {} '
    'unique values present'.format(
        len(list_vals), list_vals[:6], len(set(list_vals)))
)
print('The value we want is ', end = '')
start = datetime.now()
print(func_slow(list_vals))
print('The funnction took {}'.format(datetime.now() - start))

list_vals = [
    [
        i for i in range(0, 50)
    ] for _ in range(0, 5000)
]
list_vals = [item for sublist in list_vals for item in sublist]
list_vals += [31]
print(
    'The list vals is {} long, and the first 6 values are {} and there are {} '
    'unique values present'.format(
        len(list_vals), list_vals[:6], len(set(list_vals)))
)
print('The value we want is ', end = '')
start = datetime.now()
print(func_slow(list_vals))
print('The funnction took {}'.format(datetime.now() - start))

print('The next test takes a little longer...')
list_vals = [
    [
        i for i in range(0, 900)
    ] for _ in range(0, 5000)
]
list_vals = [item for sublist in list_vals for item in sublist]
list_vals += [55]
print(
    'The list vals is {} long, and the first 6 values are {} and there are {} '
    'unique values present'.format(
        len(list_vals), list_vals[:6], len(set(list_vals)))
)
print('The value we want is ', end = '')
start = datetime.now()
print(func_slow(list_vals))
print('The funnction took {}'.format(datetime.now() - start))

print()
print('Fast implementation')

list_vals = [11, 11, 22, 22, 22, 33, 33]
print(
    'The list vals is {} long, and the first 6 values are {} and there are {} '
    'unique values present'.format(
        len(list_vals), list_vals[:6], len(set(list_vals)))
)
print('The value we want is ', end = '')
start = datetime.now()
print(func_fast(list_vals))
print('The funnction took {}'.format(datetime.now() - start))

list_vals = (
    [1 for _ in range(0, 1000)] + 
    [2 for _ in range(0, 67)] + 
    [3 for _ in range(0, 6000)]
)
print(
    'The list vals is {} long, and the first 6 values are {} and there are {} '
    'unique values present'.format(
        len(list_vals), list_vals[:6], len(set(list_vals)))
)
print('The value we want is ', end = '')
start = datetime.now()
print(func_fast(list_vals))
print('The funnction took {}'.format(datetime.now() - start))

list_vals = [
    [
        i for i in range(0, 50)
    ] for _ in range(0, 5000)
]
list_vals = [item for sublist in list_vals for item in sublist]
list_vals += [31]
print(
    'The list vals is {} long, and the first 6 values are {} and there are {} '
    'unique values present'.format(
        len(list_vals), list_vals[:6], len(set(list_vals)))
)
print('The value we want is ', end = '')
start = datetime.now()
print(func_fast(list_vals))
print('The funnction took {}'.format(datetime.now() - start))

list_vals = [
    [
        i for i in range(0, 900)
    ] for _ in range(0, 5000)
]
list_vals = [item for sublist in list_vals for item in sublist]
list_vals += [55]
print(
    'The list vals is {} long, and the first 6 values are {} and there are {} '
    'unique values present'.format(
        len(list_vals), list_vals[:6], len(set(list_vals)))
)
print('The value we want is ', end = '')
start = datetime.now()
print(func_fast(list_vals))
print('The funnction took {}'.format(datetime.now() - start))
