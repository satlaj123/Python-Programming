from loguru import logger
import time

#Single Dimensional List
labour_name = ["Mahesh","Ramesh","Mithilesh","Sumesh"]

name_iter = len(labour_name) - 1
while name_iter >= 0:
    print(labour_name[name_iter])
    time.sleep(5)
    name_iter -= 1