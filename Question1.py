import string
from collections import Counter
with open("sample-file.txt", "r") as file:
    text = file.read()
# Open the file in read mode
tokens = text.split()
# Splits the file into tokens

complete_tokens = []
# Create a list to store the final tokens

for token in tokens:
    token = token.lower()
    token = token.strip(string.punctuation)
# Remove the punctuation from the tokens

    if sum(char.isalpha() for char in token) >= 2:
        complete_tokens.append(token)
# Check if each character is alphabetic using .isalpha() method and checks if each token has a length greater than 2, and if so append the token to the
# complete_tokens list

token_counts = Counter(complete_tokens)
# Count the number of tokens in the list

top_10_most_frequent_tokens = token_counts.most_common(10)
# Find the most frequently occurring tokens
for word, count in top_10_most_frequent_tokens:
    print(f"{word} -> {count}")
# Print the top ten most occurring words and the number of times they occur

file.close()
