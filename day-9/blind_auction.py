import os
import art

# print(art.logo)

buyer_info_list = []
while True:
    buyer_info = {}
    buyer_name = input("Enter name: ")
    buyer_bid = int(input("Enter bid: $"))
    buyer_info = {"name": buyer_name, "bid": buyer_bid}
    buyer_info_list.append(buyer_info)
    
    restart = input("Anyone else? y/n\n> ")
    if restart == 'y':
        os.system('cls')
        continue
    else:
        break

# bid_value = []
highest_bid = None
winner_name = None
for buyer_info in buyer_info_list:
    bid = buyer_info['bid']
    if highest_bid is None or bid > highest_bid:
        highest_bid = bid
        winner_name = buyer_info['name']

    
print(f"${highest_bid} wins it. This goes to {winner_name.title()}")
