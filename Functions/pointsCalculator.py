def pointsCalculator(teamData):
    wins = int(teamData[3])
    draws = int(teamData[4])
    points = (wins*3) + draws
    result = "Points Total: " + str(points)
    return result
