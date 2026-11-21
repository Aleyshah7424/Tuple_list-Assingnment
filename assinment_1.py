
cities = ["Lahore", "Karachi", "Multan", "Quetta", "Peshawar"]

print(cities[0], cities[-1], cities[1:4], cities[::-1])





marks = [78, 92, 65, 88, 54]

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

above_70 = 0
for mark in marks:
    if mark > 70:
        above_70 += 1

print(total, average, highest, lowest, above_70)





shopping_list = ["bread", "milk", "eggs"]

shopping_list.append("rice")
shopping_list.insert(1, "sugar")
shopping_list.remove("milk")
popped_item = shopping_list.pop()

print(f"popped {popped_item}, final list {shopping_list}")




nums = [3, 1, 3, 2, 1, 5]
unique_nums = []

for num in nums:
    if num not in unique_nums:
        unique_nums.append(num)

print(unique_nums)



numbers = range(1, 16)

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)




r = [1, 2, 3, 4, 5]
rotated = r[2:] + r[:2]

print(rotated)


a = [1, 2, 3]

b = a
c = a.copy()

a.append(4)

print("a =", a)
print("b =", b)
print("c =", c)


