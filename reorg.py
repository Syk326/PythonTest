# Reorganizing code
# DRY = Don't Repeat Yourself
# Contrast WET = Write Everything Twice, etc.
# Factoring = decomposing complex problem into simpler parts
# Re-factoring = restructuring existing code
# Set good variable names, repeated parts as seperate functions, use comments

def check_attempts(attempts,answers):
    """
    Checks the 5 attempts on a multiple choice quiz and returns score
    """
    # Runs function to compare each attempt to answer
    results = []
    for i in range(len(attempts)):
        results.append(compare_answers(attempts[i],answers[i]))

    # Variable to count correct answers
    count_correct = 0

    # Loop to increment correct
    for result in results:
        if result:
            count_correct += 1

    # Return passing/failure
    if count_correct/len(results) > 0.7:
        return "Congratulations, you passed the test! You scored " + str(count_correct) + " out of 5."
    elif (len(results)-count_correct)/len(results) >= 0.3:
        return "Unfortunately, you did not pass. You scored " + str(count_correct) + " out of 5."

# Function to compare attempts to answers
def compare_answers(attempt, answer):
    return attempt == answer

# Testing
testAttempts = [1, 2, 3, 4, 5]
testAnswers = [5, 2, 3, 4, 5]
testResults = check_attempts(testAttempts, testAnswers)
print(testResults)
