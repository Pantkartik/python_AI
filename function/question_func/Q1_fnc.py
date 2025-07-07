# Function to return the length of a list
def leng_list(lst):
    return len(lst)

# Create an empty list once
lst = []

# Loop to add 10 elements
for i in range(10):
    elm = int(input(f"Enter element {i + 1}: "))
    lst.append(elm)

# Call function and print length
length = leng_list(lst)
print("Length of the list is:", length)
