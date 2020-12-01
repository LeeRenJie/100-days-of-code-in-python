from replit import clear
from art import logo
print(logo)

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""

  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]

    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder

  print(f"The winner is {bidder} with a bid of ${highest_bid}")

bids = {}
bidding_finish = False

while not bidding_finish: 
  name = input("What is your name?\n")
  price = int(input("How much would you like to bid?\n$"))

  bids[name] = price

  should_continue = input('Are there any other bidders? type "Yes" or "No"\n').lower()
  
  if should_continue == "no":
    bidding_finish = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
