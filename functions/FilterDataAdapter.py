from functions import FilterData, FakingData


def filterTeamDataAdapter():
    return FilterData.filterTeamData(FakingData.getRecentUserInput(), "MostRecentTableQuery.csv")


def getHeadingsAdapter():
    return FilterData.getHeadings("HeadingsStub.csv")


getHeadingsAdapter()
