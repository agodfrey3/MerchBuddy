# Andrew Godfrey
# getAvg Version 1
# 9/14/2016
# This is the first (unfinished) algorithm, which gets the average price change per day. (Not fully documented, yet)
# Note: Script unfinished. Currently it iterates through each item in each database table to get the average change.
# To Do: Account for price change display e.g. 16.6k instead of 16,600. Implement error handling.
#        Implement comparison system to see if daily change is withing x% of average.
#        Set flag on that id if not. (notify user)
#        Create max/min prices and check against them. 

import pymysql
import credentials

def formatString(input): # Takes all characters out of strings that will cause error
        input = str(input)
        input = input.replace(' ','')
        input = input.replace("'",'')
        input = input.replace('(','')
        input = input.replace(')','')
        input = input.replace(',','')
        return input

def getAvg( ID, tables, passes, numTables): # Returns the average change for item ID: ID
        totalValue = 0
        for (table_name, ) in tables:
                db2 = pymysql.connect(credentials.host, credentials.username, credentials.password, "primary_scrape_test") # DB to iterate through
                cursor2 = db2.cursor()

                passes += 1
                table_name = str(table_name)
                cursor2.execute("SELECT item_pchange_today from `"+ table_name +"` WHERE item_id = "+str(ID)+"")
                currVal = cursor2.fetchone()
                currVal = formatString(currVal)
        
                if totalValue == 0:
                        totalValue = int(currVal)
                else:
                        totalValue = (totalValue + int(currVal))
                if passes == int(numTables):
                        avgChange = totalValue / passes
                        print "Average Change for item ID:" + str(ID) + " -> " + str(avgChange)

def main(): # Performs getAvg for each item_id in the specified database ( 4223 item_ids in database )
        totalValue = 0
        passes = 0

        db1 = pymysql.connect(credentials.host, credentials.username, credentials.password, "initial_item_list") # DB of item ids
        cursor1 = db1.cursor() # creates cursor object
        cursor1.execute("SELECT item_id FROM items") # Use as reference list for ids

        db3 = pymysql.connect(credentials.host, credentials.username, credentials.password, "primary_scrape_test") # DB to iterate through
        cursor3 = db3.cursor()
        cursor3.execute("SHOW TABLES")

        tables = cursor3.fetchall()

        cursor3.execute("SHOW TABLES")
        cursor3.execute("SELECT FOUND_ROWS()")
        
        numTables = cursor3.fetchone()
        numTables = formatString(numTables)

        IDtoUse = cursor1.fetchone()

        while IDtoUse is not None:
                ID = formatString(IDtoUse)
                getAvg(ID, tables, passes, numTables)
                IDtoUse = cursor1.fetchone()

main() # driver for script
