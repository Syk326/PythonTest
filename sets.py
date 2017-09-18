# Testing out using sets

# Removing duplicates WITHOUT sets
def remove_duplicates(source):
    target = []
    for element in source:
        if element not in target:
            target.append(element)
    return target
countries = ['USA', 'Japan', 'Mexico', 'Japan']
print(remove_duplicates(countries))

# Removing duplicates WITH sets
country_set = set(countries)
print(country_set) #wow

# Populate "square" with set of all square num ints < 2000
squares = set() #empty set
n = 1
while n**2 < 2000:
    squares.add(n**2)
    n += 1
print(len(squares))
