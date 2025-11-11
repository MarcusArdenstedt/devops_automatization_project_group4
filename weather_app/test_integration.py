from extract_data import get_weather_data
import pytest 

# checkking if the api request give some data, and if the function return a dict, then it's okej.
# using decorater pytest.mark.parametrize, first parameter is name, the seconed parameter is the name i will put in, instead of writting three test
# use this.
@pytest.mark.parametrize("stad_input", ["stockholm", "göteborg", "malmö"])
def test_stockholm_api_request(stad_input):
    data = get_weather_data(stad_input)
    
    assert isinstance(data, dict)
   

# checking that it's celsius and the value is a float type the latest 24h.
# using decorater pytest.mark.parametrize, first parameter is name, the seconed parameter is the name i will put in, instead of writting three test
# use this.
@pytest.mark.parametrize("stad_input", ["stockholm", "malmö", "göteborg"])
def test_degree_stockholm(stad_input):
    data = get_weather_data(stad_input)

    for time in data["timeSeries"][:24]:
        for x in time["parameters"]:
            
            if x["name"] == "t":
                assert x["unit"] == "Cel"
                assert isinstance(x["values"][0], float)
               

