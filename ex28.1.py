# Simple exercies for Boolean logic

a = 6
b = 7
print(1, a == 6) # True
print(2, a == 7) # False
print(3, a == 6 and b == 7) # True and True -> True
print(4, a == 7 and b == 7) # False and True -> False
print(5, not a == 7 and b == 7) # not False and True = True and True -> True
print(6, a == 7 or b == 7) # False or True -> True
print(7, a == 7 or b == 6) # False or False -> False
print(8, not (a == 7 and b == 6)) # not (False and False) = not False -> True
print(9, not a == 7 and b == 6) # not False and False = True and False -> False