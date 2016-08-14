#Made by Justin Auger
#August 9, 2016
#MySQL Inserting Script
#Verion 0.0.1
import pymysql
import datetime
import credentials

def sequel(item_id,item_name,item_icon,item_desc,item_is_mem,item_curr_price,item_pchange_today,item_curr_trend,item_trend_today,item_day30_trend,item_day30_change,item_day90_trend,item_day90_change,item_day180_trend,item_day180_change):
	# Open database connection ( If database is not created don't give dbname)
	db = pymysql.connect(credentials.host,credentials.username,credentials.password,"justin_test")

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	date_list = []
	today = datetime.date.today()
	date = str(today.strftime('%m%d%Y'))

	# create table
	cursor.execute("SET sql_notes = 0; ")
	cursor.execute("create table IF NOT EXISTS `"+ date +"` (item_id varchar(10),item_name varchar(50),item_icon varchar(255),item_desc varchar(255),item_is_mem varchar(5),item_curr_price varchar(10),item_pchange_today varchar(15),item_curr_trend varchar(15),item_trend_today varchar(15),item_day30_trend varchar(15),item_day30_change varchar(15),item_day90_trend varchar(15),item_day90_change varchar(15),item_day180_trend varchar(15),item_day180_change varchar(15));")
	cursor.execute("SET sql_notes = 1; ")

	#insert data
	cursor.execute("insert into `"+ date +"`(item_id,item_name,item_icon,item_desc,item_is_mem,item_curr_price,item_pchange_today,item_curr_trend,item_trend_today,item_day30_trend,item_day30_change,item_day90_trend,item_day90_change,item_day180_trend,item_day180_change) VALUES('"+str(item_id)+"','"+str(item_name)+"','"+str(item_icon)+"','"+str(item_desc)+"','"+str(item_is_mem)+"','"+str(item_curr_price)+"','"+str(item_pchange_today)+"','"+str(item_curr_trend)+"','"+str(item_trend_today)+"','"+str(item_day30_trend)+"','"+str(item_day30_change)+"','"+str(item_day90_trend)+"','"+str(item_day90_change)+"','"+str(item_day180_trend)+"','"+str(item_day180_change)+"')")

	# Commit your changes in the database
	db.commit()
	# disconnect from server
	db.close()

