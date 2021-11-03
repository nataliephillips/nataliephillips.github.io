#!/usr/bin/python3

'''
This more advanced wget program is more versatile.
It uses command line arguments to specify which URL should be downloaded, and where to save it.
'''

import argparse
import requests

# process command line args
# needs to have two parameters when you use the command
parser = argparse.ArgumentParser(description='Download a webpage') # intializes getting info from a url, descriptive in terms of telling the users what the code does
parser.add_argument('url', help='the url to download from the internet') 
parser.add_argument('filename', help='the path on the local computer to save the file') # corresponds with helping the poeople using the code
args = parser.parse_args() # order matters when people either put the url and filename in
#to make the filename not always inputted by the user, you can put a default filename
    # put two dashes before the filename and then specfiy a defualt
    # parser.add_argument'--filename', defualt = 'dracula.html'
# can make both arguements optional by adding more defaults
    # when specifying a different values for filename and url, just add --url or --filename



# download the url
r = requests.get(args.url)
text = r.text

# save the file
with open(args.filename, 'w', encoding='utf-8') as f:
    f.write(text)