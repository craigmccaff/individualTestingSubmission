import filterData, fakingData


def filterDataAdapter():
    filterData.filterData(fakingData.getRecentUserInput(), "mostRecentTableQuery.csv")


def getHeadingsAdapter():
    filterData.getHeadings("mostRecentTableQuery.csv")

