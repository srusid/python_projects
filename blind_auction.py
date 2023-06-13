from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

auction = {}

bidder = True


def highest_bidder(bidding_amount):
  high_bid = 0
  for bidder in auction:
    bid_amount = auction[bidder]
    if bid_amount > high_bid:
      high_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a high bid of ${high_bid}.")


while bidder:
  name = input("What is your name?: ")
  bid = int(input("What's your bid? $"))
  auction[name] = bid
  next_bidder = input("Are there any other bidders? Type 'yes' or 'no'\n")
  if next_bidder == 'no':
    bidder = False
    highest_bidder(auction)
  elif next_bidder == 'yes':
    clear()
