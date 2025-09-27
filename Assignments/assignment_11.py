# Write a program to insert a number at given index without using any in-built function/method.
from loguru import logger

lst = [202, 165, 89, 76, 12]
number_to_insert = 15

index = 0
for number in lst:
    if number < number_to_insert:
        index = index
        break
    else:
        index = index + 1
lst.append(None)
for i in range(len(lst) - 1, index, -1):
    lst[i] = lst[i-1]
lst[index] = number_to_insert
# print(index)
print(lst)