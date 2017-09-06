# Practicing with variables

# Simple assignment
savings = 514.86
salary = 320.51

# Multiple variables on one line
savings, salary = 514.86, 320.51

# Use underscores for multi-word variables
# No variable type or ending ;
manila_pop = 1780148
manila_area = 16.56
manila_pop_density = manila_pop / manila_area
print(manila_pop_density)
manila_pop += 1675

# Doesn't change
print(manila_pop_density)

# Need to do equation again
manila_pop_density = manila_pop / manila_area
print(manila_pop_density)

# Boolean examples
the_sun_is_up = True
the_sky_is_gray = False
print(1<2)
print(42>43)
print(manila_pop == manila_area)
print(savings != salary)
print(30>=29)
