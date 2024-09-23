import copy

# Original list
original_list = [1, 2, [3, 4]]

# Shallow copy using copy.copy()
shallow_copy = copy.copy(original_list)

# Deep copy using copy.deepcopy()
deep_copy = copy.deepcopy(original_list)

# Modifying the original list
original_list[2][0] = 5

# Printing the copies
print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)