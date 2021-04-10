from functions import FilterData, GoalDifference, PointsCalculator


def displayData(team):
    data = FilterData.filterTeamData(team)
    headings = FilterData.getHeadings()
    for index, element in enumerate(data):
        print(headings[index], ": ", data[index])
    print(GoalDifference.goalDifferenceCalculator(data[6], data[7]))
    print(PointsCalculator.pointsCalculator(data[3], data[4]))
