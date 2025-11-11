from extract_data import create_dict
from unittest.mock import patch
import pandas as pd

# fajkdata to run a unitetest for the function.
def test_length_return_24():
    """Create fajk data to do unitetest. it will simulate what the api request get.
    This will make sure that api request is not use when running the test"""
    fake_data = {
        "timeSeries": [
            {
                "validTime": f"2025-11-10T{i:02d}:00:00Z",
                "parameters": [{"name": "t", "values": [i]}]
            }
            for i in range(30)
        ]
    }

    with patch("extract_data.get_weather_data", return_value=fake_data):
        df = create_dict("stockholm")
        
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 24
        assert list(df.columns) == ["time", "degree"]