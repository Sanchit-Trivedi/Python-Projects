# Name: Sanchit Trivedi

import urllib.request 
import datetime

def weather_response(location , API_key):
	#This function obtains the json from the api,converts it to a string and returns it
	URL=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/forecast?q='+location+'&APPID='+API_key)
	result=URL.read()#reading the data provided by the url
	y=str(result)#conversion to string
	x=y.lstrip("b'").rstrip("'")#removing the excess "b'" and "'" python3 adds as json is binary type
	return x

def has_error(location,json):
	#This function checks whether the given location is present in the json i.e the location is valid
	if json.find(location)==-1:          
		return False
	else:
		return True

def get_dateandtime(n,t):
	''' This function is used to calculate the date from the current date along with the required time '''
	date=datetime.date.today()#fetching the current date using the date time module
	new_date=date+datetime.timedelta(days=n)#adding the no. of days as required by the user
	new_date=str(new_date) #changing type from a class object to a string
	y=str(new_date+' '+t)
	return y

def get_value(end,search_string,json):
	''' This function is used to search for the required value in the string json and returns it '''
	val_start=json.find(search_string,end-350,end)# end-350 reduces the amount of string we have to search through
	val_end=json.find(',',val_start+len(search_string)+2,end)
	result=json[val_start+len(search_string)+2:val_end]
	return result

def check_valid_date(n):
	''' This fuction checks whether the given input of n is valid or not'''
	if n<=4 :
		return True
	else:
		return False

def check_valid_time(t):
	''' This fuction checks whether the given input of time t is valid or not'''
	if t in ['00:00:00','03:00:00','06:00:00','09:00:00','12:00:00','15:00:00','18:00:00','21:00:00']:
		return 1
	else:
		return 0


def get_temperature(json,n=0,t="21:00:00"):
	''' This function returns the value of temperature for the given date and time from the json'''
	cd=check_valid_date(n)
	ct=check_valid_time(t)
	if cd and ct:
		x=get_dateandtime(n,t)
		if x in json:
			end=json.find(x)
			search_string="temp"
			return float(get_value(end,search_string,json))#type casting to float
	else:
		if cd==1 and ct==0:
			return 'Invalid Time'
		elif cd==0 and ct==1:
			return 'Invalid Date'
		else:
			return 'Invalid Date and Time'

def get_humidity(json,n=0,t="21:00:00"):
	'''  This fuction returns the value of humidity for the given date and time from the json'''
	cd=check_valid_date(n)
	ct=check_valid_time(t)
	if cd and ct:
		x=get_dateandtime(n,t)

		if x in json:
			end=json.find(x)
			search_string="humidity"
			return float(get_value(end,search_string,json))#type casting to float
	else:
		if cd==1 and ct==0:
			return 'Invalid Time'
		elif cd==0 and ct==1:
			return 'Invalid Date'
		else:
			return 'Invalid Date and Time'

def get_pressure(json,n=0,t="21:00:00"):
	''' This function returns the value of pressure for the given date and time from the json '''
	cd=check_valid_date(n)
	ct=check_valid_time(t)
	if cd and ct:
		x=get_dateandtime(n,t)

		if x in json:
			end=json.find(x)
			search_string="pressure"
			return float(get_value(end,search_string,json))#type casting to float
	else:
		if cd==1 and ct==0:
			return 'Invalid Time'
		elif cd==0 and ct==1:
			return 'Invalid Date'
		else:
			return 'Invalid Date and Time'

def get_wind(json,n=0,t="21:00:00"):
	''' This function returns the value of wind speed for the given date and time from the json'''
	cd=check_valid_date(n)
	ct=check_valid_time(t)
	if cd and ct:
		x=get_dateandtime(n,t)
		
		if x in json:
			end=json.find(x)
			search_string="speed"
			return float(get_value(end,search_string,json))#type casting to float
	else:
		if cd==1 and ct==0:
			return 'Invalid Time'
		elif cd==0 and ct==1:
			return 'Invalid Date'
		else:
			return 'Invalid Date and Time'

def get_sealevel(json,n=0,t="21:00:00"):
	''' This function returns the value of sea level for the given date and time from the json'''

	cd=check_valid_date(n)
	ct=check_valid_time(t)
	if cd and ct:
		x=get_dateandtime(n,t)
		
		if x in json:
			end=json.find(x)
			search_string="sea_level"
			return float(get_value(end,search_string,json))#type casting to float
	else:
		if cd==1 and ct==0:
			return 'Invalid Time'
		elif cd==0 and ct==1:
			return 'Invalid Date'
		else:
			return 'Invalid Date and Time'



