def pointsCalculator(wins, draws):
    points = (int(wins)*3) + int(draws)
    result = "Points Total: " + str(points)
    return result
