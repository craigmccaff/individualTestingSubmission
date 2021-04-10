import csv


def getData(fileName):
    dataList = []
    with open("../resources/" + fileName) as CSVData:
        fileReader = csv.reader(CSVData)
        for row in fileReader:
            dataList.append(row)
    return dataList
