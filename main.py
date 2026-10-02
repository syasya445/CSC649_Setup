# CSC649: My First Python experiment

sentence = input("Enter a sentence: ")

if sentence.strip() == "":
    print("Error: You did not enter any text. Please enter a valid sentence.")
else:
    word_count = len(sentence.split())
    character_count = len(sentence)

    print(f"Word count: {word_count}")
    print(f"Character count (including spaces): {character_count}")