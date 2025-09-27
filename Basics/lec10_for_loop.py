from loguru import logger

#Single Dimensional List
labour_name = ["Mahesh","Ramesh","Mithilesh","Sumesh"]

#Accessing element using loop from list
for name in range(len(labour_name)):
    logger.info(f"Labour {name+1} is {labour_name[name]}.")

#Example - WAP to print the first 50th even number.
for number in range(51):
    if number % 2 == 0:
        logger.info(number)