from requests import request
import json 

league_id = 3456
url = f"https://api-football-v1.p.rapidapi.com/v2/leagueTable/{league_id}"
headers = {
	'X-RapidAPI-Key': 'cb48fb052bmsh28f4de03a3a4eacp18fce0jsn75c3a47db615'
}

response =  request('GET',url, headers = headers).text
data = json.loads(response)
trace = data["api"]['standings'][0]
league_size = len(trace)
for i in range(league_size):
	print(f"{trace[i]['rank']} - {trace[i]['teamName']}")