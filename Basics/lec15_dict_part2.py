from loguru import logger

labour_with_cost = {"Mahesh":500, "Ramesh":400, 
                    "Mithilesh":400, "Sumesh":300, 
                    "Jagmohan":1000, "Rampyare":800}

#Get Method
print(labour_with_cost.get("Mahesh"))
print(labour_with_cost.get("Mahesh1"))

#Keys and values
print(labour_with_cost.keys())
print(labour_with_cost.values())

#Item Method
print(labour_with_cost.items())

#Update Method
labour_with_cost.update({"manish":700,"Ram":800})
new_dict = {"manish":700,"Ram":800}
final_dict = {**labour_with_cost, **new_dict}
print(final_dict)

#Pop Method
# print(labour_with_cost.pop("Mahesh"))
# print(labour_with_cost.popitem())
# print(labour_with_cost.popitem())
# print(labour_with_cost.keys())

#Copy Method
new_labour_cost = labour_with_cost.copy()
print(id(new_labour_cost))
print(id(labour_with_cost))

#Clear Method
# labour_with_cost.clear()
# print(labour_with_cost)

#Dictionary Comprehension
labour_with_cost = {key:labour_with_cost.get(key) + 100
                    for key in labour_with_cost}

print(labour_with_cost)

labour_with_cost = {key: labour_with_cost.get(key) + 100 if key != "Jagmohan"
                    else labour_with_cost.get(key)
                    for key in labour_with_cost}

print(labour_with_cost)


#Example - Each charcter in given str
name = 'Satlaj'
letter_count = {}
for char in name:
    if char in letter_count:
        letter_count[char] += 1
    else:
        letter_count[char] = 1
    print(letter_count)