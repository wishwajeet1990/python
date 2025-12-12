import pandas as pd

csv_data = pd.read_csv(r"E:\Training\Python\Codding\Pandas Library\nyc_weather.csv")
print(csv_data["Temperature"])