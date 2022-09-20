from datetime import datetime
import os, sys
from shutil import ExecError
import urllib.parse
import validators # pip install validators
from pip._vendor import requests
from datetime import datetime

print("Number of arguments: ", len(sys.argv))
print("Arguments list: ", sys.argv)

url = "https://duckduckgo.com"
if len(sys.argv) > 1:
    url = sys.argv[1]

print("Website to download:", url)

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)
print("Current working dir: ", os.getcwd())

if not os.path.exists("./websites"):
    os.mkdir("websites")

parsedUrl = urllib.parse.urlparse(url)
print(parsedUrl)

validFlag = validators.url(url)
if validFlag:
    print("Url: ", url, " is valid")
else:
    print("Url: ", url, " is invalid")
    raise Exception("Bad URL")


response = requests.get(url, allow_redirects = True)
if response.ok == True:
    print("Response ok from server for URL: ", url)
    now = datetime.now()
    dateString = now.strftime("%d.%m.%Y %H:%M:%S")
    print(dateString)
    fileName = "/Python Projects/basics/06 files/websites/" + parsedUrl.netloc + " " + dateString + ".html"
    print(fileName)
    fh = open(fileName, "wb")
    fh.write(response.content)
    fh.close()
