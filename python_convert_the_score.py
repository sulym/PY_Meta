def convert_the_score(score_string: str) -> list:
    
    numbers = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    score_list = score_string.split()
    converted_score = []
    for word in score_list:
        if word in numbers:
            converted_score.append(numbers[word])
    return converted_score

def convert_the_score(score_string: str) -> list:
    score_dict = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    return [score_dict[score] for score in score_string.split() if score in score_dict]