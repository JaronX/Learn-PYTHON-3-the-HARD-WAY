from sys import argv #calling for argv function in sys lybrary

script, input_file = argv #define two argv variables

def print_all(f): #define function with one argument
	print(f.read()) #define argument to read

def rewind(f): #define function with one argument
	f.seek(0) #starts reading from the beggining if we change index it will read file from that charachter - f.seek(2) is is line 1 ...

def print_a_line(line_count,f): #define function with two arguments
	print(line_count, f.readline()) #first argument count the number of line, second argument read that line

current_file = open(input_file) #assign a variable which open inputed file from argv 

print("First let's print the whole file: \n") #print text and make next line blank

print_all(current_file) #print contet of file inside current_file variable

print("Now let's rewind, kind of like a tape.") #print text

rewind(current_file) #starts reading our file from charachter witch is assignet to f.seek 

print("Let's print three lines:") #print text

current_line = 1 #define new variable with value 1
print_a_line(current_line, current_file) #print first line of our file

current_line += 1 #redefine value of upper variable and add 1
print_a_line(current_line, current_file) #print second line

current_line += 1 #redefine value of upper variable and add 1
print_a_line(current_line, current_file) #print third line