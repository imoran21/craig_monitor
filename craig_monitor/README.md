# craig_monitor
###python 2
### Requirements: requests, lxml

A simple no frills script to monitor craigslist posts and send email when there is a new one with some info about the post.

## Project Structure

1. main.py file executed by user that will continuously scrape craigslist/sleep
2. scrape.py logic to parse cragslist search results as well as post details 
3. listings.json - master list of all previously scraped items
4. new_listings.json - a file that is written when new listings are found.  This is erased when listings.json is updated
5. monitor.py logic to assess whether there are new posts and update the new_listings.json file
6. aggregate.py Updates the listings with the new listings and clears the new_listings file for the next run
7. send_gmail.py send an email containing the data in the new_listings.json file 
8. refresh.py creates the initial listings.json file by creating it wil all results


##Instructions

1. Clone this directory
2. In settings.py update variables as needed 
3. Create a password_settings.py file and put 3 variables in it for 
    - fromaddr = youremail@gmail.com
    - toemail = destinationemail@gmail.com
    - email_password = youremailpassword
4. run 'python refresh.py' to create the initial set of posts
5. run 'python main.py' to start the main program loop.  This will run contiously every x minutes (specified in settings) and check if any new posts are up, if so it will send an email to the address designated. 

##Notes 
1. may have to change gmail settings for the sender to allow sending of emails through python (turn on access to unauthorized apps in gmail settings) 
2. Only posts with titles are considered, anything without a title is filtered out. 
3. Be curtious and set a reasonable interval cragislist servers arent getting pinged constantly. 

##More info on program loop
1. main.py starts by getting a list of all the current listings in the search page on craigslist
2. checks the list of urls representing posts and checks whether it exists in our listings. 
3. if it does not exist then scrapes the post detail page for the post info and updates the new_listing file with these posts
4. emails the recipients with the contents of the new_listings file
5. update the listings file with the items in the new_listings file since they have been sent
6. clear the new listings file
7. sleep for x amount of min and start again at #1
