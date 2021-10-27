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
    '''
    text = text.replace('b', '')
    text = text.replace('/b', '')
    text = text.replace('<i>', '')
    text = text.replace('</i>', '')
    
    #.repale is good if there's an exact string that you want to replace, 
    # but we have a atter to replac, so .replace is too repeptitve and inefficient
    new_text = ''
    #new variable will check if within the < > : is true if between < > ; it is false if outside it
    inside_tag = False
    for i in range (len(text)):
        #do something
        if text[i] == '<':
            inside_tag = True
        elif text[i] == '>':
            inside_tag = False
        elif inside_tag == False: #can do it like so ORRRR if inside_tag == False and text[i] != '>'
            new_text += text[i]
    return new_text
    '''
    lessthans = text.split('<')
    new_text = ''
    for lessthan in lessthans:
        greaterthans = lessthan.split('>')
        #for greaterthan in greaterthans:
            #print ("greaterthan =", greaterthans)
        #print ("lensthan=", lessthan)
        new_text += greaterthans[-1]
    return new_text
    

