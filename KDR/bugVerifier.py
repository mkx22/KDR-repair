import csv
import sys

def doSave(fileName, res):
    with open(fileName, 'w') as csvfile:
        spamwriter = csv.writer(csvfile)
        spamwriter.writerows(res)

def readCSV(fileName):
    res = []
    with open(fileName) as csvfile:
        spamreader = csv.reader(csvfile)
        count = 0
        for row in spamreader:
            res.append(row)
    return res

def interpretInt(ins):
    if ins == "1":
        return "mutex_lock"
    elif ins == "2":
        return "changing operation orders"
    elif ins == "3":
        return "complex fix"
    elif ins == "4":
        return "A"
    elif ins == "5":
        return "changing operation orders"
    elif ins == "6":
        return "changing operation orders"
    elif ins == "7":
        return "changing operation orders"


if __name__ == '__main__':
    fileName = sys.argv[1]
    with open(fileName) as csvfile:
        spamreader = csv.reader(csvfile)
        count = 0
        res = readCSV(fileName)
        for index in range(len(res)):
            row = res[index]
            if count == 0:
                count += 1
                continue
            if row[-1] != "":
                count += 1
                continue
            count += 1
            print("https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id="+row[4])
            tag = raw_input()
            while(tag == "save"):
                if tag == "save":
                    doSave(fileName, res)
                tag = raw_input()
            if tag == "exit":
                doSave(fileName, res)
                break
            row[-1] = tag
