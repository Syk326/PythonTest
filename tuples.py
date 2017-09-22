# Tuples store 2+ values that are closely related pieces of info, immutable

AngkorWat = (13.4125, 103.866667) #parens optional
print(type(AngkorWat))

# tuple unpacking
dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions: {}x{}x{}".format(length, width, height))

# tuples can be stored in sets or as dictionary keys
world_heritage_locations = {(13.4125, 103.866667): "AngkorWat", (25.73333, 32.6): "Ancient Thebes", (30.330556, 35.443330): "Peta", (-13.116667, -72.583333): "Machu Picchu"}
print(world_heritage_locations)

# return tuples, unpack right away
def first_and_last(sequence):
    """Return 1st and last sequence elements"""
    return sequence[0], sequence[-1]
start, end = first_and_last(["spam", "egg", "sausage", "spam"])
print(start)
print(end)

# sample tuple function
def hours2days(hours_length):
    return (hours_length // 24), (hours_length % 24)
print(hours2days(24))
print(hours2days(25))
print(hours2days(10000))
