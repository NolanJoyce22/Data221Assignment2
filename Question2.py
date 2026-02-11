import string
from collections import Counter
with open("sample-file.txt", "r") as file:
    text = file.read()
# Open the file in read mode

tokens = text.split()
# Splits the file into tokens

clean_tokens = []
# Create a list to store the final tokens

for token in tokens:
    token = token.lower()
    token = token.strip(string.punctuation)
# Remove the punctuation from the tokens

    if sum(char.isalpha() for char in token) >= 2:
        clean_tokens.append(token)
# Check if each character is alphabetic using .isalpha() method and checks if each token has a length greater than 2,
# and if so append the token to the clean_tokens list

list_of_bigrams = []
#Create anew list to store the bigrams

for i in range(len(clean_tokens)-1):
    bigram = (clean_tokens[i], clean_tokens[i+1])
    list_of_bigrams.append(bigram)
# Loop through the list of clean tokens and created the bigrams by collected consecutive words


bigram_counts = Counter(list_of_bigrams)
# Create key-value pairs of unique elements and how many times each appears in the list

most_frequent_5_bigrams = bigram_counts.most_common(5)
# Collect the most frequently occurring 5 bigrams

for (word1, word2), count in most_frequent_5_bigrams:
    print(f"{word1} {word2} -> {count}")
# Print the bigrams and their frequency


