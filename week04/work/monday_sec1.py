def delete_HTML(text):
    '''
    This function removes all HTML tags from the input text.
    >>> delete_HTML('This is <b>bold</b>!')
    'This is bold!'
    >>> delete_HTML('This is <i>italic</i>!')
    'This is italic!'
    >>> delete_HTML('This is <strong>italic</strong> and this is <ins>strikethrough</ins>!')
    'This is italic and this is strikethrough!'
    '''
    #accumulator
    new = ''
    for i in range (len(text)):
        #do something with text at i
        new += text[i]
    return new
     
"""
recognize the accumulator pattern idea to work with the assignment
function wants us to remove something from a string, so just create a new string and add on the string with the value parts of it
input is text and output should start at an empty string
just when we had a list, when you have a text [0], it will give you the first character of the string
list(text) = converts the string of the text into a list, each character would be in one index return 
"""