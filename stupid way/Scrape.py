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
ph = pd.DataFrame(index=[range(0,1000)], columns=['mgrno','mgrname','zipcode'])


#create scrape function
def scrape():
	data = urllib2.urlopen(url)
	for line in data:
		if "ZIP" in line: 
			a = line.replace('ZIP:','')
			a = a.replace('	','')
			a = a.replace('\n','')
			print a
			ph['zipcode'].iloc[i] = a
			break

def readystate_complete(d):
    	# AFAICT Selenium offers no better way to wait for the document to be loaded,
    	# if one is in ignorance of its contents.
    	return d.execute_script("return document.readyState") == "complete"

for i in range(0, 1000): #change range later to 5934
	try:
		term = "site:http://www.sec.gov/Archives/edgar/data " + str(y['mgrname'].iloc[i]) + ' 13f' +' edgar' +' zip'
		ph['mgrname'].iloc[i],  ph['mgrno'].iloc[i] = y['mgrname'].iloc[i], y['mgrno'].iloc[i]
		print y['mgrname'].iloc[i]
		driver.get("https://www.google.com/webhp?complete=0&hl=en")
		elem = driver.find_element_by_name("q")
		elem.send_keys(term)
		elem = driver.find_element_by_name("btnI")
		elem.click()
	    	WebDriverWait(driver, 30).until(readystate_complete)
		url = driver.current_url
		scrape()
	except:
		pass

print ph

ph.to_csv('table.csv')