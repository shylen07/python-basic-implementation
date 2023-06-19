# Title: Count Vowels in a String
# Created by Devender Singh

def count_vowels(string):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    for char in string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

text = input("Enter a string: ")
print("Vowel count:", count_vowels(text))
