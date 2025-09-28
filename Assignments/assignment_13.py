from loguru import logger

labour_cost = {"Mahesh":500, "Ramesh":400, "Mithilesh":400, "Sumesh":300, "Jagmohan":1000, "Rampyare":800}

total = 0
no_of_days = 50

for cost in labour_cost:
    total += labour_cost[cost]
    
total = (total * no_of_days) - ((7 *(labour_cost['Mahesh'])) + (4 * (labour_cost['Jagmohan'])))
print(total)