# Using dictionaries concepts:
# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"


text = input()
char_counts = {}

for char in text:
    if char != " ":
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1

for char, count in char_counts.items():
    print(f"{char} -> {count}")


