'''
As a reminder, we've now seen 4 ways to run python:
    1. pythontutor.com
    2. $ python3 filename.py            # the "triangle button"
    3. $ python3 -m doctest filename.py # runs the doctests
    4. $ python3                        # runs "interactive python"
In order for python to be able to find your files,
you need to have the right folder open.
For some people, this means pressing the "pages button" in the left of vscode and then pressing "open folder".
For other people, this means running a command like
    $ cd foldername
in the terminal to "change directory" into the folder that contains your python files.
Today, we will see a 5th way to run python:
    5. $ python3 -i filename.py
The -i stands for interactive, and this is a special way to run interactive python that also loads the file and gives you access to all its internal functions and variables.
'''

'''
xs = [4, 9, 9, 3, 5, 2]
xs [2] = 9 <- this is called positive indexing and calls the number at the index
xs [-1] = 2 <- this is negative indexing, neg index starts at -1 and starts the index from the right most place in the list
xs [1:4] = [9, 9, 3] <- starts at position one, and goes up to but does not include position 4
    COLON INDICATES A SLICE OR SUBLIST
xs [1:4] = [9, 9, 3] <- starts at position one, and goes up to but does not include position 4
xs [:4] = [4, 9, 9, 3] <- assume start at position zero, and goes up to but does not include position 4
xs[:] = [4, 9, 9, 3, 5, 2] <- gives the whole list
xs [2:] = [9, 9, 3, 5, 2] <-  start at position index 2, and goes up until the very end
xs [1:5:2] = [9, 9, 3] <- starts at position one, and goes up to but does not include position 5, steps up two at a time
    THIRD COLON INDICATES STEP
LIST OF LISTS
xss = [[1,2,3], [3,4,5], [6,7,8]]
xss [0] = [1,2,3]
xss [0][2] = 3

VERBOSE: will tell you what is wokring, and what is NOT working
    if you dont have verbose then it wont come out with any code if it is correct
SORTING IN LISTS: 
xs = [4, 7, 1, 3, 9, 5, 6]
xs.sort()
    is a COMMAND
THIS WILL BE THE MODIFIED LIST :
    xs = [1, 3, 4, 5, 6, 7, 9]
modifies the list and puts it in sorted order from least to greatest

LEN () 
len() does not modify the list, it tells us about parameter of the list
    not a command
LENGTH does NOT have the special 0 value
'''


import math

################################################################################
# lists
################################################################################

def largest(xs):
    '''
    Return the largest element in the input list.
    If the list has no elements, return None.
    HINT:
    There are three ways to solve this problem:
    1. use a for loop + if statement
    2. sort the list and use list subscripting
    3. use a built-in function
    >>> largest([1,2,3])
    3
    >>> largest([99,-56,80,100,90])
    100
    >>> largest(list(range(0,100)))
    99
    >>> largest([10])
    10
    >>> largest([])
    '''
    if len(xs) == 0:
        return None
    xs.sort()
    return xs[len(xs)-1]
    '''
    if len(xs) == 0:
        return None
    max = 0
    for x in xs:
        if x> max:
            max = x
    return max
    '''
    '''
    ORRRR YOU CAN YOU THE RETURN MAX (xs)
    if len(xs) == 0:
        return None
    return max(xs)
    '''

def largest_index(xs):
    '''
    Return the index of the largest element in the input list.
    If the list has no elements, return None.
    HINT:
    The sorting/built-in function approach will not work on this function.
    >>> largest_index([1,2,3])
    2
    >>> largest_index([99,-56,80,100,90])
    3
    >>> largest_index(list(range(0,100)))
    99
    >>> largest_index([10])
    0
    >>> largest_index([])
    '''
    if len(xs) == 0:
        return None
    max = 0 #start at negative infinity, so if the list is full of negative numbers, it will still find the max
    #for x in xs:
    for i in range(len(xs)): #this loops over indexes not the values, the range function goes up to, but doesn't include the len(xs)
        if xs[i] > xs[max]:
            max = i
    return max
    '''
    if len(xs) == 0:
        return None
    return len(xs)-1
    '''


def filter_odd(xs):
    '''
    Return a list with all the odd elements removed.
    HINT:
    Use the accumulator pattern with a for loop.
    >>> filter_odd([1,3,5])
    []
    >>> filter_odd([2,4,6])
    [2, 4, 6]
    >>> filter_odd([4,5,6,7])
    [4, 6]
    >>> filter_odd([20,13,4,16,8,19,10])
    [20, 4, 16, 8, 10]
    '''
    accumulator = []
    for x in xs:
        if x%2==0:
            accumulator.append(x)
    return accumulator
    '''
    for x in xs:
        if x%2!=0:
            xs.remove(x)
    return xs
    '''



################################################################################
# dictionaries
    # uses curly braces, and uses colons and commas
    # left of the colon is the key and to the right of colon is the value
    # each line is a key, value pair and these pairs are separated by commas
    # each (key,value) pair is like an item in a list
    # dictionary uses the whatever the key is to keep track of the value
        #  math_grades['donald knuth'] = 85
    # len(math_grades) = 8
        # will give the amount of people in the dictionary
    # if you put in a key that doesnt exist, there is a key error, so it would mean, the name is not in the dictionary, out of range type of error
    #
    #
    #

################################################################################

# These dictionaries store the grades of famous people in their math, english, and economics classes.
# You shouldn't modify these dictionaries,
# they are used in the doctests for the functions below.
math_grades={
        'donald knuth':85,
        'hypatia':75,
        'emmy noether':86,
        'leonhard euler':92,
        'grigori perelman':95,
        'alexander grothendieck':95,
        'shelton cooper':72,
        'ada lovelace':96,
        }

english_grades={
        'emily dickenson':92,
        'edgar allan poe':88,
        'william shakespeare':84,
        'robert frost':83,
        'dorthy day':95,
        'douglas adams':42,
        'maya angelou':89,
        'emma goldman':85,
        }

economics_grades={
        'christine lagarde':85,
        'alan greenspan':92,
        'adam smith':88,
        'kristalina georgieva':79,
        'karl marx':90,
        'pierre-joseph proudhon':95,
        }

def lowest_grade(d):
    '''
    Return the largest value.
    >>> lowest_grade(math_grades)
    72
    >>> lowest_grade(english_grades)
    42
    >>> lowest_grade(economics_grades)
    79
    '''
    lowest = math.inf
    # looping over a list gets the values of the list
    # looping over a dictionary, you get the keys in the list
    for key in d: 
        grade = d [key]
        if grade < lowest:
            lowest = grade
    return lowest


def student_with_lowest_grade(d):
    '''
    Return the key that has the greatest value.
    >>> student_with_lowest_grade(math_grades)
    'shelton cooper'
    >>> student_with_lowest_grade(english_grades)
    'douglas adams'
    >>> student_with_lowest_grade(economics_grades)
    'kristalina georgieva'
    '''
    lowest = math.inf
    for key in d: 
        grade = d [key]
        if grade < lowest:
            lowest = grade
            studentname = key
    return studentname
