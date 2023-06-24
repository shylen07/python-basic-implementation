# Title: Word Count
# Created by Devender Singh

def word_count(sentence):
    words = sentence.split()
    return len(words)

text = input("Enter a sentence: ")
count = word_count(text)
print("Word Count:", count)
