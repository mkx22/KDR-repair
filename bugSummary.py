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
            repairType = row[colIndex].strip()
            while not repairType[-1].isalpha():
                repairType = repairType[:-1]

            num = repairSum.get(repairType)
            listID = int(row[0][1:-1])
            if num:
                repairSum[repairType].append(listID)
            else:
                repairSum[repairType] = [listID]

       	repairSum = sorted(repairSum.items(), key = lambda d:len(d[1]), reverse = True)
       	#print(repairSum[0])
        for i in range(len(repairSum)):
            print(repairSum[i][0] + ": " + str(len(repairSum[i][1])) + ". indices: " + str(repairSum[i][1]))
