#!/usr/bin/python3

'''
A wget program is a program that "gets" something from the "w"eb,
and saves it to the local computer.
It is the "hello world" of web programming.

simplest thing to get files from the internet
if you want to use requests, you must run the pip install requests to get it
requests library is not built into python

'''

import requests

# this is a correct url, if you plug in gibberish a 404 error will come up
# error 404 is a valid webpage saying that its not a webpage
# when we open an incorrect file, python gave us an error mesage
# but when we open an incorrect url, python sometimes does and sometimes doesnt give an error
# webreqeusts and urls r confusing, more so than files
# schema://domain/path <- set up of the url, if the domain is not right there will be a 404 error
# if missing the schema, if will have a python error
# 
url = 'https://www.gutenberg.org/files/345/345-h/345-h.htm'
filename = 'dracula.html'

# download the url
# stats code, tells us the number of the webpage, if the webpage is 404, then there is an error
# r.statuscode == 200, when it is a successful url
'''
other ways things can fail
- 503 status code, dont have permission to access the url, if you are downloading too much stuff
    - have certain limits about how much a person/computer can download infomration from the web
    - can you bounce around other ip addresses
'''

r = requests.get(url)
if r.status_code == 404: # url not found
    print ("ERROR 404")
elif r.status_code == 200: #successful
    text = r.text

# save the file
with open(filename, 'w', encoding='utf-8') as f:
    f.write(text)

