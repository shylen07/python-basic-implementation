# Title: Find Common Elements
# Created by Devender Singh

def find_common_elements(arr1, arr2):
    common = []
    for element in arr1:
        if element in arr2:
            common.append(element)
    return common

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(list1, list2)
print("Common Elements:", common_elements)
