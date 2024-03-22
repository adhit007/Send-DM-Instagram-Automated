from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "localhost:9222")
browser = webdriver.Chrome(options=options)

# Enter username/keyword target send message
usernames = ['', ''] 

# Messages:
messages = ['hello world! :)'] # Enter Your Message Here


for user in usernames:
        try:
                    time.sleep(10)
                    browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[5]/div/div/div/span/div/a/div').click()
                    browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div[4]/div').click()
                    time.sleep(3)
                    input_target = browser.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input')
                    input_target.send_keys(user)
                    time.sleep(5)
                    browser.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div').click()
                    time.sleep(3)
                    browser.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div').click()
                    browser.implicitly_wait(10)
                    time.sleep(10)
                    input_message = browser.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
                    input_message.send_keys(messages)
                    time.sleep(3)
                    input_message.send_keys(Keys.ENTER)         
        except Exception as err:
                print(err)
        else:
                print(f'Message successfully sent to {usernames}')
