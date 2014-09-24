from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import urllib2

#Import excel data into pandas dataframe
y = pd.read_csv('mfv.mgrname13F.csv') #import CSV file containing the names of the companies

#open browser
driver = webdriver.Chrome()

#placeholder: create pandas dataframe to store info
placeholder = pd.DataFrame(index=[range(0,20)], columns=['mgrno', 'mgrname','country','zipcode']) #change range later to 5934


#create scrape function
def scrape():
	data = urllib2.urlopen(url)
	for line in data:
		if "ZIP" in line: 
			a = line.replace('ZIP:','')
			a = a.replace('	','')
			print a
			break


def readystate_complete(d):
    	# AFAICT Selenium offers no better way to wait for the document to be loaded,
    	# if one is in ignorance of its contents.
    	return d.execute_script("return document.readyState") == "complete"

for i in range(0, 10): #change range later to 5934
	term = "site:http://www.sec.gov/Archives/edgar/data " + str(y['mgrname'].iloc[i]) + ' 13f' +' edgar'
	print(term)
	driver.get("https://www.google.com/webhp?complete=0&hl=en")
	elem = driver.find_element_by_name("q")
	elem.send_keys(term)
	elem = driver.find_element_by_name("btnI")
	elem.click()
    	WebDriverWait(driver, 30).until(readystate_complete)
	url = driver.current_url
	scrape()
