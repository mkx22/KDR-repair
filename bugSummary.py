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

def addFixType(sumInfo, fixType):
    if sumInfo.get(fixType) == None:
        sumInfo[fixType] = 1
    else:
        sumInfo[fixType] += 1


if __name__ == '__main__':
    fileName = sys.argv[1]
    repairSum = {}
    repairId={}
    #preprocess data
    summaryInfo = {}
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
            # summary based on type
            #if len(repairType[i][1]) < 2:
                #summaryInfo["others"] += 1
            info = repairType.lower()
            if info.find("unknown") != -1 or info.find("wrong") != -1 or info.find("complex fix") != -1 or info.find("na") != -1:
                continue
            info = info.split("&")
            for fix in info:
                fix = fix.strip()
                if fix.find("lock") != -1 or fix.find("mutex") != -1:
                    addFixType(summaryInfo, "locks")
                elif fix.find("atomic") != -1:
                    addFixType(summaryInfo, "adding atomic instructions")
                elif fix.find("moving code") != -1:
                    addFixType(summaryInfo, "changing operation orders")
                else:
                    addFixType(summaryInfo, fix)

       	repairSum = sorted(repairSum.items(), key = lambda d:len(d[1]), reverse = True)
       	#print(repairSum[0])


        for i in summaryInfo:
            print(i, summaryInfo[i])

        csvfile = open('csv.csv', 'wb')
        writer = csv.writer(csvfile)
        writer.writerow(['Fix', 'Num', 'Indic'])
        otherCount = 0
        for i in summaryInfo:
            if summaryInfo[i] < 2:
                otherCount += summaryInfo[i]
                continue
            writer.writerow([i, summaryInfo[i]])
        writer.writerow(["Other", otherCount])


        '''
        for i in range(len(repairSum)):
            writer.writerow([repairSum[i][0], str(len(repairSum[i][1])), str(repairSum[i][1])])
        '''
