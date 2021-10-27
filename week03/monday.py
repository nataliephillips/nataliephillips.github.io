

def largest(xs):
    '''
    Return the largest element in the input list.
    If the list has less no elements, return None.
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
    #if you want to go to index the back of the list, use negative numbers, it starts from the left and goes right
    #if you want to go right to left: start from -1 and get increasingly negative
    max = 0
    for x in xs:
        if x < x+1:
            max = x+1
        else:
            max = x
    return max
        

def filter_odd(xs):
    '''
    Return a list with all the odd elements removed.
    HINT:
    Use the accumulator pattern with a for loop.
    >>> filter_even([1,3,5])
    []
    >>> filter_even([2,4,6])
    [2, 4, 6]
    >>> filter_even([4,5,6,7])
    [4, 6]
    >>> filter_even([20,13,4,16,8,19,10])
    [20, 4, 16, 8, 10]
    '''