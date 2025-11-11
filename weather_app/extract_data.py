import requests
import pandas as pd


städer = {
    "stockholm": {"latitude": "59.3",
                "longitude": "18.02"},
    "göteborg": {"latitude": "57.70",
                "longitude": "11.97"},
    "malmö": {"latitude": "59.33",
                "longitude": "11.07"}
}
headers = {
    "Accept": "application/json"
}

def get_weather_data(city):

    try:
        url = f"https://opendata-download-metfcst.smhi.se/api/category/pmp3g/version/2/geotype/point/lon/{städer[city]["longitude"]}/lat/{städer[city]["latitude"]}/data.json"
        r = requests.get(url= url, headers= headers)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP-fel: {e}")
    except requests.exceptions.ConnectionError:
        print("Kunde inte ansluta till servern")
    except requests.exceptions.RequestException as e:
        print(f"Ett oväntat fel inträffade: {e}")
    
    return None 

    
def create_dict(stad):
    data = get_weather_data(stad)
    degree_data = []
    time_data = []

    for time in data["timeSeries"]:
        for x in time["parameters"]:
            
            if x["name"] == "t":
                time_data.append(time["validTime"])
                degree_data.append(x["values"][0])
    
  
    dict_test = {
        "time": time_data[0:24],
        "degree": degree_data[0:24]
    }

    return pd.DataFrame(dict_test)

