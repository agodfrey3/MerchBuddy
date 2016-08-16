#MerchBuddy

This is a project which scrapes the item price data from each tradable item in Runescape and places it into a MYSQL Database
located on a server local to this project, which is then analyzed to find the best item(s) for merching, as well as other 
various information that can be drawn from price trends. 

##Notes:

**8-9-2016**
- Justin Auger has created a MySQL insertion script that will take the information found by the scrape2.py script and place it into a
table located on our server. Justin's script has not been uploaded yet, which is why there is an import in scrape2.py that looks 
foreign. I have added a credential hiding system to Justin's script, however, so it will be uploaded shortly. The scrape2.py script 
is working, but, will continue to be improved as I find ways to do so.

**8-10-2016**
- Added more data variables to the initial scraping script (named 'scrape2.py' for now) that will be used to store any data that we 
may need for analysis. Just waiting on Justin's mySQL insertion tool to be updated to accommodate the changes. The backup logs 
were also modified; they are now csv files to more neatly store the increased amount of data  per item. Now that I am able to 
scrape all the items once, I will work on a second script to run that will only run through the items that are tradable to  
decrease the necessary run time to complete a full scan. That function is currently operational, however, I will not push it 
until it, too, has the extended data that was just added into the initial scraper. 

**8-13-2016**
- The mySQL insertion tool has been completed, so the initial scraper and primary scrapers are fully fuctional as far as data storing
goes. Improvements will continue to be made, however. Daily scrapes will be setup on our server to start collecting data. Run 
time should be around 12:00 daily to ensure the game update has taken place already.  

##Languages used:
- Python (2.7 & 3.5)

##Project by: 
[Andrew Godfrey](https://github.com/agodfrey3/)

[Justin Auger](http://justnaugr.github.io)