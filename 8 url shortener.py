import requests
import json

linkRequest = {
	"destination": "https://www.facebook.com/mr.lim99",
	"domain": { "fullName": "rebrand.ly" }
}


requestHeaders = {
	"Content-type": "application/json",
	"apikey": "aadb64df3b3743fa817b685ba389246f"
}

r = requests.post("https://api.rebrandly.com/v1/links",
	data = json.dumps(linkRequest),
	headers=requestHeaders)

if (r.status_code == requests.codes.ok):
    link = r.json()
    print(f"Original link: {link['destination']}\nShortUrl: {link['shortUrl']}")
    # print("Long URL was %s, short URL is %s" % (link["destination"], link["shortUrl"]))