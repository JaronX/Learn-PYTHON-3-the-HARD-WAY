def while_loop_first_is_lower_than_second(first, second):
	while first < second:
		first = first + increments_by
		print(f"At the top i is {first}")
		numbers.append(first)
		
		
		print("Numbers now: ", numbers)
		print(f"At the bottom i is {first}")






numbers = []

increments_by = 1
to = 6
while_loop_first_is_lower_than_second(0, to)

print("The numbers: ")

for num in numbers:
	print(num)