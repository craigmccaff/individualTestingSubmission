from functions import readCSV, searchTeam, fakingData


def filterData(teamName, file = "teamTable.csv"):
    table = readCSV.getData(file)
    fakingData.writeToCSV(table)
    flag = True

    while flag:
        for data in table:
            if data[0] == teamName:
                fakingData.writeRecentUserInput(teamName)
                return data
        print("Team name not found. Please enter: red, blue, yellow, green, orange, purple")
        teamName = searchTeam.formattedSearchTeam()


def getHeadings(file = "mostRecentTableQuery.csv"):
    return readCSV.getData(file)[0]
