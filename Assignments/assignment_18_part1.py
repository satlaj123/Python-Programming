# Swap the case of the string without using swapcase inbuilt methood for string.

Input = "Programming Aasan Hai"
ans = ""
for char in Input:
    if char.isupper() == True:
        ans+=(char.lower())
    else:
        ans+=(char.upper())

print(ans)