#Made by Justin Auger
#August 9, 2016
#MySQL Inserting Script
#Verion 0.0.1
import pymysql
import datetime
import credentials

def sequel(item_id,item_name):
	# Open database connection ( If database is not created don't give dbname)
	db = pymysql.connect(credentials.host,credentials.username,credentials.password,"justin_test")

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	date_list = []
	today = datetime.date.today()
	date = str(today.strftime('%m%d%Y'))

	# create table
	cursor.execute("SET sql_notes = 0; ")
	cursor.execute("create table IF NOT EXISTS `"+ date +"` (item_ids varchar(10),item_names varchar(50));")
	cursor.execute("SET sql_notes = 1; ")

	#insert data
	cursor.execute("insert into `"+ date +"`(item_ids,item_names) VALUES('"+str(item_id)+"','"+str(item_name)+"')")

	# Commit your changes in the database
	db.commit()
	# disconnect from server
	db.close()

