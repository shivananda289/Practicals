n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num
print("Maximum value is:", max_value)
