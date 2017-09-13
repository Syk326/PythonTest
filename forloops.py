# Practice with for loops

# for each name in names (singular in plural) print in title cases
names = ['merkle', 'valerie', 'mary beth', 'matt', 'jenny', 'craig', 'anthony', 'aldo', 'bethany']
for name in names:
    print(name.title())

# for each element in list, add to sum total
def list_sum(input_list):
    sum = 0
    for number in input_list:
        sum += number
    return sum

# Test cases to check list_sum works correctly
test1 = list_sum([1, 2, 3])
print("list_sum expected result: 6, actual result: {}".format(test1))
test2 = list_sum([-1, 0, 1])
print("list_sum expected result: 0, actual result: {}".format(test2))

# for each string in list, check 1st and last indices for XML brackets
def tag_count(string_list):
    count = 0
    for tag in string_list:
        if tag[0] == "<" and tag[-1] == ">":
            count+=1
    return count

# Test for the tag_count function:
list1 = ['<TextView>', 'android:text="yo"', '</>']
count = tag_count(list1)
print("tag_count expected result: 2, Actual result: {}".format(count))

# for each token (singular string) in tokens (plural strings list),
# += to create one string in HTML format
def html_list(tokens):
    html_string="<ul>\n"
    for token in tokens:
        html_string+="<li>{}</li>\n".format(token)
    html_string+="</ul>"
    return html_string
list1 = ['first string', 'second string']
final_string = html_list(list1)
print(final_string)

# create box of * using 'for i in range(some_length)'
def starbox(width, height):
    print("*" * width) #print top edge of box
    for i in range(height-2): #print sides based on height - top & bottom
        print("*" + (" " * (width-2)) + "*")
    print("*" * width) #print bottom edge of box

# Test Cases
print("Test 1:")
starbox(5, 5)
print("Test 2:")
starbox(6, 3)

# typical for loops
for i in range(4):
    print(i)
print(names)
for index in range(len(names)):
    names[index] = names[index].title()
print(names)
