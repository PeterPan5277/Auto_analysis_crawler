from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def crawl(PATH, taf_list):
    driver = webdriver.Chrome(PATH)
    driver.get('https://peterpan5277:Pance123456@@aoaws.anws.gov.tw/wmds/content/aoaws_chinese/tafors')
    # time.sleep(2)
    # log = driver.find_element(By.XPATH, '//*[@id="b2"]/ul/ul/li/a')
    # log.click()
    search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "taf_ids")))
    search.clear()
    search.send_keys(taf_list)
    log = driver.find_element(By.XPATH, '/html/body/p/table/tbody/tr[2]/td/ul/li/form/table/tbody/tr[5]/td/font[2]/input')
    log.click()
    # taf_final = driver.find_element(By.XPATH, '/html/body/p/table/tbody/tr[2]/td/pre/text()').text
    taf_final = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'pre'))).text
    with open ('taf.txt', 'w') as f:
        f.write(taf_final)
    driver.quit()
    # taf_final.click()
    # taf_final.send_keys(Keys.CONTROL + 'a') # select all the text
    # taf_final.send_keys(Keys.CONTROL + 'c') # copy it
    # taf = taf_final.send_keys(Keys.CONTROL + 'v') # paste
if __name__ == '__main__':
    PATH = "C:/Users/peteprpan/Desktop/CAA_TAF/chrome/chromedriver.exe"
    taf_list = ('VTCC VLLB VVNB ZGNN ZJHK ZPPP ZGKL ZGGG VHHH RPLI ZSAM ZSFZ ZSWZ ZSPD ZSOF ZSCN\
 ZHHH ZGHA ZUCK ZUUU ZLLL ZLXY ZHCC ZSJN ZBTJ ZBAA ZSQD ZSYT ZYTL ZYTX ZKPY RKSI\
 RKPK RKPC ROAH RJFK RJFF RJOK RJOB RJBB RJGG RJNT')
    crawl(PATH, taf_list)
