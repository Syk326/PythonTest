# Practice with lists

# Basic index tests
python_versions = [1.0, 1.5, 1.6, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6]
print(python_versions[0])
print(python_versions[-1])
# print(python_versions[30]) -> Index Error
# lists are mutable (can be modified), while strings are IMmutable
# If you assign one list to another and change the firt, will it be reflected in the 2nd? Yes.
print(sorted(python_versions, reverse = True))
python_versions.append('4.0')
print(python_versions)

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(months)
q3 = months[6:9] # Index 6, 7, 8 (stop before 9)
print(q3)
first_half = months[:6]
print(first_half)
second_half = months[6:]
print(second_half)
three_last = months[-3:]
print(three_last)
print('September' in months)
months[0:2] = ['Jasminuary', 'Valencuary']
print(months)
print(max(months)) # last in aphabetical order

# "\n" as separator between each element in the list
# join -> error if anything other than str
nautical_directions = "\n".join(["fore", "aft", "starboard", "port"])
print(nautical_directions)

# returns highest 3 numbers in the list
def top_three(input_list):
    return sorted(input_list, reverse = True)[:3]
new_list = [2,3,5,6,8,4,2,1]
print(top_three(new_list))
