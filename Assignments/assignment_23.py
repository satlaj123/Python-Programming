from loguru import logger

class EmptyFileException(Exception):
    """Custom exception for empty files."""
    pass

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().strip()  # Read content and remove leading/trailing whitespace
            if not content:
                raise EmptyFileException(f"The file '{filename}' is empty.")
            else:
                names = content.split()  # Split by whitespace to get individual names
                unique_names = set(names)  # Use a set to store unique names
                logger.info(f"Unique names in '{filename}':")
                for name in unique_names:
                    logger.info(name)
    except FileNotFoundError:
        logger.info(f"Error: The file '{filename}' was not found.")
    except EmptyFileException as e:
        logger.info(f"Error: {e}")
    except Exception as e:
        logger.info(f"An unexpected error occurred: {e}")

process_file(r"C:\Users\samit\Desktop\Python Promgramming\files\my_data.txt")

