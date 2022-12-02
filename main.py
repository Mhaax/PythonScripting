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


def main():
    print("Welcome to our Python Scripting project! What data would you like to see?")
    print("1. Players Points goals per time played")
    print("2. ...")
    print("3. ...")
    print("4. ...")
    print("5. ...")
    print("6. Exit")
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
        exit()
    else :
        print('\n')
        print("Invalid choice")
        main()


main()

