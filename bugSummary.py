import csv
import sys

def readCSV(fileName):
    res = []
    with open(fileName) as csvfile:
        spamreader = csv.reader(csvfile)
        count = 0
        for row in spamreader:
            res.append(row)
    return res

if __name__ == '__main__':
    fileName = sys.argv[1]
    repairSum = {}
    repairId={}
    with open(fileName) as csvfile:
        spamreader = csv.reader(csvfile)
        count = 0
        res = readCSV(fileName)
        colIndex = 0
        for index in range(len(res)):
            row = res[index]
            if count == 0:
                for r in range(len(row)):
                    if row[r] == "Repair type":
                        colIndex = r
                count += 1
                continue
            if row[colIndex] == "":
                count += 1
                continue
            repairType = row[colIndex]

            num = repairSum.get(repairType)
            if num:
                repairSum[repairType] += 1
            else:
                repairSum[repairType] = 1
        
       	repairSum = sorted(repairSum.items(), key = lambda d:d[1], reverse = True)	
       	#print(repairSum[0])
        for i in range(len(repairSum)):
            print(repairSum[i])
