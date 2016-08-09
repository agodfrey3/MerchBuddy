import json
import urllib2
import time


successful = 0
failed404  = 0
failedVal  = 0
x          = 0

f = open('itemFile_8_7_2016.txt'  , 'w')
w = open('ID_used_8_7_2016.txt'   , 'w')
q = open('ID_unused_8_7_2016.txt' , 'w')


def rs_scrape( x , successful , failed404 , failedVal ):
        time.sleep(.4)
        try:
                data = json.load(urllib2.urlopen('http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=' + str(x)))
                successful += 1
		item = data['item']['name']
		f.write(str(x) + '-' + str(item) + '\n')
		w.write(str(x) + '\n')
		x = x + 1
		print "Found item: " + str(item)
		do_scrape( x , successful , failed404, failedVal)

        except urllib2.HTTPError:
                failed404 += 1
		q.write(str(x) + '\n')
		x = x +  1
		print "ID does not correlate to a tradeable item"
        	do_scrape( x , successful , failed404, failedVal)
		
	except ValueError:
		time.sleep(2)
                do_scrape( x , successful, failed404, failedVal)
                failedVal += 1
                print "Value Error"
        

def do_scrape( x , successful, failed404, failedVal):
	while (x < 1000):
        	print "Looking for id: " + str(x)
        	try:
        	        data = json.load(urllib2.urlopen('http://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item=' + str(x)))
        	        successful += 1
			item = data['item']['name']
			f.write(str(x) + '-' + str(item) + '\n')
			w.write(str(x) + '\n')
			x = x + 1
        	        print "Found item: " + str(item)		
        	except urllib2.HTTPError:
        	        failed404 += 1
			q.write(str(x) + '\n')
			x = x + 1
        	        print "ID does not correlate to a tradeable item"
        	except ValueError:
			time.sleep(2)
			rs_scrape( x, successful, failed404, failedVal)
        	        
	print "Num successful: " + str(successful)
	print "    404 Errors: " + str(failed404)
	print "   Value Erros: " + str(failedVal)       	        

start = time.time()
do_scrape(x , successful, failed404, failedVal)
end = time.time()

print end - start 

f.close()
w.close()
q.close()













