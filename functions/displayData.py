from functions import filterData, goalDifference, pointsCalculator


def displayData(team):
    data = filterData.filterTeamData(team)
    headings = filterData.getHeadings()
    for index, element in enumerate(data):
        print(headings[index], ": ", data[index])
    print(goalDifference.goalDifferenceCalculator(data[6], data[7]))
    print(pointsCalculator.pointsCalculator(data[3], data[4]))
