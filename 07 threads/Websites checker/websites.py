<<<<<<< HEAD

from operator import index


class Websites:
    def __init__(self, filename):
        self.filename = filename
        self.fileList = [] #lista słowników
        self.reportList = []
        self.index = 0
        self.loadFile(filename)

    def loadFile(self, filename):
        fh = open(filename, "r")
        dataList = fh.readlines()

        for v in dataList:
            v = "https://" + v.strip()
            data = { "websites" : v, "Status code" : -1}
            self.fileList.append(data)
            data["index"] = len(self.fileList) - 1
            #print(data)

    def getNextWebsiteToCheck(self):
        if self.index >= len(self.fileList):
            return None

        data = self.fileList[self.index]
        self.index += 1
        
        return data

    def putWebsiteData(self, data):
        if "index" in data and "website" in data and "statusCode" in data:
            self.reportList.append(data)
        else:
            print("Bad keys in report: " + str(data))


    def saveReport(self):
        fh = open("report.txt", "w")

        for el in self.reportList:
            print(el)
            fh.write( str(el["website"]) + " - " + str(el) + " \n")

        fh.close()
        print("Report saved")
=======

from operator import index


class Websites:
    def __init__(self, filename):
        self.filename = filename
        self.fileList = [] #lista słowników
        self.reportList = []
        self.index = 0
        self.loadFile(filename)

    def loadFile(self, filename):
        fh = open(filename, "r")
        dataList = fh.readlines()

        for v in dataList:
            v = "https://" + v.strip()
            data = { "websites" : v, "Status code" : -1}
            self.fileList.append(data)
            data["index"] = len(self.fileList) - 1
            #print(data)

    def getNextWebsiteToCheck(self):
        if self.index >= len(self.fileList):
            return None

        data = self.fileList[self.index]
        self.index += 1
        
        return data

    def putWebsiteData(self, data):
        if "index" in data and "website" in data and "statusCode" in data:
            self.reportList.append(data)
        else:
            print("Bad keys in report: " + str(data))


    def saveReport(self):
        fh = open("report.txt", "w")

        for el in self.reportList:
            print(el)
            fh.write( str(el["website"]) + " - " + str(el) + " \n")

        fh.close()
        print("Report saved")
>>>>>>> d4f06d970b4d665710026f2d53dde28fad90b685
