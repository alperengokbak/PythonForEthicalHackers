myDictionary = {"key": "value"}
print(myDictionary["key"])

myDictionary2 = {"Swim": 100, "Running": 200}
print(myDictionary2["Swim"])
print(myDictionary2["Running"])

#! Key can be integer or string value. It doesn't matter.
myDictionary3 = {10: 1, "key2": 2, "key3": "Apple"}
print(myDictionary3["key3"])
print(myDictionary3[10])

#! We can create a list or different dictionary inside of a dictionary.
myDictionary4 = {"key1": 100, "key2": [10, 20, 30], "key3": {"key4": 5}}
print(myDictionary4["key1"])
print(myDictionary4["key2"])
print(myDictionary4["key3"])
#! We can reach the whole keys and values.
print(myDictionary4.keys())
print(myDictionary4.values())
#! If we want to reach dictionary values, you can write two brackets.
print(myDictionary4["key3"]["key4"])

# ? At the same time, we can change the value and add new keys.
myDictionary5 = {"key1": "value1", "key2": "value2"}
myDictionary5["key1"] = "ChangeableValue"
myDictionary5["key3"] = "Adding Value"
print(myDictionary5)
