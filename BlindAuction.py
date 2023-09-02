#This program imitates silent auction where it ask for bidder name and bid price and calculates the higest bidder/winner. 

from replit import clear

auction={}

other_biders = True


def find_largest_bidder(auction):
  largest_bid = 0
  largest_bid_holder = ""

  for name in auction:
      if auction[name] > largest_bid:
        largest_bid = auction[name]
        largest_bid_holder = name

  print(f"The winner is {largest_bid_holder} with a bid of {largest_bid}")


while other_biders:
  name=input("What is your name?: ")
  bid=int(input("What's your bid?: "))
  bider_sw = input("Are there other biders? Type 'yes' or 'no' ")
                   
  auction[name]=bid
  clear()
                   
  if bider_sw == 'no':
    other_biders=False
    find_largest_bidder(auction)
    
  


