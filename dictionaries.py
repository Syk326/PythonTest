from countries import country_list # Note: since the list is so large, it's tidier

# Practicing with dictionaries, like HashSets

# count number of each country, imported
country_counts = {}
for country in country_list:
    if country in country_counts:
        country_counts[country] += 1
    else:
        country_counts[country] = 1
print(country_counts)

# simple dictionary, key: value
population = {'Shanghai':17.8, 'Istanbul': 13.3, 'Karachi': 13.0, 'Mumbai': 12.5}
print(population['Shanghai'])
#KeyError: print(population['Atlanta'])
print(population.get('Atlanta')) #None
if 'Atlanta' in population: #Check if in dictionary
    print("City under control")
else:
    print("CITY OUT OF CONTROL!")
print(population.get('Atlanta', 'No population there')) #Will print latter
population['Atlanta'] = 3
for city in population:
    print("The city {} has a population of {} million".format(city, population[city]))

# Dictionary sample
Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963,
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}
for album_title in Beatles_Discography:
    print("title: {}, year: {}".format(album_title, Beatles_Discography[album_title]))

# Finds the value that repeats the most
def most_prolific(discography):
    year_list = {}
    # creates dictionary of key = year, value = occurrence number
    for album_title in discography:
        year = discography[album_title]
        if year in year_list:
            year_list[year] += 1
        else:
            year_list[year] = 1
    # return max value
    return max(year_list, key=year_list.get)
print (most_prolific(Beatles_Discography))
