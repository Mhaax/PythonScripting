from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
import time

#function to get current season nba team stats
def get_nba_stats():
    driver = webdriver.Chrome()
    driver.get("https://www.nba.com/stats/teams/traditional")
    
    # Get the table
    table = driver.find_element("xpath", '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table')
    # Get the rows
    rows = table.find_elements("tag name", "tr")
    # Get the columns
    columns = table.find_elements("tag name", "td")
    # Store the data
    data = [[]]
    for i in range(len(columns)):
        if i % 28 == 0:
            data.append([])
        data[-1].append(columns[i].text)
    data.pop(0)
    

    # Close the driver
    driver.close()
    return data


#function to get current season nba player stats
def getPlayerStats():
    driver = webdriver.Chrome()
    driver.get("https://www.nba.com/stats/leaders")
    #decline cookies
    decline=driver.find_element("id","onetrust-reject-all-handler")
    decline.click()
    data = [[]]
    time.sleep(2)
    #get the next page button
    button=driver.find_element("xpath",'/html/body/div/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[5]/button[2]')
    #do the operation as much as necessary until you get all players data
    while button.is_enabled():
        # Get the table
        table = driver.find_element("xpath", '/html/body/div/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[3]/table')
        # Get the rows
        rows = table.find_elements("tag name", "tr")
        # Get the columns
        columns = table.find_elements("tag name", "td")
        # Store the data
        
        for i in range(len(columns)):
            if i % 23 == 0:
                data.append([])
            data[-1].append(columns[i].text)

        data.pop(0)
        button.click()

    # Close the driver
    driver.close()

    return data

#get nba team stats
teamData=get_nba_stats()

teamDataJson={}
j= -1
for i in teamData:
    j+=1
    #organize team data for json
    teamDataJson[j]={"Team":i[1],"GP":i[2],"W":i[3],"L":i[4],"W_PCT":i[5],"MIN":i[6],"PTS":i[7],"FGM":i[8],"FGA":i[9],"FG_PCT":i[10],"3PM":i[11],"3PA":i[12],"3P_PCT":i[13],"FTM":i[14],"FTA":i[15],"FT_PCT":i[16],"OREB":i[17],"DREB":i[18],"REB":i[19],"AST":i[20],"TOV":i[21],"STL":i[22],"BLK":i[23],"BLKA":i[24],"PF":i[25],"PFD":i[26],"PLUS_MINUS":i[27]
    }

#save in json
with open('teamData.json', 'w') as f:
    json.dump(teamDataJson, f)

print("Team Data Done")


#get player data
playerData=getPlayerStats()
playerDataJson={}
j= -1
for i in playerData:
    j+=1
    #organize player data for json
    playerDataJson[j]={"Player":i[1],"Team":i[2],"GP":i[3],"MIN":i[4],"PTS":i[5],"FGM":i[6],"FGA":i[7],"FG_PCT":i[8],"3PM":i[9],"3PA":i[10],"3P_PCT":i[11],"FTM":i[12],"FTA":i[13],"FT_PCT":i[14],"OREB":i[15],"DREB":i[16],"REB":i[17],"AST":i[18],"STL":i[19],"BLK":i[20],"TOV":i[21],"EFF":i[22]
    }
#save in json
with open('playerData.json', 'w') as f:
    json.dump(playerDataJson, f)

print("Player Data Done")