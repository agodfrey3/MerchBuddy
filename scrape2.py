#Andrew Godfrey
#August 9, 2016
#RS Item Scraper Version 0.0.3

import json
import urllib2
import time

#Used for Bug testing
successful = 0
failed404  = 0
failedVal  = 0

#Used as ItemID iterator
x          = 0

#Creates or edits text files that will contain item information
items = open('itemFile_8_7_2016.txt'  , 'w')
used_items = open('ID_used_8_7_2016.txt'   , 'w')
unused_items = open('ID_unused_8_7_2016.txt' , 'w')

def do_scrape( x , successful, failed404, failedVal):
        #Main While loop: Checks Item Ids from 0 to X
        while (x <= 50):
                print "Looking for id: " + str(x)
                time.sleep(0.5)
                
                #checks to see if item is tradeable
                try:
                        data = json.load(urllib2.urlopen('http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=' + str(x)))
                        successful += 1
                        item = data['item']['name']
                        items.write(str(x) + '-' + str(item) + '\n')
                        used_items.write(str(x) + '\n')
                        x += 1
                        print "Found item: " + str(item)
                #If item is not tradeable, this runs
                except urllib2.HTTPError:
                        failed404 += 1
                        unused_items.write(str(x) + '\n')
                        x += 1
                        print "ID does not correlate to a tradeable item"

                #Notifies if page request is being blocked
                except ValueError:
                        time.sleep(2)

        #Looks for bugs caused from sending too many page requests
        print "Num successful: " + str(successful)
        print "    404 Errors: " + str(failed404)
        print "   Value Erros: " + str(failedVal)

#Times the operation for efficiency testing
start = time.time()
do_scrape(x , successful, failed404, failedVal)
end = time.time()

print end - start

#closes files
items.close()
used_items.close()
unused_items.close()

