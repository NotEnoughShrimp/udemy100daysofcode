import random
from art import logo, vs
from game_data import data
        
def get_account():  # this will give me a random choice from data
    return random.choice(data)

def format_info(user):  # much better than manually typing out f"{data.get('name')}, a {data.get('description')}, from {data.get('country')}.
    name = user["name"]   
    description = user["description"]
    country = user["country"]
    return f"{name}, a {description} from {country}"

def answer(guess, person_a, person_b):
    if person_a > person_b:
        return guess == "a"
    else:
        return guess == "b"

def high_or_low():
    print(logo)
    score = 0
    
    person_one = get_account()
    person_two = get_account()
    
    while True:
        person_one = person_two
        person_two = get_account()
        
        while person_one == person_two:
            person_two = get_account()
        
        print(f"Person 1: {format_info(person_one)}")
        print(vs)
        print(f"Person 2: {format_info(person_two)}")
        guess = input("A or B: ").lower()
        
        person_one_follower_count = person_one["follower_count"]
        person_two_follower_count = person_two["follower_count"]
        check_correct = answer(guess, person_one_follower_count, person_two_follower_count)
        
        print(logo)
        if check_correct:
            score += 1
            print(f"Correct. Score: {score}")
        else:
            print(f"Incorrect. Final score: {score}")
            break
        
high_or_low()
