# Title: Anagram Checker
# Created by Devender Singh

def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
if is_anagram(word1, word2):
    print("Anagram")
else:
    print("Not Anagram")
