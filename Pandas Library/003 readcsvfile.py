import pandas as pd

csv_data = pd.read_csv(r"E:\Training\Python\Codding\Pandas Library\nyc_weather.csv")
print(csv_data["Temperature"])

print("Print Temp greater than 35")
print(csv_data[csv_data["Temperature"]>35])
print("Print Temperature less than 25")
print(csv_data[csv_data["Temperature"]<25])