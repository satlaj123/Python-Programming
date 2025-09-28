from loguru import logger

#Creating dictionay
labour_with_cost = {"Mahesh": 500, "Ramesh": 400, "Mithilesh": 400, "Sumesh": 300}

#Updating dict with new values
labour_with_cost["Jagmohan"] = 1000
labour_with_cost["Rampyare"] = 800

#Key Method in dict
logger.info(labour_with_cost.keys())

#Value Method in dict
logger.info(labour_with_cost.values())

#Item Method in dict
logger.info(labour_with_cost.items())

#Dictionary iteration
for name in labour_with_cost:
    logger.info(f"{name}, {labour_with_cost[name]}")

for key, value in labour_with_cost.items():
    logger.info(f"{key}, {value}")

# logger.info(labour_with_cost)