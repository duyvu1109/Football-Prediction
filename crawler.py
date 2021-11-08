from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from plotting import show1Chart, showCharts
import pandas as pd
# Open Microsoft Edge 
driver = webdriver.Edge(executable_path='msedgedriver.exe')
driver.get("https://www.11v11.com/teams/manchester-united/tab/matches/")

### Season 2021-2022

matchResult = []
matchList = driver.find_elements_by_xpath('//*[@id="pageContent"]/div[2]/table/tbody/tr/td[3]/span')
for entry in matchList:
    matchResult.append(entry.text)

matchName = []
matchList = driver.find_elements_by_xpath('//*[@id="pageContent"]/div[2]/table/tbody/tr/td[2]/a')
for entry in matchList:
    matchName.append(entry.text)

matchScore = []
matchList = driver.find_elements_by_xpath('//*[@id="pageContent"]/div[2]/table/tbody/tr/td[4]')
for entry in matchList:
    matchScore.append(entry.text)

matchHA = []
matchCompetitor = []
for match in matchName:
    if (str(match)[0:17] == 'Manchester United'):
        matchHA.append('H')
        matchCompetitor.append(match[20: len(match)])
    else:
        matchHA.append('A')
        matchCompetitor.append(match[0: len(match) - 1 - 19])

df = pd.DataFrame({'Match':matchName,
                    'Result':matchResult,
                    'Score': matchScore,
                    'Home-Away': matchHA,
                    'Competitor': matchCompetitor})

df.to_excel('data.xlsx', sheet_name='season21_22')

print('Done!')

driver.close()