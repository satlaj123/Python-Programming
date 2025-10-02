from loguru import logger

#Assigning Tuple variables
test_tupple = (1,2,45,65,32,"True",2,"Manish",True,2)

#Type Method
logger.info(type(test_tupple))

#Len Method
logger.info(len(test_tupple))

#Index Method -> to find first occurance of given element in tupple
logger.info(test_tupple.index(2))

#Count Method
logger.info(test_tupple.count(2))

