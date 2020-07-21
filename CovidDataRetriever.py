import json
import sys
import requests
Baseurl ='https://hub.mph.in.gov/api/3/action/'
#display relevant info
ListPackages='package_list'
response = requests.get(Baseurl+ListPackages)
response.raise_for_status()
ListGroups='group_list'
response = requests.get(Baseurl+ListGroups)
response.raise_for_status()
# Load JSON data into a Python variable.
RetrieveData = json.loads(response.text)
print(RetrieveData)
#print covid case data
ListCovidCaseData='package_show?id=covid-19-case-data'
response = requests.get(Baseurl+ListCovidCaseData)
response.raise_for_status()
RetrieveData = json.loads(response.text)
print(RetrieveData)
#print details of covid packages
#print(" ")
#w = weatherData['weather']
#print(w)
#print (weatherDict)
# Print weather descriptions.
#w = weatherData['weather']
#print (w)
#print('Current weather in %s:' % (location))
#print([w]['main'], '-', w[0]['weather'][0]['description'])
