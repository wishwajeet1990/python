import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import numpy as np

data  = pd.read_csv(r"E:\Training\Python\Codding\Pandas Library\adult.csv")
# print(data)
# print("Top 10 Row of the data set")
# print(data.head(10))
# print("Tail 10 Row of the data set")
# print(data.tail(10))
# print("Shape of the data")
# print("Row :- ",data.shape[0])
# print("Colomn:- ",data.shape[1])
# print("Coloumn name ")
# print(data.columns)
# print("Describe the information about our data set")
# print(data.info())
# print("Get 50% random of Data set")
# print(data.sample(frac=0.0001, random_state=100))       #if we remove random_state parameter from the sample method then it will produce the same as preduced the previous one
#                                                         #else generate random sample from the dataset.
#                                                         #the first parameter frac= produe the %age of the sample 
# print("Print the is null value")
# print(data[data.isnull()].count())
# print("Print the is null value using sum function")
# print(data[data.isnull()].sum(axis=0))
# print("Using Visualization tool ")
# print(data['age'].isnull())
# print(data.columns)
# sns.heatmap(data.isnull())
# plt.show()
print("Check ? in data")
print(data.isin(["?"]).sum())
data["workclass"] = data['workclass'].replace("?",np.nan)
data["occupation"] = data['occupation'].replace("?",np.nan)
data["native-country"] = data['native-country'].replace("?",np.nan)
print("Now check again")
print(data.isin(["?"]).sum())