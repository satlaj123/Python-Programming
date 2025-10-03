from loguru import logger
import configparser

config = configparser.ConfigParser()
config.read(r"C:\Users\samit\Desktop\Python Promgramming\files\config_file.ini")

brick_cost = config["raw_materials"]["brick_cost"]

logger.info(f"{brick_cost}, type of brick_cost {type(brick_cost)}")

def total_no_of_bricks(length, breath, height):
    no_of_bricks_in_length_side = length * (height * 2)
    tota_no_of_bricks_in_length_side = no_of_bricks_in_length_side * 2

    no_of_bricks_in_breath_side = breath * (height * 2)
    tota_no_of_bricks_in_breath_side = no_of_bricks_in_breath_side * 2

    total_no_of_bricks = tota_no_of_bricks_in_length_side + tota_no_of_bricks_in_breath_side

    return total_no_of_bricks

def total_cost_for_bricks(config):
    brick_cost = float(config["raw_materials"]["brick_cost"])
    total_no_of_bricks1 = total_no_of_bricks(15, 15, 10)
    final_cost = brick_cost * total_no_of_bricks1

    return final_cost

result = total_cost_for_bricks(config = config)
logger.info(f"Total bricks cost to make 1 room = {result}")

