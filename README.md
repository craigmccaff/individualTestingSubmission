# Individual Testing Submission:

This project takes in data from a CSV file which contains a fictional football league table. This data includes: Team, Position, Games Played, Wins, Draws, Losses, Goals Scored, Goals Conceded.
This data is read into the project and filtered via a user input on Team Name. From there the data is manipulated to calculate a points total (3 points for a win, 1 for a draw) and calculate goal difference. The end statistics are then formatted and printed to the screen.

# How to Run the Project:

To run this project, simply run the file [main](functions/main.py)


# Data Load File:

- [teamTable](resources/teamTable.csv) acts as our external call. This is in place of a database which would essentially act as our "live" data that we would pull into the file. Doubling for this file is in the form of repeat .csv's but are intended to show the logic of how doubling would operate had we used live external data. So assume this is a live external DB.
  

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

- Adapter: adapted both functions within [filterData](functions/filterData.py) within [filterDataAdapter](functions/filterDataAdapter.py) so that the two functions do not call [teamTable](resources/teamTable.csv) and instead call doubling files.
  

- Faking: created write to file and read from file methods within [fakingData](functions/fakingData.py) which writes most recent input and file from within [filterData](functions/readCSV.py). Essentially, they capture the most recent user input, and most recent file query within the files: [mostRecentTableQuery](resources/mostRecentTableQuery.csv), [mostRecentUserInput](resources/mostRecentUserInput.txt). These are used to fake user inputs and the call to [teamTable](resources/teamTable.csv). These are then used to test whether the input name matches the output.


Faking Test: [test_inputNameEqualsOutputName](tests/test_filterData.py)
  

- Stub: [getHeadings](functions/filterData.py) calls the [teamTable](resources/teamTable.csv) to retrieve the headings. To double this, [headingsStub](resources/headingsStub.csv) is passed to the [getHeadingsAdapter](functions/filterDataAdapter.py) which allows the code to run without calling [teamTable](resources/teamTable.csv)
