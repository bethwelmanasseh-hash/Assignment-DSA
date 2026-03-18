#array insertion
arr = [1, 2, 3, 4, 5]
def visualize_array(arr):
    print(f"Array: {arr}")
visualize_array(arr)
def insert_at_position(arr, position, value):
    if position < 0 or position > len(arr):
        print("Invalid position")
        return
    arr.insert(position, value)
    print(f"Inserted {value} at position {position}")
    visualize_array(arr)
insert_at_position(arr, 2, 10)  # Insert 10 at index 2
insert_at_position(arr, 0, 0)   # Insert 0 at the beginning
insert_at_position(arr, len(arr), 20) # Insert 20 at the end
