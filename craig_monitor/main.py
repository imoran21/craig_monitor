from monitor import main_monitor
from aggregate import main_aggregate
from send_gmail import main_email
import time
from settings import sleep_seconds_interval

while True:
    print 'waking up checking craigslist posts...'
    new = main_monitor()
    if new:
       main_email()
       main_aggregate()
    else:
       print 'No new posts found'
    print 'sleeping for {} minuts'.format(sleep_seconds_interval/60)
    time.sleep(sleep_seconds_interval)
       
