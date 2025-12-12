import pickle

# Your Python object (you can change this as you want)
my_data = {
    "name": "Wishwajeet Singh Tanwar",
    "age": 34,
    "skills": ["Python", "AI/ML", "Embedded Systems"],
    "married": True
}

# Creating a pickle file
with open("mydata.pkl", "wb") as file:
    pickle.dump(my_data, file)

print("Pickle file 'mydata.pkl' created successfully!")

with open("mydata.pkl","rb") as f:
    data = pickle.load(f)

print(data)
