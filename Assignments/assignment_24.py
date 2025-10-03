#WAP to read the data from config file and calculate the cost of books for each student.
from loguru import logger
import configparser

config=configparser.ConfigParser()
config.read(r"C:\Users\samit\Desktop\Python Promgramming\files\config_file.ini")

student_details={1:["Math","History"],2:["Biology","Chemistry","History"],3:["science"]}

logger.info(student_details)

cost_per_student={}
total_cost=0
for student,subject in student_details.items():
    student_cost=0
    for sub in subject:
        student_cost=student_cost+int(config["book_cost"][sub.lower()])
    cost_per_student[student] = student_cost
    total_cost=total_cost+student_cost
logger.info(cost_per_student)