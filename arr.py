def display(arr):
    print("Current Array:", arr)
arr = [10, 20, 30, 40, 50]
print("Initial Array:")
display(arr)
print("\nUsing elements:")
print("First element:", arr[0])
print("Last element:", arr[-1])
print("\nInserting an element at index 2, value 25:")
arr.insert(2, 25)
display(arr)
print("\nAppending Element (60):")
arr.append(60)
display(arr)
print("\nExtending an array ([70, 80]):")
arr.extend([70, 80])
display(arr)
print("\nLength of Array:", len(arr))
print("\nSorting Array:")
arr.sort()
display(arr)
print("\nReversing Array:")
arr.reverse()
display(arr)
print("Sum of elements:", sum(arr))
15
print("While loop (1 to 5):")
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1
print("\n\nfor loop (1 to 5):")
for i in range(1, 6):
    print(i, end=" ")
print("\n\nNested loop (3 x 3 Pattern):")
for row in range(3):
    for col in range(3):
        print("*", end=" ")
    print()
