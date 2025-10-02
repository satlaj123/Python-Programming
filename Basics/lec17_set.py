from loguru import logger

#Assignment of set variable
set_variable = {1,2,7,8,4,12}
new_set_variable = {2,4,6,5,15}

#Union Method
logger.info(set_variable.union(new_set_variable))

#Intersection Method
logger.info(set_variable.intersection(new_set_variable))

#Disjoint Method
logger.info(set_variable.isdisjoint(new_set_variable))

#Add Method
set_variable.add(45)
new_set_variable.add(45)
logger.info(set_variable)
logger.info(new_set_variable)

#Remove Method
set_variable.remove(45)
new_set_variable.remove(45)
logger.info(set_variable)
logger.info(new_set_variable)