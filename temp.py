from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://www.instagram.com/?hl=eg")

sleep(4)

# just in case its not in english...

driver.find_element_by_xpath(("//select[@class='hztqj']"))\
    .click()

sleep(6)
# need to accept terms (cookies) by yourself

driver.find_element_by_xpath(('//input[@name=\"username\"]'))\
    .send_keys(('ig_pass')) # insert name    
driver.find_element_by_xpath(('//input[@name=\"password\"]'))\
    .send_keys(('password')) # insert password 
driver.find_element_by_xpath(('//button[@type="submit\"]'))\
    .click()
    
sleep(5)  

driver.find_element_by_xpath(("//button[contains(text(),'Not Now')]"))\
    .click()
driver.find_element_by_xpath(("	//button[contains(@class,'HoLwm')]"))\
    .click()
sleep(5)  

# add you personal list

names = ("ricardo.de.matos", '') # do not let the list be just one name

for name in names:
    driver.find_element_by_xpath(("//span[@class='TqC_a']"))\
        .click()
    sleep(2)
    driver.find_element_by_xpath(("//input[@type='text']"))\
        .send_keys((name))
    sleep(4)
    driver.find_element_by_xpath(("/html[1]/body[1]/div[1]/section[1]/nav[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/div[1]/a[1]/div[1]/div[2]/div[1]/span[1]"))\
        .click()
    sleep(2)
    try:
        # driver.find_element_by_xpath(("//button[contains(text(),'Follow')]"))\
            # .click()
        driver.find_element_by_xpath(("/html[1]/body[1]/div[1]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/span[1]/button[1]"))\
        .click()
    except:
        pass
    

