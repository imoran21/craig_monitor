from scrape import get_listings, get_or_error, get_tree, get_listing_details, write_file
from settings import base_url, search_url, archive_path, update_path
import json


def load_archived_listings(filename):
  
    with open(filename) as data_file:
        archive_listings = json.load(data_file)
        #get the top level key for each dictionary in the list of listings (this is the url)
        archive_listings = [x.keys()[0] for x in archive_listings]
        return archive_listings



def get_new_listings(archived_listings):
    current_listings = get_listings(get_tree(base_url+search_url))
    new_listings = [x for x in current_listings if x not in archived_listings]
    return new_listings



def main_monitor():
 

    archived_listings = load_archived_listings(archive_path)
    new_listings = get_new_listings(archived_listings)
    details = []
    for x in new_listings:
        d= get_listing_details(get_tree(x))
        if d:
            details.append({x:d})
    
    write_file(update_path, details)
    print '{} new posts found'.format(len(details))
    if len(new_listings) > 0: 
        return True
    else:
        return False



