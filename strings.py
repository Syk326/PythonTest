# String practice

# "" or '' are OK
print("Hello World")
print('Hello World')
pet_halibut = 'Why should I be tarred with the epithet "loony" merely because I have a pet halibut?'
salesman_single = 'I think you\'re an encyclopaedia salesman'
salesman_double = "I think you're an encyclopaedia salesman"

# concatenated strings
coconuts = "34"
mangos = "15"
fruit = coconuts + mangos
print(fruit) # 3415
print(coconuts + " and " + mangos)

# str functions
given_name = "Gregory"
middle_name = "Walker"
family_name = "Stevens"
name_length = len(given_name + middle_name + family_name) + 2 # includes spaces
print(name_length)

# primitive types
print(type(633))
print(type("633"))
print(type(633.))
print(type(633>632))

# manipulate str
print("hippo"*3)

# convert str to int and back
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales)
print("This week total: " + str(weekly_sales)) # turn back into str

# change int for str
house_num = 13
street_name = "Jumpers"
town_name = "Hirose"
address = str(house_num) + " " + street_name + ", " + town_name
print(address)

# check or change str
full_name = "gregory stevens"
print(full_name.islower()) #true
print(full_name.title()) #Gregory Stevens

# count elements in str
fish_count = "One fish, two fish, red fish, blue fish".count('fish')
print(fish_count)

# pre-populate str
user_ip = 208.94.117.90
url = /bears/koala
now = 16:20
log_message = "IP address {} accessed {} at {}".format(user_ip, url, now)
print(log_message)
