inches = float (input("Inches = "))
pounds = float (input("Pounds = "))
centimeters = float(inches * 2.54)
kilograms = float(pounds * 0.453592)
print(f"Inches ({inches}) => Cm ({round(centimeters, 2)})")
print(f"Pounds ({pounds}) => Kg ({round(kilograms, 2)})")