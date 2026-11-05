bids = {}
newBiders = True
answers = ["yes","no"]

def find_highest_bid(bidding_dictionary): 
    winner = ""
    highest_bid = 0
    for bid in bidding_dictionary:
        bid_amount = bidding_dictionary[bid]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bid
    
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while newBiders == True:
    name = input("What is your name? ")
    bids[name] = float(input("What is your bid? $"))
    choice = ""
    while not choice in answers:
        choice = input("Are there any other bidders? (type 'yes' or 'no') \n").replace(" ", "").lower()
    if choice == "yes":
        print("\n"*100)
    else:
        newBiders = False

find_highest_bid(bids)

