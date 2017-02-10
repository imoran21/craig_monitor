from scrape import *
from settings import archive_path

tree = get_tree(base_url+search_url)
listings = get_listings(tree)
listing_details = []
for x in listings:
    d = get_listing_details(get_tree(x)) 
    if d:
        listing_details.append({x:d})
write_file(archive_path,listing_details)
print 'Archive refreshed, {} posts saved in {}'.format(len(listing_details), archive_path)




