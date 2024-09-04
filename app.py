import requests

# Step 1: Download the word list
url = "https://public.websites.umich.edu/~jlawler/wordlist"
response = requests.get(url)
word_list = response.text.splitlines()

# Step 2: Create an empty list to hold palindromes
palindromes = []

# Step 3: Loop through each word in the word list
for word in word_list:
    # Check if the word is a palindrome
    if word == word[::-1]:
        # Append word to the palindrome list
        palindromes.append(word)

# Step 4: Print the list of palindromes
print(palindromes)
