# Practicing with functions
def readable_timedelta(days):
    # docstring with """
    """Takes a value in days and returns weeks with days remaining
    """
    weeks = days // 7
    remainder = days % 7
    total_time = "{} week(s) and {} day(s)".format(weeks, remainder)
    return total_time

print(readable_timedelta(76))

def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

print(cylinder_volume(10,3))

def print_testcase(expected_value, actual_value):
    print("expected value: {}, actual value: {}".format(expected_value, actual_value))
return_value = print_testcase(42, 42)
# will print "None" = absence of value
print(return_value)
