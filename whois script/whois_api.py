import urllib2
import json


Api_url = "http://whoiz.herokuapp.com/lookup.json?url="
url = raw_input("Enter website example: google.com  => ")

f = open("whois_output.txt","w")

json_data = urllib2.urlopen(Api_url+url)

data = json.load(json_data)
f.write(data['disclaimer']+"\n\n")
print("done , SEE Whois_output.text file")
f.close()
    
