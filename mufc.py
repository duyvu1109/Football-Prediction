from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from plotting import show1Chart
# Open Microsoft Edge 
driver = webdriver.Edge(executable_path='msedgedriver.exe')
driver.get("https://www.11v11.com/teams/manchester-united/tab/matches/")

win, draw, lose = 0,0,0
result = driver.find_elements_by_xpath('//*[@id="pageContent"]/div[2]/table/tbody/tr/td[3]/span')
for r in result:
    if (r.text == 'W'):
        win+=1
    elif (r.text == 'D'):
        draw+=1
    else:
        lose+=1
    
print('win: {0}, draw: {1}, lose: {2}'.format(win, draw, lose))
driver.close()
show1Chart(win, draw, lose)

sleep(10)

