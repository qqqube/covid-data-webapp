import requests


def _get_news():

	url = "https://coronavirus-smartable.p.rapidapi.com/news/v1/US/"
	headers = {
		'x-rapidapi-host': "coronavirus-smartable.p.rapidapi.com",
        'x-rapidapi-key': "f260160c3fmshffa83ddc24b2e03p1705d1jsn1f9b1e03552b"
		}

	response = requests.request("GET", url, headers=headers)
	news_list = response.json()["news"]
	return news_list


def _get_countries():

	url = "https://covid-19-data.p.rapidapi.com/help/countries"

	headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "f260160c3fmshffa83ddc24b2e03p1705d1jsn1f9b1e03552b"
        }
	response = requests.request("GET", url, headers=headers)
	resp_json = response.json()
	countries = [item["name"] for item in resp_json]
	return countries


def _get_totals():

	url = "https://covid-19-data.p.rapidapi.com/totals"
	headers = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': "f260160c3fmshffa83ddc24b2e03p1705d1jsn1f9b1e03552b"
        }
	response = requests.request("GET", url, headers=headers)
	resp_json = response.json()[0]
	confirmed = resp_json["confirmed"]
	recovered = resp_json["recovered"]
	critical = resp_json["critical"]
	deaths = resp_json["deaths"]

	return confirmed, recovered, critical, deaths


def _get_country_stats(country):

	url = "https://covid-19-data.p.rapidapi.com/country"

	querystring = {"name":country}

	headers = {
	    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
	    'x-rapidapi-key': "f260160c3fmshffa83ddc24b2e03p1705d1jsn1f9b1e03552b"
	    }

	response = requests.request("GET", url, headers=headers, params=querystring)
	
	return response.json()




