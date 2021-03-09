#Importing Libraries.
import requests
from bs4 import BeautifulSoup
#It is the url we will use the get information from.
url = "https://www.python.org/jobs"
#We gettind send to url.
r = requests.get(url)
# We are specifying we want to content lxml.
soup = BeautifulSoup(r.content,"lxml")
#We are getting ul from Html which has class pagination.
pages = len(soup.find_all("ul",attrs={"class":"pagination"})[0].find_all("li")) - 2
totalJobs = 0
for pageNumber in range(1,pages + 1):
    pageRequest = requests.get("https://www.python.org/jobs/?page=" + str(pageNumber))
    pageSource = BeautifulSoup(pageRequest.content,"lxml")
    jobs = pageSource.find("div",attrs={"class":"row"}).ol.find_all("li")
    #We have all information about a job. Now get in detail.
    for job in jobs:
        name = job.h2.find("a").text
        location = job.find("span",attrs={"class":"listing-location"}).text
        company = job.find("span",attrs={"class":"listing-company-name"}).br.next.strip()
        publish_time = job.find("time").text
        totalJobs += 1
        print(name,company,location,publish_time,sep="\n")
        print("-"*60)

print("Total {} jobs found.".format(totalJobs))