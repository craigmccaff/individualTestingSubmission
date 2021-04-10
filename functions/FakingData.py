import csv


def writeToCSV(data):
    with open("../resources/MostRecentTableQuery.csv", 'w', newline='') as fakingTable:
        writer = csv.writer(fakingTable)
        writer.writerows(data)


def writeRecentUserInput(teamName):
    with open("../resources/MostRecentUserInput.txt", 'w') as fakingInput:
        fakingInput.write(teamName)


def getRecentUserInput():
    with open("../resources/MostRecentUserInput.txt", 'r') as fakingInput:
        result = fakingInput.readline()
        return result
