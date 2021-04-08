import readCSV, searchTeam

def filterData():
    teamName = searchTeam.formattedSearchTeam()
    table = readCSV.getData()
    flag = True

    while flag:
        for data in table:
            if data[0] == teamName:
                return data
        print("Team name not found. Please enter: red, blue, yellow, green, orange, purple")
        teamName = searchTeam.formattedSearchTeam()

def getHeadings():
    return readCSV.getData()[0]

