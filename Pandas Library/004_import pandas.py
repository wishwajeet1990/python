import pandas as pd

#read CSV file using pandas library into dataframe
# from csv import DictReader 
#pandas has a special method to read the csv file called pandas.read_csv()

pd_dataframe = pd.read_csv(r"E:\Training\Python\Codding\Pandas Library\nyc_weather.csv")

# Read CSV Using python library itself
# data = open(r"E:\Training\Python\Codding\Pandas Library\nyc_weather.csv","r")
# my_data = DictReader(data)
# for cdata in my_data:
    # print(cdata)

# print(pd_dataframe.head())
print(pd_dataframe)