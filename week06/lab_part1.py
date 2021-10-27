'''
with open ('data/condensed_2018.json', encoding = 'ascii') as f:
    Text = f.read()
with open ('data/condensed_2017.json', encoding = 'ascii') as f:
    Text += f.read()
with open ('data/condensed_2016.json', encoding = 'ascii') as f:
    Text += f.read()
with open ('data/condensed_2015.json', encoding = 'ascii') as f:
    Text += f.read()
with open ('data/condensed_2014.json', encoding = 'ascii') as f:
    Text += f.read()
with open ('data/condensed_2013.json', encoding = 'ascii') as f:
    Text += f.read()
with open ('data/condensed_2012.json', encoding = 'ascii') as f:
    Text += f.read()
with open ('data/condensed_2011.json', encoding = 'ascii') as f:
    Text += f.read()
with open ('data/condensed_2010.json', encoding = 'ascii') as f:
    Text += f.read()
with open ('data/condensed_2009.json', encoding = 'ascii') as f:
    Text += f.read()
'''

import json
import glob
tweets = []
text = ""
files = glob.glob('data/*')
for file in files:
    with open (file, encoding = 'ASCII') as f:
        text = f.read()
        tweets += json.loads(text)
print (len(tweets))

count = {}  
num_trump = 0
num_russia = 0
num_obama = 0
num_fake = 0
num_mexico = 0
num_ivanka = 0
num_immigrants = 0
num_stupid = 0
for tweet in tweets:
    lowertweet = tweet['text'].lower()
    if 'trump' in lowertweet:
        num_trump += 1
    if 'russia' in lowertweet:
        num_russia += 1
    if 'obama' in lowertweet:
        num_obama += 1
    if 'fake news' in lowertweet:
        num_fake += 1
    if 'mexico' in lowertweet:
        num_mexico += 1
    if 'ivanka' in lowertweet:
        num_ivanka += 1
    if 'we cannot allow all of these people to invade our country' in lowertweet:
        num_immigrants += 1
    if 'stupid' in lowertweet:
        num_stupid += 1
count = {'trump' : num_trump, 'russia' : num_russia, 'obama' : num_obama, 'fake news' : num_fake, 'mexico' : num_mexico, 'ivanka' : num_ivanka , 'the phrase "we cannot allow all of these people to invade our country"' : num_immigrants, 'stupid' : num_stupid}
print (count)
print ("the percentage of tweets using the phrase:")
total = len(tweets)
for key in count:
    text = "{:>30} : {:>1}" 
    percent = "{0:.2%}".format(count[key]/total)
    print (text.format(key,percent))
