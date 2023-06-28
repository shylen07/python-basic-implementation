# Title: Reverse String
# Created by Devender Singh

def reverse_string(string):
    return string[::-1]

text = input("Enter a string: ")
reversed_text = reverse_string(text)
print("Reversed String:", reversed_text)
