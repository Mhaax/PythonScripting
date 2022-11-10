import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json


def get_nba_stats():
    driver = webdriver.Chrome()
    driver.get("https://www.nba.com/stats/teams/traditional")

    # Get the table
    table = driver.find_element("xpath", '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table')
    # Get the rows
    rows = table.find_elements("tag name", "tr")
    # Get the columns
    columns = table.find_elements("tag name", "td")
    # Get the data
    data = [[]]
    for i in range(len(columns)):
        if i % 30 == 0:
            data.append([])
        data[-1].append(columns[i].text)
    data.pop(0)
    

    # Close the driver
    driver.close()
    return data

x=get_nba_stats()
#print(x[0])
y={}
j= -1
for i in x:
    print(i[10])
    j+=1
    y[j]={"Team":i[1],"GP":i[2],"W":i[3],"L":i[4],"W_PCT":i[5],"MIN":i[6],"PTS":i[7],"FGM":i[8],"FGA":i[9],"FG_PCT":i[10],"3PM":i[11],"3PA":i[12],"3P_PCT":i[13],"FTM":i[14],"FTA":i[15],"FT_PCT":i[16],"OREB":i[17],"DREB":i[18],"REB":i[19],"AST":i[20],"TOV":i[21],"STL":i[22],"BLK":i[23],"BLKA":i[24],"PF":i[25],"PFD":i[26],"PLUS_MINUS":i[27]
    }
print(y)
with open('data.json', 'w') as f:
    json.dump(y, f)


