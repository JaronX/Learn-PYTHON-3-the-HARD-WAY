# create a mappin of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California': 'CA',
	'New Yourk': 'NY',
	'Michigan': 'MI'
}

print(states)

# create a basic set of states and somme cities in them
cities = {
	'CA': 'San Francisco',
	'MI': 'Detroit',
	'FL': 'Jacksonville',
}

print("1", cities)

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print("2", cities)

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print("-" * 10)
print("Michigan's abbreviations is: ", states['Michigan'])
print("Florida's abbreviations is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} is abbreviated {abbrev}")
	
# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
	print(f"{abbrev} has the city {city}")

# now do both at the same tie
print('-' * 10)
for state, abbrev in list(states.items()):
	print(f"{state} state is abbreviated {abbrev}")
	print(f"and has city {cities[abbrev]}")
	
print('-' * 10)
# safely get a abbreviatin by state that might not be there
state = states.get('Texas')

if not state:
	print("Sorry, no texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")


	
	
	
	
	

