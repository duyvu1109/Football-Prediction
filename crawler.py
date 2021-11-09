from selenium import webdriver
from time import sleep

import pandas as pd
# Open Microsoft Edge 
driver = webdriver.Edge(executable_path='msedgedriver.exe')
driver.get("https://www.11v11.com/teams/manchester-united/tab/matches/")

writer = pd.ExcelWriter('data.xlsx', engine = 'xlsxwriter')

###########################################################################################################################
####################################################season 21-22###########################################################
###########################################################################################################################
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

df1 = pd.DataFrame({'Match':matchName,
                    'Result':matchResult,
                    'Score': matchScore,
                    'Home-Away': matchHA,
                    'Competitor': matchCompetitor})

df1.to_excel(writer, sheet_name='season21_22', index=None)

###########################################################################################################################
####################################################season 20-21###########################################################
###########################################################################################################################
sleep(2)

newSeason = driver.find_element_by_xpath('//*[@id="season"]/li[2]/a')
newSeason.click()

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

df2 = pd.DataFrame({'Match':matchName,
                    'Result':matchResult,
                    'Score': matchScore,
                    'Home-Away': matchHA,
                    'Competitor': matchCompetitor})

df2.to_excel(writer, sheet_name='season20_21', index=None)

###########################################################################################################################
####################################################season 19-20###########################################################
###########################################################################################################################
sleep(2)

newSeason = driver.find_element_by_xpath('//*[@id="season"]/li[3]/a')
newSeason.click()

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

df3 = pd.DataFrame({'Match':matchName,
                    'Result':matchResult,
                    'Score': matchScore,
                    'Home-Away': matchHA,
                    'Competitor': matchCompetitor})

df3.to_excel(writer, sheet_name='season19_20', index=None)

writer.save()
writer.close()

print('Done!')

driver.close()