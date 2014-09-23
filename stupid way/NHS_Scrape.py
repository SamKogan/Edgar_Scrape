from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd

#Import excel data into pandas dataframe
y = pd.read_csv('mfv.mgrname13F.csv') #import CSV file containing the names of the 

#open browser
driver = webdriver.Chrome()

#placeholder: create pandas dataframe to store info
placeholder = pd.DataFrame(index=[range(0,5934)], columns=['mgrno', 'mgrname','country','zipcode'])


#create scrape function for nhs site
def scrape():
	for i in range(0, 2): #change range later to 5934
		term = str(y['mgrname'].iloc[i]) + ' sec' +' edgar'
		print(term)
		driver.get("https://www.google.com/webhp?complete=0&hl=en")
		elem = driver.find_element_by_name("q")
		elem.send_keys(term)
		elem = driver.find_element_by_name("btnI")
		elem.click()
		url = driver.current_url
		print(url)
		a = pd.read_csv(url, sep="/n")
		print a

# 	#if already in services tab
# 		if "www.nhs.uk/services/hospitals/services/" in x:
# 			scrape()  

# 	#if not in services tab
# 		else:
# 			if "www.nhs.uk/services/hospitals/" in x:
# 				try:
# 					elem = driver.find_element_by_link_text('Services')
# 					elem.click()
# 					scrape()
# 				except NoSuchElementException:
# 					try:
# 						elem = driver.find_element_by_link_text('Departments and services')
# 						elem.click()
# 						scrape()
# 					except NoSuchElementException:
# 						placeholder.iloc[i,1] = "N/A"
# 			else:
# 				placeholder.iloc[i,1] = "N/A"
# 	#return to google
# 		driver.get("https://www.google.com/webhp?complete=0&hl=en")
# 	except IndexError:
# 		break
# print placeholder
# placeholder.to_csv('C:\Users\Samuel\Desktop\FTSE scrape\parent_org_scrape_address.csv')
# #close browser
# driver.close()
print y
scrape()