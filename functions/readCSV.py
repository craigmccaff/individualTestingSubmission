import csv


def getData():
    dataList = []
    with open("../resources/teamTable.csv") as CSVData:
        fileReader = csv.reader(CSVData)
        for row in fileReader:
            dataList.append(row)
    return dataList
