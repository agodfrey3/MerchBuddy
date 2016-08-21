# Andrew Godfrey
# 8 / 20 / 2016
# Daily Scraping Tool
# Version 0.0.6

import json
import urllib2
import time
import pymysql
from   datetime    import date
import os

def daily_scrape():
        # Gets today's date
        today     = date.today()
        curr_date = str(today.strftime('%m%d%Y'))

        # Opens database connections
        # db1 is home to the list of IDs we will be scraping
        db1 = pymysql.connect(credentials.host, credentials.username, credentials.password, "initial_item_list")
        # db2 is where we wish to send our information
        db2 = pymysql.connect(credentials.host, credentials.username, credentials.password, "primary_scrape_test")

        # Prepares cursor objects to execute mysql commands on respective databases
        cursor1 = db1.cursor()
        cursor2 = db2.cursor()

        # Creates a table based on the current date to store item information in db2
        cursor2.execute("create table IF NOT EXISTS `"+ curr_date +"` (item_id varchar(10),item_name varchar(50),item_icon varchar(255),item_desc varchar(255),item_is_mem varchar(10),item_curr_price varchar(10),item_pchange_today varchar(20),item_curr_trend varchar(20),item_trend_today varchar(20),item_day30_trend varchar(20),item_day30_change varchar(20),item_day90_trend varchar(30),item_day90_change varchar(20),item_day180_trend varchar(20),item_day180_change varchar(20));")

        # Declares and defines a variable that will be used as an index
        a = 0

        # Fetches all the information we need from db1
        # Gets all item ids from database and sends them to variable item_ids
        cursor1.execute("select item_id from items;")
        item_ids   = cursor1.fetchall()

        # Main loop : Checks all IDs from our database
        for row in item_ids:
                # Cleans data that will be used later on to ensure no syntax errors
                #ID   = str(item_ids[a]).replace("'", "")
                #ID   = str(ID).replace("(", "")
                #ID   = str(ID).replace(")", "")
                #ID   = str(ID).replace(",", "")
                ID = str(row).replace("(","")
                ID = ID.replace(")","")
                ID = ID.replace(",","")
                ID = ID.replace("'","")
                print ID
                print "Looking for ID: " + str(ID) + "..."
                try:
                        # Sends a web request for item information
                        data = json.load(urllib2.urlopen('http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=' + str(ID)))
                        print "Found information on ID : " + str(ID) + "..."
                        # Cleans all item data and places them into a variable
                        item = str(data['item']['name']).replace("'", "")
                        icon_large         = 'http://services.runescape.com/m=itemdb_rs/5276_obj_big.gif?id=' + str(ID)
                        descr              = str(data['item']['description']).replace("'", "")
                        is_members         = data['item']['members']
                        curr_price         = data['item']['current']['price']
                        price_change_today = data['item']['today']['price']
                        curr_trend         = data['item']['current']['trend']
                        trend_today        = data['item']['today']['trend']
                        day30_trend        = data['item']['day30']['trend']
                        day30_change       = str(data['item']['day30']['change']).replace("%", "")
                        day90_trend        = data['item']['day90']['trend']
                        day90_change       = str(data['item']['day90']['change']).replace("%", "")
                        day180_trend       = data['item']['day180']['trend']
                        day180_change      = str(data['item']['day180']['change']).replace("%", "")

                        # Sends item information to database
                        cursor2.execute("insert into `"+ curr_date +"`(item_id,item_name,item_icon,item_desc,item_is_mem,item_curr_price,item_pchange_today,item_curr_trend,item_trend_today,item_day30_trend,item_day30_change,item_day90_trend,item_day90_change,item_day180_trend,item_day180_change) VALUES('"+str(ID)+"','"+str(item)+"','"+str(icon_large)+"','"+str(descr)+"','"+str(is_members)+"','"+str(curr_price)+"','"+str(price_change_today)+"','"+str(curr_trend)+"','"+str(trend_today)+"','"+str(day30_trend)+"','"+str(day30_change)+"','"+str(day90_trend)+"','"+str(day90_change)+"','"+str(day180_trend)+"','"+str(day180_change)+"')")
                        print "Data for ID: " + str(ID) + " placed into datebase..."
                        # Increments the index
                        #a += 1
                        # Commits changes to database
                        db2.commit()
                # Catches error caused by untradable items
                except urllib2.HTTPError:
                        print "Item not tradable...Error in ID list."
                        # Catches error caused by our request being blocked. Reruns request until unblocked
                except ValueError:
                        print "Waiting..."
                        time.sleep(2)

        #Closes databases and commits changes
        cursor1.close()
        cursor2.close()
        db1.close()
        db2.close()

# Runs main function
daily_scrape()

