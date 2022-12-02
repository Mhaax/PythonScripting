import os
import json
import pandas as pd
import matplotlib.pyplot as plot

#Get the timePlayed, pointsScored, number of games played for each player
#Displays a plot of the average points scored per time played for each player

def function1():
    #Get the data from the json file
    with open('playerData.json') as f:
        data = json.load(f)

    #Get the timePlayed, pointsScored, number of games played for each player
    timePlayed = []
    pointsScored = []
    gamesPlayed = []

    for player in data:
        timePlayed.append(data[player]['MIN'])
        pointsScored.append(data[player]['PTS'])

        print(data[player])
        print('\n')


    print(timePlayed)
    print('\n')
    print(pointsScored)

    #Plot the average points scored per time played for each player
    plot.plot(timePlayed, pointsScored, 'ro')
    plot.xlabel('Time Played')
    plot.ylabel('Average Points Scored')
    plot.title('Average Points Scored per Time Played')

    #make index ascending
    plot.gca().invert_xaxis()
    plot.gca().invert_yaxis()

    plot.xticks([0,50,100,150,200,250])
    plot.yticks([0,50,100,150,200,250])

    plot.show()

    return


def function2():
    df=pd.read_csv('playerData.csv')
    sns.heatmap(df[['3PM','AST']].corr(method='pearson'),annot=True)
    plot.show()
    return

def function3():
    df=pd.read_csv('playerData.csv')
    
    sns.scatterplot(x="FTM", y="PTS", hue="Team", data=df)
    plot.show()
    return

def function4():
    df=pd.read_csv('teamData.csv')
    sns.jointplot(x="3PM", y="3PA", data=df, kind="kde")
    plot.show()
    return

def function5():
    df=pd.read_csv('playerData.csv')
    sns.kdeplot(x="FGA", y="REB", data=df[df['Team']=='UTA']) #Dunk essayés et Rebond
    #define x axe title as "Dunk essayés"
    plot.xlabel("Dunk essayés")
    #define y axe title as "Rebond"
    plot.ylabel("Rebond")
    plot.show()
    return

def main():
    StillActive = True
    while(StillActive):
        print("\nWelcome to our Python Scripting project! What data would you like to see?")
        print("1. Players Points goals per time played")
        print("2. 3points marqués par équipe en fonction des passes décisives")
        print("3. Points marqués par équipe en fonction des lancers francs marqués")
        print("4. 3points tentés par équipe en fonction des 3points marqués")
        print("5. Rebonds par équipe en fonction des dunks essayés")
        
        print("6. Get Data")
        print("7. Exit")
        choice = input("Enter your choice: ")
        

        if choice == "1":
            print('\n')
            function1()
        elif choice == "2":
            print('\n')
            function2()
        elif choice == "3":
            print('\n')
            function3()
        elif choice == "4":
            print('\n')
            function4()
        elif choice == "5":
            print('\n')
            function5()
        elif choice == "6":
            StillActive = False
        elif choice == "7":
            StillActive = False
        else :
            print('\n')
            print("Invalid choice")
            
main()
