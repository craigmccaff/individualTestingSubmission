def setSearchTeam():
    return input("What team would you like to search for?  (red, blue, yellow, green, orange, purple):  ")

def formattedSearchTeam():
    formattedSearch = setSearchTeam().lower()
    return formattedSearch
