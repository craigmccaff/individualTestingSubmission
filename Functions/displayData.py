import filterData, goalDifference, pointsCalculator

def displayData():
    data = filterData.filterData()
    headings = filterData.getHeadings()
    for index, element in enumerate(data):
        print(headings[index], ":  ", data[index])
    print(goalDifference.goalDifferenceCalculator(data))
    print(pointsCalculator.pointsCalculator(data))

