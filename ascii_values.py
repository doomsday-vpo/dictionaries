# Write a program that receives a list of characters separated by ", ".
# It should create a dictionary with each character as a key and its ASCII value as a value. Try solving that problem using comprehension.


characters = input().split(", ")
ascii_values = {char: ord(char) for char in characters}

print(ascii_values)