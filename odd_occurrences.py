# Write a program that prints all elements from a given sequence of words that occur an odd number of times (case-insensitive) in it.
# •	Words are given on a single line, space-separated.
# •	Print the result elements in lowercase, in their order of appearance.


words = input().split()
words = [word.lower() for word in words]
occurrences = {}

# Count occurrences
for word in words:
    if word in occurrences:
        occurrences[word] += 1
    else:
        occurrences[word] = 1

# Print words with odd occurrences
odd_words = []
for word in words:  # Using original order from input
    if occurrences[word] % 2 != 0 and word not in odd_words:
        odd_words.append(word)

print(" ".join(odd_words))
