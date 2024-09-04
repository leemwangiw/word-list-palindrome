import requests

# Step 1: Download the word list
url = "https://public.websites.umich.edu/~jlawler/wordlist"
response = requests.get(url)
word_list = response.text.splitlines()

# Step 2: Create an empty list to hold palindromes
palindromes = []

# Step 3: Loop through each word in the word list with index
for index, word in enumerate(word_list):
    # Check if the word is a palindrome
    if word == word[::-1]:
        # Append the tuple (index, word) to the palindrome list
        palindromes.append((index, word))

# Step 4: Print the final list of palindromes with their indices
print(f"Final list of palindromes ({len(palindromes)}):")
for index, word in palindromes:
    print(f"Index: {index}, Palindrome: {word}")
