# Individual Testing Submission:

This project takes in data from a CSV file which contains a fictional football league table. This data includes: Team, Position, Games Played, Wins, Draws, Losses, Goals Scored, Goals Conceded.
This data is read into the project and filtered via a user input on Team Name. From there the data is manipulated to calculate a points total (3 points for a win, 1 for a draw) and calculate goal difference. The end statistics are then formatted and printed to the screen.

# How to Run the Project:

To run this project, simply run the file [main](functions/Main.py)


# Data Load File:

- [teamTable](resources/TeamTable.csv) acts as our external call. This is in place of a database which would essentially act as our "live" data that we would pull into the file. Doubling for this file is in the form of repeat .csv's but are intended to show the logic of how doubling would operate had we used live external data. So assume this is a live external DB.
  

- [readCSV](functions/ReadCSV.py)

# Functions To Be Doubled:

- [readCSV](functions/ReadCSV.py)
- [goalDifference](functions/GoalDifference.py)
- [pointsCalculator](functions/PointsCalculator.py)
- [filterData / getHeadings](functions/FilterData.py)
- [searchTeam](functions/SearchTeam.py)

# Link to Unit Tests:

- [tests](tests)

# Important Examples

- Adapter: adapted both functions within [filterData](functions/FilterData.py) within [filterDataAdapter](functions/FilterDataAdapter.py) so that the two functions do not call [teamTable](resources/TeamTable.csv) and instead call doubling files.
  

- Faking: created write to file and read from file methods within [fakingData](functions/FakingData.py) which writes most recent input and file from within [filterData](functions/ReadCSV.py). Essentially, they capture the most recent user input, and most recent file query within the files: [mostRecentTableQuery](resources/MostRecentTableQuery.csv), [mostRecentUserInput](resources/MostRecentUserInput.txt). These are used to fake user inputs and the call to [teamTable](resources/TeamTable.csv).


    Faking Tests 


[test_inputNameEqualsOutputName/ test_lenListEqualLenHeadings](tests/TestFilterData.py)

[test_fileData (GoalDifference)](tests/TestGoalDifferenceCalculator.py)

[test_fileData (PointsCalculator)](tests/TestPointsCalculator.py)



- Stub: 
  
1 - [getHeadings](functions/FilterData.py) calls the [teamTable](resources/TeamTable.csv) to retrieve the headings. To double this, [headingsStub](resources/HeadingsStub.csv) is passed to the [getHeadingsAdapter](functions/FilterDataAdapter.py) which allows the code to run without calling [teamTable](resources/TeamTable.csv). 


    Stub (1) Tests
[test_lenListEqualLenHeadings/ test_returnHeadingsValues](tests/TestFilterData.py)


2 - [GoalDifference](functions/GoalDifference.py) and [PointsCalculator](functions/PointsCalculator.py) both use data from [TeamTable](resources/TeamTable.csv). For testing, this data is changed to implement hard coded data and the faking files from earlier.


    Stub (2/3) Tests
[TestGoalDifferenceCalculator](tests/TestGoalDifferenceCalculator.py)
[TestPointsCalculator](tests/TestPointsCalculator.py)


- Mocks: [SearchTeam](functions/SearchTeam.py) asks for a user input which sets the value for what team we want to search for. For testing we use mocks to set the return value of these functions.


    Mock Tests


[test_errorHandlingTeamName/ test_cantReturnHeadings](tests/TestFilterData.py)
[TestSearchTeam](tests/TestSearchTeam.py)
