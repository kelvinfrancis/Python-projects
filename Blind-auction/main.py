from replit import clear
from art import logo

print(logo)
print("Welcome to the auction program.")

# Dictionary
participants = {}
restart = True

def find_hightest(bid_participants):
  highest_bid = 0
  for bidder in bid_participants:
    bid_ammount = bid_participants[bidder]
    
    if bid_ammount > highest_bid:
      highest_bid = bid_ammount
      winner = bidder

  print(f"The winner is {winner} with a bid of ${highest_bid}")
    

while restart == True:
  name = input("What is your name?: ")
  bid = int(input("Enter your bid: $"))

  # Enter the participant
  participants[name] = bid

  # Ask if want to continue adding participants
  continue_add = input("Are there any other bidders? Type 'yes' or 'no'. ")

  if continue_add == "yes":
    restart = True
    clear()
  elif continue_add == 'no':
    restart = False
    find_hightest(participants)




  
