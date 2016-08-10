#Andrew Godfrey
#August 9, 2016
#RS Item Scraper Version 0.0.4

import json
import urllib2
import time
from   datetime import date
from   input_mysql import *

def do_scrape( length ):
    #Times the operation for efficiency testing
    start = time.time()

    #Fetches Today's Date
    today = date.today()

    #Used as ItemID iterator
    x            = 0  
 
    #Creates or edits text files that will contain item information
    items        = open( 'itemFile'  + str(today) + '.txt' , 'w' )
    used_items   = open( 'ID_used'   + str(today) + '.txt' , 'w' )
    unused_items = open( 'ID_unused' + str(today) + '.txt' , 'w' )   
  
    #Used for Bug testing
    successful   = 0
    failed_404   = 0
    failed_val   = 0

    #Main While loop: Checks Item Ids from 0 to X
    while ( x <= length ):
            print "Looking for id: " + str(x) 
            time.sleep(0.5)
            #checks to see if item is tradeable
            try:
                    data = json.load(urllib2.urlopen('http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=' + str(x)))
                    successful += 1
                    item = data['item']['name']
                    items.write(str(x) + '-' + str(item) + '\n')
                    used_items.write(str(x) + '\n')
                    sequel(str(x) , str(item)) 
		    x += 1
                    print "Found item: " + str(item)
            #If item is not tradeable, this runs
            except urllib2.HTTPError:
                    failed_404 += 1
                    unused_items.write(str(x) + '\n')
                    x += 1
                    print "ID does not correlate to a tradeable item"
            #Notifies if page request is being blocked
            except ValueError:
                    failed_val += 1
                    time.sleep(30)
    
    #Prints time taken
    end = time.time()
    print end - start
    
    #closes files
    items.close()
    used_items.close()
    unused_items.close()
    
    #Looks for bugs caused from sending too many page requests and counts the number of used and unused IDs
    print "Num successful: " + str(successful)
    print "    404 Errors: " + str(failed_404)
    print "   Value Erros: " + str(failed_val)

#Main Function
do_scrape(500)







