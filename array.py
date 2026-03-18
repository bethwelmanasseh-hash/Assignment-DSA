#array indexing

arr = [1, 2, 3, 4, 5]
print(f"Array: {arr}")  #original array in dict form
print(f"Element at index 0: {arr[0]}")  # Accessing
print(f"Element at index 2: {arr[2]}")  # Accessing
print(f"Element at index 4: {arr[4]}")  # Accessing
# Negative indexing
print(f"Element at index -1: {arr[-1]}")  # Accessing last element
print(f"Element at index -2: {arr[-2]}")  # Accessing second-to-last element

#array insertion
arr.append(6)  # Inserting at the end
print(f"Array after appending 6: {arr}")
arr.insert(2, 10)  # Inserting 10 at index 2
print(f"Array after inserting 10 at index 2: {arr}")


