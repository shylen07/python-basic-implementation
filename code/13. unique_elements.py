# Title: Find Unique Elements
# Created by Devender Singh

def find_unique_elements(arr):
    unique_set = set(arr)
    unique_list = list(unique_set)
    return unique_list

numbers = [1, 2, 3, 3, 4, 4, 5, 6, 6]
unique_numbers = find_unique_elements(numbers)
print("Unique Elements:", unique_numbers)
