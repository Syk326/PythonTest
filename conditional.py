# Practicing with conditionals if/elif/else
# and, or, not
is_raining = True
is_sunny = True
if is_raining and is_sunny:
    print("Is there a rainbow?")

# Not "if real_grail == False"
real_grail = False
if not real_grail:
    print("It's a grail-shaped beacon!")

# Change values depending on conditional
phone_balance = 7.53
bank_balance = 94.39
if phone_balance < 10:
    phone_balance += 10
    bank_balance -= 10
print(phone_balance)
print(bank_balance)

# Multiple conditions
age = 17
free_up_to_age = 4
child_up_to_age = 18
senior_from_age = 65
concession_ticket = 1.25
adult_ticket = 2.50
if age <= free_up_to_age:
    ticket_price = 0
elif age <= child_up_to_age:
    ticket_price = concession_ticket
elif age >= senior_from_age:
    ticket_price = concession_ticket
else:
    ticket_price = adult_ticket
message = "Somebody who is {} years old will pay ${} to ride the bus.".format(age,ticket_price)
print(message)

# Return string right away depending on conditions
def which_prize(points):
    """
    Returns the prize-winning message, given a number of points
    """
    if points <= 50:
        return "Congratulations! You have won a wooden rabbit!"
    elif points <= 150:
        return "Oh dear, no prize this time."
    elif points <= 180:
        return "Congratulations! You have won a wafer-thin mint!"
    else:
        return "Congratulations! You have won a penguin!"
print(which_prize(164))

# "if <variable>" means if not None (null)
def which_prize(points):
    prize = None
    if points > 180:
        prize = "penguin"
    elif points > 150:
        prize = "wafer-thin mint"
    elif points <= 50:
        prize = "wooden rabbit"
    if prize:
        return "Congratulations! You have won a {}!".format(prize)
    else:
        return "Oh dear, no prize this time."
print(which_prize(5))
