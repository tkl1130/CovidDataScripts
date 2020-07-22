import json
import sys
import requests
# simple script to call the State of Indiana API to retreive information
#script is to play around and test calling of API through Python
Baseurl ='https://hub.mph.in.gov/api/3/action/'
#display relevant info
#ListPackages='package_list'
#response = requests.get(Baseurl+ListPackages)
#response.raise_for_status()
#ListGroups='group_list'
#response = requests.get(Baseurl+ListGroups)
#response.raise_for_status()
# Load JSON data into a Python variable.
#RetrieveData = json.loads(response.text)
ListCovidCaseData='package_show?id=covid-19-case-data'
response = requests.get(Baseurl+ListCovidCaseData)
response.raise_for_status()
RetrieveData = json.loads(response.text)
resourcesURL = RetrieveData["result"]["resources"]
FileURL = resourcesURL[0]["url"]
print(FileURL)

