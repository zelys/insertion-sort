# Sort function using list comprehensions
def sortFunction(array):
    n = len(array)
    [
        array.insert(j + 1, array.pop(j))
        for i in range(n)
        for j in range(n - i - 1)
        if array[j] > array[j + 1]
    ]


# List
arrayNumber = [75, 35, 20, 2, 1]

# Call the function
sortFunction(arrayNumber)

# Show sorted list
print("Ordered list:", arrayNumber)

# Ordered list: [1, 2, 20, 35, 75]
