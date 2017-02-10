from lxml import html 
import requests
import json
from settings import base_url, search_url

#for tolerance as we would rather have missing data than errors
def get_or_error(tree, xp, error_msg,first=True):
    try:
        result=tree.xpath("{}".format(xp))
        if first:
            result = result[0]       
    except Exception as e:
	result = error_msg
    return result

def get_tree(url):
    page = requests.get(url)
    tree = html.fromstring(page.content)
    return tree

#can be used on any craigslist search page to get list of all posting links
def get_listings(tree):
    listings = tree.xpath("//li[@class='result-row']//a/@href") 
    listings = [base_url + x  for x in listings if x.startswith('/')]
    return list(set(listings))

#subject to change if craigslist page design changes
def get_listing_details(t):
    price = get_or_error(t, "//span[@class='price']/text()", 'No Price found')  
    housing = get_or_error(t, "//span[@class='housing']/text()", 'No Housing found')
    title = get_or_error(t, "//span[@id='titletextonly']/text()", 'No Title Found')
    location = get_or_error(t, "//span[@class='postingtitletext']//small/text()", 'No location Found')  
    body = " ".join(get_or_error(t,"//section[@id='postingbody']/text()", ['No Body Found'], False))
    if title == 'No Title Found':
        return {}
    else: 
         return {'price':price, 'housing':housing,'title':title,'body':body, 'location':location}

def write_file(output_file, json_data):
    with open(output_file, 'w') as outfile:
        json.dump(json_data, outfile)



 




 
