# using dictionaries and dictionary comprehension
# Write a program that receives info from the console about people and their phone numbers.
# Each entry should have a name and a number (both strings) separated by a "-".
# If you receive a name that already exists in the phonebook, update its number.
# After filling out the phonebook, you will receive a number – N.
# Your program should be able to perform a search of contact by name and
# print its details in the format: "{name} -> {number}".
# In case the contact isn't found, print: "Contact {name} does not exist."


phonebook = {}

while True:
    entry = input()
    if entry.isdigit():
        n = int(entry)
        break

    name, number = entry.split("-")
    phonebook[name] = number

for _ in range(n):
    search_name = input()
    if search_name in phonebook:
        print(f"{search_name} -> {phonebook[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")
