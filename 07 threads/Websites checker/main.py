<<<<<<< HEAD
from wsgiref.validate import validator
from websites import *
import os, sys
import threading, time
from pip._vendor import requests
import validators

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

websites = Websites("websites.txt")

#print( websites.getNextWebsiteToCheck() )
#websites.putWebsiteData({"index" : 0, "website": "google.com", "statusCode": 200})
#websites.saveReport()

dataLock = threading.Lock()

class Client(threading.Thread):
    def __init__(self, threadName, websites, sleepTime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.websites = websites
        self.sleepTime = sleepTime

    def run(self):
        while True:
            dataLock.acquire()
            websiteToCheck = self.websites.getNextWebsiteToCheck()
            dataLock.release()

            if not websiteToCheck:
                break
            print(websiteToCheck)
            self.checkUrl(websiteToCheck)
            time.sleep(self.sleepTime)

        print(self.threadName, "ended")

    def checkUrl(self,data):
        try:
            validUrlFlag = validator.url(data["website"])
            if validUrlFlag:
                data["validUrlFlag"] = True
                response = requests.get(data["website"], allow_redirects = True)
                data["statusCode"] = response.status_code
            else:
                data["validUrlFlag"] = False
        except:
            data["exception"] = sys.exc_info()[0]

        dataLock.acquire()
        self.websites.putWebsiteData(data)
        dataLock.release()


numThreads = 10
threadsList = []
num = 0

while num < numThreads:
    t = Client("T" + str(num), websites, 0.1)
    threadsList.append(t)
    t.start()
    num += 1

for t in threadsList:
    t.join()

websites.saveReport()
=======
from wsgiref.validate import validator
from websites import *
import os, sys
import threading, time
from pip._vendor import requests
import validators

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

websites = Websites("websites.txt")

#print( websites.getNextWebsiteToCheck() )
#websites.putWebsiteData({"index" : 0, "website": "google.com", "statusCode": 200})
#websites.saveReport()

dataLock = threading.Lock()

class Client(threading.Thread):
    def __init__(self, threadName, websites, sleepTime):
        threading.Thread.__init__(self)
        self.threadName = threadName
        self.websites = websites
        self.sleepTime = sleepTime

    def run(self):
        while True:
            dataLock.acquire()
            websiteToCheck = self.websites.getNextWebsiteToCheck()
            dataLock.release()

            if not websiteToCheck:
                break
            print(websiteToCheck)
            self.checkUrl(websiteToCheck)
            time.sleep(self.sleepTime)

        print(self.threadName, "ended")

    def checkUrl(self,data):
        try:
            validUrlFlag = validator.url(data["website"])
            if validUrlFlag:
                data["validUrlFlag"] = True
                response = requests.get(data["website"], allow_redirects = True)
                data["statusCode"] = response.status_code
            else:
                data["validUrlFlag"] = False
        except:
            data["exception"] = sys.exc_info()[0]

        dataLock.acquire()
        self.websites.putWebsiteData(data)
        dataLock.release()


numThreads = 10
threadsList = []
num = 0

while num < numThreads:
    t = Client("T" + str(num), websites, 0.1)
    threadsList.append(t)
    t.start()
    num += 1

for t in threadsList:
    t.join()

websites.saveReport()
>>>>>>> d4f06d970b4d665710026f2d53dde28fad90b685
print("Job done!")