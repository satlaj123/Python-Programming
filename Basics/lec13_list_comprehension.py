#Satandard way to store the value based on codition in new list.
#Task -1 -> Store only even number
new_list = []
for i in range(1,11):
    if i % 2 == 0:
        new_list.append(i)

print(new_list)

#Performaing same task using list_comprehension with only if condition.
#Synatx - [output for loop if condition]
new_list = [i for i in range(1,11) if i % 2 == 0]
print(new_list)

#Task -2 -> Store Odd and Even flag based on number.
new_list = []
for i in range(1,11):
    if i % 2 == 0:
        new_list.append("Even")
    else:
        new_list.append("Odd")

print(new_list)


#Performaing same task using list_comprehension with only if condition.
#Synatx - [output if condition else output for loop]
new_list = ["Even" if i % 2 == 0 else "Odd" for i in range(1,11)]
print(new_list)