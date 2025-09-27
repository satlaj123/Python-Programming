from loguru import logger

#Single Dimensional List
labour_name = ["Mahesh","Ramesh","Mithilesh","Sumesh"]

#Access element from list at given index
logger.info(f"First Element in the list is {labour_name[0]}.")

#Append Method
labour_name.append("Ram")
labour_name.append("Mohan")

#Insert Method
labour_name.insert(0,"Ram")
labour_name.insert(1,"Mohan")

#Extend Method
new_labour = ["Ram","Mohan"]
labour_name.extend(new_labour)

logger.info(f"Element present in list is {labour_name}")

#Multi-Dimensional List
labour_wiht_wage = [["Ram",500],["Shyam",400]]

logger.info(f"Labour {labour_wiht_wage[0][0]} is charging total of {labour_wiht_wage[0][1]} per day.")
