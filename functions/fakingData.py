import csv


def writeToCSV(data):
    with open("../resources/mostRecentTableQuery.csv", 'w', newline='') as fakingTable:
        writer = csv.writer(fakingTable)
        writer.writerows(data)


def writeRecentUserInput(teamName):
    with open("../resources/mostRecentUserInput.txt", 'w') as fakingInput:
        fakingInput.write(teamName)


def getRecentUserInput():
    with open("../resources/mostRecentUserInput.txt", 'r') as fakingInput:
        result = fakingInput.readline()
        return result

