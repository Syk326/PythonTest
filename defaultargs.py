# Default Arguments to avoid creating multiple over-ridden functions
# AVOID IF VARIABLE = MUTABLE, will continue to change w/ instances

# Set default values to args that are optional
def print_list(l, numbered = False, bullet_character = "-"):
    """Prints a list on multiple lines, with numbers or bullets"""
    for index, element in enumerate(l):
        if numbered:
            print("{}: {}".format(index+1, element))
        else:
            print("{} {}".format(bullet_character, element))
print_list(["cats", "in", "space"], False, '*')
print_list(["cats", "in", "space"], True)
print_list(["cats", "in", "space"])
