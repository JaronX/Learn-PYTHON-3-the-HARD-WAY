def cheese_and_crackers(cheese_count, boxes_of_crackers): #define function with name "cheese_an_crackers" with 2 arguments inside
	print(f"You have {cheese_count} cheeses!") #print text + value of first argument "cheese_count" from our function 
	print(f"You have {boxes_of_crackers} boxes of crackers!") #print text + value of second argument "cheese_count" from our function
	print("Man that's enough for a party!") #print text
	print("Get a blanket.\n") #print text + new blank line


print("We can just give the funcion numbers directly:") #print text
cheese_and_crackers(20, 30) #define the value of the two arguments inside our functiont as numbers

print("OR, we can use variables from our scipt:") #print text
amount_of_cheese = 10 #call for a variable and define the value as number
amount_of_crackers = 50 #call for a variable and define the value as number

cheese_and_crackers(amount_of_cheese, amount_of_crackers) #define the value of the two arguments inside our function as variables 


print("We can even do math inside too:") #print text
cheese_and_crackers(10 + 20, 5 + 6) #define the value of the two arguments inside our function like result of simple math calculations


print("And we can combine the two, variables and math:") #print text
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #define the value of the two arguments inside our function like variables and simple math calculations