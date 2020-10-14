from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from isimolustur import male_name
import random
from selenium.webdriver.common.proxy import Proxy, ProxyType



class InstaBot:
    def __init__(self,male_name):

        self.browser = webdriver.Chrome()
        self.male_name = male_name
        
    def mailcek(self):
        self.browser.get('https://10minutemail.net/')
        time.sleep(2)
        mail = self.browser.find_element_by_id('fe_text')
        self.mailim = mail.get_attribute('value')
        #get_attribute() to get value of input box
        time.sleep(2)
    def instasignup(self):
        self.browser.get('https://www.croxyproxy.com/')
        time.sleep(2)

        croxyproxy = self.browser.find_element_by_xpath("//*[@id='url']")
        croxyproxy.send_keys('https://www.instagram.com/accounts/emailsignup')
        croxyproxy.send_keys(Keys.ENTER)
        time.sleep(2)
    
        
        try: 
            self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[2]/button[1]").click()
        except:
            time.sleep(1)
        time.sleep(2)
        mailinput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
        mailinput.send_keys(self.mailim)
        time.sleep(2) 
        #********************************
        adsoyadinput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]/div/label/input")
        adsoyadinput.send_keys(male_name)
        #********************************
        
        time.sleep(3)
        nickoneri = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[5]/div/div/div/button")
        nickoneri.click()
        number = "Asd2134531!"
        passwordinput = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input ")

        passwordinput.send_keys(number)
        passwordinput.send_keys(Keys.ENTER)

        time.sleep(2)
        yil = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select")
        yil.click()
        yil.send_keys("11")
        yil.send_keys(Keys.ENTER)
   
        ileri = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/div[6]/button")
        ileri.click()
        time.sleep(15)
    def activate(self):
        self.browser.execute_script("window.open('');")
# Switch to the new window and open URL B
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.get("https://10minutemail.net/")
        time.sleep(30)

        refresh = self.browser.find_element_by_xpath("//*[@id='left']/ul/li[1]/a")
        
        refresh.click()
        time.sleep(10)
        refresh2 = self.browser.find_element_by_xpath("//*[@id='left']/ul/li[1]/a")
        refresh2.click()
         
        codes = self.browser.find_element_by_xpath("""//*[@id="maillist"]/tbody/tr[2]/td[2]""").text
        inst_codes = codes[0:6]
        print(inst_codes)
        time.sleep(3)
        self.browser.switch_to.window(self.browser.window_handles[0])
        time.sleep(5)
        onayk = self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div[2]/form/div/div[1]/input")
        onayk.send_keys(inst_codes)
        onayk.send_keys(Keys.ENTER)
              


insta = InstaBot(male_name)
insta.mailcek()
insta.instasignup()
insta.activate()