# Dictionaries are used to store data values in " key : value " pairs
# A dictionary is a collection which is ordered, changeable and do not allow duplicates

# This is how to make a dictionary
Car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(Car)

# You can access a Value by using the key name
print(Car["brand"]) # Ford

# In Dictionaries Duplicates are not allowed and the newest change is saved

# to get the length of dictionary
print(len(Car))

# Dictionaries can be of any type

# The dict constructor is a kind of short- hand to making dictionaries
thisdict = dict(name = "John", age = 36, country = "Norway")

# use the update method to change a value
thisdict.update({"country" : "Germany"})

# Add items
thisdict["Favcolor"] = "red"

# Remove items
thisdict.pop("name")

# You can copy entire dictionaries 
mydict = thisdict.copy()

# A dictionary can contain dictionaries, this is called nested dictionaries
Employees = {
  "Employee1" : {
    "name" : "Emil",
    "salary" : 20000
  },
  "Employee2" : {
    "name" : "Tobias",
    "salary" : 30000
  },
  "Employee3" : {
    "name" : "Linus",
    "salary" : 54000
  }
}

# you can also create three seperate dictionaries then joing them into one
Customer1 = {
  "name" : "Emil",
  "OrderNumber" : 20000
}

Customer2 = {
  "name" : "Tobias",
  "OrderNumber" : 30000
}
Customer3 = {
  "name" : "Linus",
  "OrderNumber" : 54000
}

MyCustomers = {
    "customer1" : Customer1,
    "customer2" : Customer2,
    "customer3" : Customer3
}