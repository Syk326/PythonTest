# files

# open and read
"""
f = variable the file value is assigned to
open = build-in open function
flying_circus_cast.txt = path to file
r = mode to open in, in this case read-only
"""
f = open('flying_circus_cast.txt', 'r')
# file_data = string object with text in file
file_data = f.read()
# close files to free up system resources
f.close()

# write
"""
my-file.txt = path to file, will create if it doesn't exist
w = write mode, will delete all previous content
a = append mode, won't delete
"""
f = open('my-file.txt', 'w')
f.write("Hello World")
f.close()

# with = function to do ops on file then auto-close
with open('camelot.txt') as song:
    print(song.read(2)) # prints file up to char 2
    print(song.read(8)) # prints file from prev char to char 8
    print(song.read()) # prints rest of file

# loop through file lines and extract actor names (before comma)
def create_cast_list(filename):
    cast_list = []
    actor_line = []
    with open(filename) as f:
        #use the for loop syntax to process each line
        for line in f:
            #and add the actor name to cast_list
            actor_line.append(line.split(','))
        for info in actor_line:
            cast_list.append(info[0])
    return cast_list
print(create_cast_list("flying_circus_cast.txt"))
