import random 
from art import logo
def difficulty_set():
    difficulty = input("Choose a difficulty. Type 'e' for Easy (10 lives), 'h' for Hard (5 lives). ")
    if difficulty == 'e':
        return 10
    elif difficulty == 'h':
        return 5

def high_or_low():
    print(logo)
    print("Number guessing. A number 1-100")
    lives = difficulty_set()
    test_answer = random.randint(1,100)
    is_game_over = False
    
    print(f"Total lives: {lives}")
    while not is_game_over:
        print(f"For the sake of testing: {test_answer}")
        
        if lives == 0:
            print(f"Game Over. The number is: {test_answer}")
            break
        
        user_guess = int(input("Enter a number: "))
        if user_guess > 100 or user_guess <= 0:
            print("Invalid input")
        else:
            distance = abs(user_guess - test_answer)
            if distance <= 5:
                message = "Very close"
            elif distance <= 10:
                message = "Close"
            elif distance <= 20:
                message = "A little cold"
            else:
                message = "Keep at it"
                
        if user_guess < test_answer:
            lives -= 1
            print(f"{message}, but you're too low, {lives} lives remaining.")
        elif user_guess > test_answer:
            lives -= 1
            print(f"{message}, but you're too high, {lives} lives remaining.")
        else:
            print(f"Correct. The answer is: {test_answer}, with {lives} life remaining.")
            is_game_over = True
            
high_or_low()
