from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

#Import excel data into pandas dataframe
y = pd.read_csv('mfv.mgrname13F.csv') #import CSV file containing the names of the 
a = y['mgrname'] #search by mgrname columnn 

#open browser
driver = webdriver.Chrome()

#placeholder: create pandas dataframe to store info
placeholder = pd.DataFrame(index=[range(0,5934)], columns=['mgrno', 'mgrname','country','zipcode'])

#search keyword name +sec +edgar

#create scrape function for nhs site
def scrape():
	try:
		elem = driver.find_element_by_class_name('departments-services')
		g = elem.get_attribute("innerHTML")
		b = pd.read_html(g)
		b = b[0]
		l = len(b.index)
		for j in range(0,l):
		 	if ('inor' in str(b.iloc[j,1])) or ('inor' in str(b.iloc[j,0])) == True:
		 		if pd.isnull(b.iloc[j,2]) == True:
		 			placeholder.iloc[i,1] = b.iloc[j,1] + ' ?doubt?'
		 		else:
		 			placeholder.iloc[i,1] = b.iloc[j,2]
		 	else:
		 		pass

	except NoSuchElementException:
		try:
			elem = driver.find_element_by_class_name('box')
			elem = elem.find_element_by_tag_name('a')
			placeholder.iloc[i,1] = elem.text
		except NoSuchElementException:
			placeholder.iloc[i,1] = "N/A"

	print placeholder.iloc[i,:]

#Loop for cycling through cells range = number of cells starting with 1
for i in range(0, 130):
	try:
		term = str(a.iloc[i]) #select specific cell - replace with c for address
		placeholder.iloc[i,0] = a.iloc[i]
		term = term.replace(" -",'') + ' NHS choices services' + " site:http://www.nhs.uk/" #for search by name add .replace(" -",'') remove replace for address
		driver.get("https://www.google.com/webhp?complete=0&hl=en")
		elem = driver.find_element_by_name("q")
		elem.send_keys(term)
		elem = driver.find_element_by_name("btnI")
		elem.click()
		x = driver.current_url #retrieve current url as string
		x = x.lower()

	#if already in services tab
		if "www.nhs.uk/services/hospitals/services/" in x:
			scrape()  

	#if not in services tab
		else:
			if "www.nhs.uk/services/hospitals/" in x:
				try:
					elem = driver.find_element_by_link_text('Services')
					elem.click()
					scrape()
				except NoSuchElementException:
					try:
						elem = driver.find_element_by_link_text('Departments and services')
						elem.click()
						scrape()
					except NoSuchElementException:
						placeholder.iloc[i,1] = "N/A"
			else:
				placeholder.iloc[i,1] = "N/A"
	#return to google
		driver.get("https://www.google.com/webhp?complete=0&hl=en")
	except IndexError:
		break
print placeholder
placeholder.to_csv('C:\Users\Samuel\Desktop\FTSE scrape\parent_org_scrape_address.csv')
#close browser
driver.close()

#driver.close() #close browser