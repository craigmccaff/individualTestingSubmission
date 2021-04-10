from functions import ReadCSV, SearchTeam, FakingData


def filterTeamData(teamName, file ="TeamTable.csv"):
    table = ReadCSV.getData(file)
    FakingData.writeToCSV(table)
    flag = True

    while flag:
        for data in table[1:]:
            if data[0] == teamName:
                FakingData.writeRecentUserInput(teamName)
                return data
        print("Team name not found. Please enter: red, blue, yellow, green, orange, purple")
        teamName = SearchTeam.formattedSearchTeam()


def getHeadings(file = "MostRecentTableQuery.csv"):
    return ReadCSV.getData(file)[0]
