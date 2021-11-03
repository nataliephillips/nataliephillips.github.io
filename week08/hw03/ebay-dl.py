import requests
import json
import argparse
from bs4 import BeautifulSoup
import sys #read in ANY command line arguments when running the file
import csv

def parse_itemssold(text):
    '''
    Takes as input a string and returns the number of items sold, as specified in the string
    
    >>> parse_itemssold('38 sold')
    38
    >>> parse_itemssold('14 watchers')
    0
    >>> parse_itemssold('Almost gone')
    0
    '''
    numbers = ''
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'sold' in text: 
        return int(numbers)
    else:
        return 0

def parse_price(text):
    '''
    Takes as input a string and returns the price of the items sold, as specified in the string
    
    >>> parse_price('$54.99 to $79.99')
    5499
    >>> parse_price('$13.99')
    1399
    >>> parse_price('$7.95')
    795
    >>> parse_price('Free shipping')
    0
    >>> parse_price('+$5.00 shipping')
    500
    >>> parse_price('+$15.80 shipping')
    1580
    '''
    numbers = ''
    if text.find("to")!=-1:
        text = text[:text.find("to")]
    for char in text:
        if char in '1234567890':
            numbers += char
    if 'Free' in text:
        return 0
    else:
        return int(numbers)


# this if statement says only run the code below when the pythoon file is run normally, meaning not inside the doctests/ 
if __name__ == '__main__':
    # getting command line arguements, of the search terms
    parser = argparse.ArgumentParser(description='download information from ebay and convert to json')
    parser.add_argument('search_term')
    parser.add_argument('--num_pages', default=10)
    parser.add_argument('--csv', action='store_true')
    args = parser.parse_args()
    print ('args.search_term = ', args.search_term)
    print ('args.csv = ', args.csv)
    print ('args.num_pages = ', args.num_pages)
    # list of all items found on each ebay webpage
    items = []

    # loop over ebay webpages
    for page_number in range (1,int(args.num_pages)+1):
        
        #build the url
        if args.search_term.find(" ")!=-1:
            args.search_term = args.search_term.replace(" ", "+")
        url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw='+ args.search_term + '&_sacat=0&_pgn=' + str(page_number) + '&rt=nc'
        r = requests.get(url)
        r.status_code
        print ("url = " + url)

        # download the html
        r = requests.get(url)
        status = r.status_code
        print ('status = ', status)

        html = r.text
        #print ("html = ", html[:50])

        # process the html
        soup = BeautifulSoup(html, 'html.parser')
        
        tags_items = soup.select('.s-item')
        for tag_item in tags_items:
            #print ('tag_item', tag_item)
            
            #extract names
            tags_name = tag_item.select('.s-item__title')
            name = None
            for tag in tags_name:
                #print('tag = ', tag.text)
                name = tag.text
            
            #extract free returns 
            freereturns = False
            tags_freereturn = tag_item.select('.s-item__free-returns')
            for tag in tags_freereturn:
                freereturns = True
                        
            # extract items sold
            itemssold = None
            tags_itemssold = tag_item.select('.s-item__hotness')
            for tag in tags_itemssold:
                itemssold = parse_itemssold(tag.text)

            #extract status
            tags_status = tag_item.select('.SECONDARY_INFO')
            status = None
            for tag in tags_status:
                # print('tag = ', tag.text)
                status = tag.text
            
            #extract price
            price = 0
            tags_price = tag_item.select('.s-item__price')
            for tag in tags_price:
                # print('tag = ', parse_price(tag.text))
                price = parse_price(tag.text)
            
            #extract shipping
            shipping = 0
            tags_shipping = tag_item.select('.s-item__shipping')
            for tag in tags_shipping:
                shipping = parse_price(tag.text)

            item = {
                'name' : name, 
                'freereturns' : freereturns,
                'itemssold' : itemssold,
                'status' : status,
                'price' : price,
                'shipping' : shipping
            }
            items.append(item) 

            for item in items:
                ('item = ', item)
        items = items[1:]
        # print ('len(items)=', len(items))

    if args.csv == True:
        filename = args.search_term+'.csv'
        with open(filename, 'w') as f: 
            columnnames = ["name", "freereturns", "itemssold", "status", "price", "shipping"]
            writer = csv.DictWriter(f, fieldnames=columnnames)
            writer.writeheader()
            for data in items:
                writer.writerow(data)
    else:
        filename = args.search_term+'.json'
        with open(filename, 'w', encoding='UTF-8') as f:
            f.write(json.dumps(items))