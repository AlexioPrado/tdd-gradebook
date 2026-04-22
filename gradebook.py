def letter_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be an int or float")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def is_passing(score):
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be an int or float")

    return score >= 60

def average(scores):
    if not isinstance(scores, list):
        raise TypeError("scores must be a list")
    if len(scores) == 0:
        raise ValueError("Scores list cannot be empty")        
    if not all(isinstance(s, (int, float)) for s in scores):
        raise TypeError("all scores must be a float or int")

    return round(sum(scores) / len(scores), 2)

def curved_score(score, bonus):
    if bonus < 0:
        raise ValueError("Bonus must be a positive")
    return min(score + bonus, 100) 