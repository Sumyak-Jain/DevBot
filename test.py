# test script
from selenium import webdriver
import time  
from selenium.webdriver.common.keys import Keys  
print("sample test case started")  
driver = webdriver.Chrome(r"D:\chromedriver\chromedriver.exe")   
#maximize the window size  
driver.maximize_window()  
#navigate to the url  
#driver.get("https://www.google.com/")
driver.get("https://learn.upes.ac.in/")  
#identify the Google search text box and enter the value  
#driver.find_element_by_name("q").send_keys("https://learn.upes.ac.in/") 
time.sleep(3)  
#click on the Google search button  

print("opened bb") 
driver.find_element_by_name("user_id").send_keys("..")
time.sleep(3)
print("id done") 
driver.find_element_by_name("password").send_keys("..")
time.sleep(3)
print("password done")
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[4]/form/div[3]/ul/li[3]/input").click()  
time.sleep(3)  
print("login done")
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div/div/button").click()  
time.sleep(3)  
print("agreee")
driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[2]/ul/li[3]/a").click()  
time.sleep(3)  
print("cloud class") 
driver.find_element_by_xpath("/html/body/div[5]/div[2]/nav/div/div[2]/div/div[2]/ul/li[18]/a/span/b").click()  
time.sleep(15)  
print("collabrate") 
time.sleep(15)
#driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/main/div[1]/div/div/button/div[1]").click()  
#time.sleep(15)  
print("collabrate+1") 
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div/div[2]/div/bb-loading-button/button").click()  
time.sleep(3)  
print("join class") 

#close the browser  
driver.close()  
print("sample test case successfully completed") 
