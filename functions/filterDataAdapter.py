from functions import filterData, fakingData


def filterTeamDataAdapter():
    return filterData.filterTeamData(fakingData.getRecentUserInput(), "mostRecentTableQuery.csv")


def getHeadingsAdapter():
    return filterData.getHeadings("headingsStub.csv")


getHeadingsAdapter()
