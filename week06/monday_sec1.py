# print('hello')
# why is there a case with the file name and the long absolute path
# abosulate path = /Users/nataliephillips/Documents/GitHub/nataliephillips.github.io/week06/monday_sec1.py
    # aboulsute path is a path that works anywheere; it always references the smae file no matter where you are located
    # you know its an abosulate path because it starts with a slash
# relative path: doesnt start with a slash
    # references a file that is not absolute path
    # the computer always converts relative paths to absolute apths to access a file
    # system variable = working directory : is where you are located on the computer
# pwd = print working directory
    # directory is the smae thing as a folder
    # directory is an older term
    # if you call pwd it will show the conversion of the relative path to the absolute path
# cd = change working directory
    # changes where the file is being called upon
    # affects what would be returned if called pwd
# special folder called cd ..
    # "cd .." means you should go up a folder, become more broad
    # if you did cd.. then it would take you out of the week06 folder and solely into the github.io folder
# os
    # import os 
    # print(os.getcwd()) # returns the string which is you working directory, same result as pwd command
    # os stands for operating system
# PRINCIPLE 1
    # know your working directory
    #FileNotFoundError = something wrong with the path
# PRINCIPLE 2
    # know your file encoding
    # touches back to unicode
    # can specificy explictily with open ('', encoding = '')  is equal to the line below
        # with open ('blurb', encoding='utf8') as f: 
                # UTF8 is the default encoding for macs (different for windows)
        # if you dont specificy the encoding, there will be errors wehn operating with interoperating systems
        # if you use the with open command, must give which encoding you are working with
        # vs code by defualt saves things in utf8
    #can see what you are encoding with the lower right hand corner
    #UnicodeDecodeError when you save code with a different unicode you try and open things with
# PRINCIPLE 3
    # 
# OPENING MODE: second parameter to the open function
    # if you open something in b mode, then you open it in bytes
    # bytes type can be encoded and decoded
    # for example: anyhting in quotation marks is a string: ''
        # if there is a b'a' it is a byte type tho
    # r'a' == 'a' <- true, because r just ignores backslashes
    # b'a' is NOT equal to 'a'
    # with open in 'br' mode then 
with open ('blurb', 'tr') as f:
    text = f.read()
with open ('blurb', 'br') as f:
    byte = f.read()
    text = byte.decode('utf8')
# the above two open functions are equal to each other

with open ('blurb', encode = 'utf8', 'br') as f: # if added "data/blurb" instead of blurb, then the open function would call the blurb from data folder
    text = f.read() # what you are doing iwth the file (first read it, and then store it in the value/varialbe  "text")
print (text)
# on the python cheat sheet, can ONLY READ FILES, needs to do something different if you want to write to it
    #format like so: with open ('blurb', 'w' ,encode = 'utf8') as f:  <-- this will create a new file
        # f.write(text)
    # print (text)
