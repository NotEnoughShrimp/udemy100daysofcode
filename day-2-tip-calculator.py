#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇

# simple version with static values
bill = 150.00
people = 5
tip = 0.12

split_payment = (bill/people) * (1+tip)
total = round(split_payment, 2)
print("{:.2f}".format(total))

# modified version
bill = float(input("What is the total? "))
people = int(input("How many people? "))

tip = float(input("What is your tip? "))
tip_decimal = tip/100


split_payment = (bill/people) * (1 + tip_decimal)
final = round(split_payment, 2)

print("{:.2f}".format(final))
