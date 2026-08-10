words = {
    "madad": "help",
    "kurshi": "chair",
    "kutta": "dog"
}

word = input("Enter the word: ")

if word in words:
    print(words[word])
else:
    print("Word not found in dictionary") 
