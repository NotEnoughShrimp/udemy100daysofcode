#Password Generator Project
import random, os, time
os.system('cls')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
           'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


while True:
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    password = []
    for l in range(1, nr_letters+1):
        password.append(random.choice(letters))
    for n in range(1, nr_numbers+1):
        password.append(random.choice(numbers))
    for s in range(1, nr_symbols+1):
        password.append(random.choice(symbols))

    random.shuffle(password)
    result = ''.join(password)
    print(f"Password is: {result}")
    
    
    end = input("restart [1], exit [2]\n> ")
    if end == '2':
        break
    else:
        time.sleep(1)
        os.system('cls')
