def goalDifferenceCalculator(teamData):
    goalsFor = teamData[6]
    goalsAgainst = teamData[7]
    goalDifference = int(goalsFor) - int(goalsAgainst)
    result = "Goal Difference:  " + str(goalDifference)
    return result


