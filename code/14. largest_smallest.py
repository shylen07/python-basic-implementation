# Title: Find Largest and Smallest Elements
# Created by Devender Singh

def find_largest_smallest(arr):
    largest = max(arr)
    smallest = min(arr)
    return largest, smallest

numbers = [12, 45, 23, 67, 9, 56]
largest_num, smallest_num = find_largest_smallest(numbers)
print("Largest:", largest_num)
print("Smallest:", smallest_num)
