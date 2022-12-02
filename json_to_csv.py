import json
import pandas as pd

def json_to_csv_Player():
    #Get the data from the json file
    with open('playerData.json') as f:
        data = json.load(f)
    #get every data of the json file with first element called index
    df = pd.DataFrame.from_dict(data, orient='index')
    #save the data in a csv file
    df.to_csv('playerData.csv')
    return

def json_to_csv_Team():
    #Get the data from the json file
    with open('teamData.json') as f:
        data = json.load(f)
    #get every data of the json file with first element called index
    df = pd.DataFrame.from_dict(data, orient='index')
    #save the data in a csv file
    df.to_csv('teamData.csv')
    return

json_to_csv_Player()
json_to_csv_Team()