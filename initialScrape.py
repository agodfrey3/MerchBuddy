#Andrew Godfrey
#August 9, 2016
#RS Item Scraper Version 0.0.5

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
    items        = open( 'logFiles/itemInfo'  + str(today) + '.csv' , 'w' )
    used_items   = open( 'logFiles/ID_used'   + str(today) + '.txt' , 'w' )
    unused_items = open( 'logFiles/ID_unused' + str(today) + '.txt' , 'w' )   
  
    #Used for Bug testing
    successful   = 0
    failed_404   = 0
    failed_val   = 0

    #Main While loop: Checks Item Ids from 0 to X
    while ( x <= length ):
            print "Looking for id: " + str( x )
            time.sleep( 0.5 )
            #checks to see if item is tradeable
            try:
                    data = json.load(urllib2.urlopen( 'http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=' + str(x)) )
                    successful += 1
                    #Stores item data into unique variables, which are then sent to mysql and a backup csv file
                    item               = data['item']['name']
                    ID                 = data['item']['id']
                    icon_large         = 'http://services.runescape.com/m=itemdb_rs/5276_obj_big.gif?id=' + str(ID)
                    descr              = data['item']['description']
                    is_members         = data['item']['members']
                    curr_price         = data['item']['current']['price']
                    price_change_today = data['item']['today']['price']
                    curr_trend         = data['item']['current']['trend']
                    trend_today        = data['item']['today']['trend']             
                    day30_trend        = data['item']['day30']['trend']
                    day30_change       = data['item']['day30']['change']
                    day90_trend        = data['item']['day90']['trend']
                    day90_change       = data['item']['day90']['change']
                    day180_trend       = data['item']['day180']['trend']
                    day180_change      = data['item']['day180']['change']
                    #Eliminates errors in the name string
		    item = data['item']['name']
                    item = item.replace("'" , "")
                    #Inputs data to mySQL database
                    sequel( ID, item, icon_large, descr, is_members, curr_price, price_change_today, curr_trend, trend_today, day30_trend,
			day30_change, day90_trend, day90_change, day180_trend, day180_change ) 
		    #writes to a csv file for backup   
                    items.write(
                       str(item)         + '|'      + str(ID)           + '|' + icon_large              + '|' + str(descr) + '|'        + 
                       str(is_members)   + '|'      + str(curr_price)   + '|' + str(price_change_today) + '|' + str(curr_trend)  + '|' + 
                       str(trend_today)  + '|'      + str(day30_trend)  + '|' + str(day30_change)       + '|' + str(day90_trend) + '|' +  
                       str(day90_change) + '|'      + str(day180_trend) + '|' + str(day180_change)      + '|' + '\n' )
                    
                    used_items.write(str(x) + '\n')
                    x += 1
                    print "Found item: " + str( item )
            #If item is not tradeable, this runs
            except urllib2.HTTPError:
                    failed_404 += 1
                    unused_items.write( str( x ) + '\n' )
                    x += 1
                    print "ID does not correlate to a tradeable item"
            #Notifies if page request is being blocked
            except ValueError:
                    failed_val += 1
                    time.sleep( 2 )
    
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
do_scrape( 50000 )
