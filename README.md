# Individual Testing Submission:

This project takes in data from a CSV file which contains a fictional football league table. This data includes: Team, Position, Games Played, Wins, Draws, Losses, Goals Scored, Goals Conceded.
This data is read into the project and filtered via a user input on Team Name. From there the data is manipulated to calculate a points total (3 points for a win, 1 for a draw) and calculate goal difference. The end statistics are then formatted and printed to the screen.

# How to Run the Project:

To run this project, simply run the file [main](functions/main.py)


# Data Load File:

- [teamTable](resources/teamTable.csv)
- [readCSV](functions/readCSV.py)

# Functions To Be Doubled:

- [readCSV](functions/readCSV.py)
- [goalDifference](functions/goalDifference.py)
- [pointsCalculator](functions/pointsCalculator.py)
- [filterData / getHeadings](functions/filterData.py)
- [searchTeam](functions/searchTeam.py)

# Link to Unit Tests:

- [tests](tests)

# Important Examples

- Adapter [filterDataAdapter](functions/filterDataAdapter.py)
- Faking [[fakingData](functions/fakingData.py) (features in [readCSV](functions/readCSV.py), [filterDataAdapter](functions/filterDataAdapter.py) and [searchTeam](functions/searchTeam.py)), [mostRecentTableQuery](resources/mostRecentTableQuery.csv), [mostRecentUserInput](resources/mostRecentUserInput.txt)]
