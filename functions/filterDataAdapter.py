from functions import filterData, fakingData


def filterDataAdapter():
    return filterData.filterData(fakingData.getRecentUserInput(), "mostRecentTableQuery.csv")


def getHeadingsAdapter():
    return filterData.getHeadings("headingsStub.csv")


getHeadingsAdapter()
