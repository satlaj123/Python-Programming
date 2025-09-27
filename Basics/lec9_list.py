from loguru import logger

#Single Dimensional List
labour_name = ["Mahesh","Ramesh","Mithilesh","Sumesh", 500, 400, 400, 300]

new_labour = ["Ram","Mohan"]

#Append Method
labour_name.append(new_labour)

#Concatenation of lists
labour_name = labour_name + new_labour
print(labour_name)

#Accessing list using slicing method
print(labour_name[0:2])

#Length Method
print(len(labour_name))

#Pop Method -> delete the last element from the stack/queue.
wage = labour_name.pop()
print(wage)

#Split Method
api_endpoint = "https://medium.com/nerd-for-tech/understanding-acid-properties-in-database-management-98243bfe244c"
new_api_list = api_endpoint.split("/")
print(new_api_list)

# logger.info(f"Resultant List is {labour_name}")
