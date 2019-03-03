def function_name(argument1, argument2):
	print(f"This is the value of 1-st argument inside my function: {argument1}")
	print(f"This is the value of 2-nd argument inside my function: {argument2}")
	print("Just a simple text")
	print("and little blank space for easy read \n")
	

print("1-st way with simple input")
function_name(input("Give me something: "), input("Once more please: "))

print("2-nd way with input as whole numbers")
function_name(int(input("First number: ")), int(input("Second number: ")))

print("3-rd way with variable")
x = "blalbalbal"
y = "tralalala"

function_name(x, y)

print("4-th way with input as floating numbers and some math - collection")
function_name(float(input("First number: ")) + float(input("Second number: ")),float(input("Third number: ")) + float(input("Fourth number: ")))

print("and more... next time")