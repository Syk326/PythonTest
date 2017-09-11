# A full program with different functions that implement specific tasks

def scores_to_rating(score1,score2,score3,score4,score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    #STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    #STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1,score2,score3,score4,score5)/3

    #STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating

def convert_to_numeric(score):
    """Take a score and convert it to an int or float"""
    return float(score)

def sum_of_middle_three(score1,score2,score3,score4,score5):
    """Take 5 scores and return the sum without the minimum or maximum"""
    sum_of_all_five_scores = score1 + score2 + score3 + score4 + score5
    min_score = min(score1,score2,score3,score4,score5)
    max_score = max(score1,score2,score3,score4,score5)
    return sum_of_all_five_scores - min_score - max_score

def score_to_rating_string(score):
    """Take average score and compare to different ratings"""
    if 0 <= score < 1:
        return "Terrible"
    elif 1 <= score < 2:
        return "Bad"
    elif 2 <= score < 3:
        return "OK"
    elif 3 <= score < 4:
        return "Good"
    else:
        return "Excellent"

print(scores_to_rating(1,2,3,4,5)) # should be Good
print(scores_to_rating(4,4,2,1,4))
