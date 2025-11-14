from extract_data import create_dict
from unittest.mock import patch

# fakedata to run a unit test for the function.
def test_length():
    """Create fajk data to do unitetest. it will simulate what the api request get.
    This will make sure that api request is not use when running the test"""
    fake_data = {
        "timeSeries": [
            {
                "validTime": f"2025-11-10T{i:02d}:00:00Z",
                "parameters": [{"name": "t", "values": [i]}]
            }
            for i in range(17)
        ]
    }

    # mockar bort externa data och matar funktioinen med kontrollerad testdata. create_dict testas i isolerad miljö utan att göra
    # riktigt API-request.
    with patch("extract_data.get_weather_data", return_value=fake_data):
        
        df = create_dict("stockholm")
        
        assert len(df) == 24
        assert list(df.columns) == ["time", "degree"]