# test script
from selenium import webdriver
import time  
from selenium.webdriver.common.keys import Keys  
print("sample test case started")  
driver = webdriver.Chrome(r"D:\chromedriver\chromedriver.exe")   
#maximize the window size  
#driver.maximize_window()  
#navigate to the url  
#driver.get("https://www.google.com/")
driver.get("https://learn.upes.ac.in/")  
#identify the Google search text box and enter the value  
#driver.find_element_by_name("q").send_keys("https://learn.upes.ac.in/") 
time.sleep(3)  
#click on the Google search button  
print("opened bb") 
driver.find_element_by_name("user_id").send_keys("500068360@stu.upes.ac.in")
time.sleep(3)
print("id done") 
driver.find_element_by_name("password").send_keys("QV1aID@1")
time.sleep(3)
print("password done") 
driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/div[4]/form/div[3]/ul/li[3]/input").click()  
time.sleep(3)  
print("login done")
driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div/div/button").click()  
time.sleep(3)  
print("agreee") 
#close the browser  
driver.close()  
print("sample test case successfully completed") 
