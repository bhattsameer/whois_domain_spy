# Adjustments to repo to migrate from Python 2 to Python 3
# Primary documentation is in README.md. Additional, specific program notes are here.
#
#  TODO: File outpts only disclaimer. Need to better frame the desired output in athe file.



import urllib.request
import json


Api_url = "http://whoiz.herokuapp.com/lookup.json?url="
url = input("Enter website example: google.com  => ")

f = open("whois_output.txt","w")

json_data = urllib.request.urlopen(Api_url+url)

data = json.load(json_data)
f.write(data['disclaimer']+"\n\n")
print("done , SEE Whois_output.text file")
f.close()
    
