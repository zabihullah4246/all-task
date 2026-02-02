# 1. Area of a circle
radius = float(input("Enter radius of circle: "))
area = 3.14159 * radius * radius
print("Area of circle:", area)
print("-" * 30)

# 2. Swap two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)
print("-" * 30)

# 3. Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
print("-" * 30)

# 4. Total marks and percentage of 5 subjects
marks = []
for i in range(5):
    m = int(input(f"Enter marks of subject {i+1}: "))
    marks.append(m)

total = sum(marks)
percentage = total / 5
print("Total marks:", total)
print("Percentage:", percentage)
print("-" * 30)

# 5. Integer to float & float to integer
num_int = int(input("Enter an integer: "))
num_float = float(input("Enter a float: "))
print("Integer to float:", float(num_int))
print("Float to integer:", int(num_float))
print("-" * 30)

# 6. List of five numbers (sum, max, min)
numbers = [5, 10, 15, 20, 25]
print("Numbers:", numbers)
print("Sum:", sum(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("-" * 30)

# 7. Take 5 names from user
names = []
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)
print("Names list:", names)
print("-" * 30)

# 8. Add element using append()
my_list = [1, 2, 3]
my_list.append(4)
print("After append():", my_list)
print("-" * 30)

# 9. Insert element at specific index
my_list.insert(2, 99)
print("After insert():", my_list)
print("-" * 30)

# 10. Remove element using remove() and pop()
my_list.remove(99)
print("After remove():", my_list)
my_list.pop(1)
print("After pop():", my_list)
