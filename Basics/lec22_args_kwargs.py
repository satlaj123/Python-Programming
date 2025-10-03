from loguru import logger

#Args
def final_cart_amount(*args, discount):
    result = 0
    for amount in args:
        result += amount
    amount_after_discount = result - (result * discount)
    return amount_after_discount
    
final_amount_to_be_paid = final_cart_amount(100,500,120,300,500,discount=0.5)
logger.info(final_amount_to_be_paid)

#Kwargs
# Function using **kwargs
def print_student_details(**kwargs):
    print("Received keyword arguments as a dictionary:", kwargs)
    
    # Accessing values
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Calling the function with keyword arguments
print_student_details(name="Amit", age=22, course="Data Engineering", city="Bangalore")

print("\nAnother example:")
print_student_details(name="Sneha", age=25, course="Python", grade="A")
