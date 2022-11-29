#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Write your code below this line 👇

print("Welcome to the bill calculator.")    
bill = float(input("What was the total bill? ")) 
percen = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_percen = percen / 100 * bill + bill
result = (bill_with_percen / people)

print(f"Each person should pay: ${round(result,2)}")
