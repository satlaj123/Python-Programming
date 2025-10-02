from loguru import logger

name = "satlaj thakur"

#Capitalize Method -> Convert first cahr of word to Upper letter and rest to in small.
logger.info(name.capitalize())

#Count Method
logger.info(name.count('a'))

#Ord Method
logger.info(ord('a'))
logger.info(ord('z'))
logger.info(ord('A'))
logger.info(ord('Z'))

#Endswith Method
logger.info(name.endswith('s'))

#Lower & Upper Method
logger.info(name.lower())
logger.info(name.upper())

#Replace Method
new_name = name.replace("satlaj","amit")
logger.info(new_name)

#Split Method
new_name = name.split(" ")
logger.info(new_name)