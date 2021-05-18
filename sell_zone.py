import argparse

parser = argparse.ArgumentParser()

""" parser.add_argument('--purchasePrice', type=float, required=True)
parser.add_argument('--filled', type=float, required=True)

args = parser.parse_args()

purchase_price = args.purchasePrice
filled = args.filled """

# parser.add_argument('-c', type=float, required=True)

lis_names = ["ETH_USDT", "LINK_USDT", "DOT_USDT", "THETA_USDT",
             "VET_USDT", "TRX_USDT", "ONT_USDT", "NKN_USDT", "BTT_USDT", "ROSE_USDT"]
print("Select the coin for which you want to see the profit points:\n")

print(f"0. {lis_names[0]}\n1. {lis_names[1]}\n2. {lis_names[2]}\n3. {lis_names[3]}\n4. {lis_names[4]}\n5. {lis_names[5]}\n6. {lis_names[6]}\n7. {lis_names[7]}\n8. {lis_names[8]}\n9. {lis_names[9]}")

user_choice = int(input())


lis_pp = [3520.83, 39.301, 40.240, 9.413,
          0.226, 0.14, 2.5822, 0.0071644, 0.0071644, 0.15294]
lis_filled = [0.06717, 7.633, 4.970, 5.252,
              2800, 137.2058, 5.5844751, 18.2, 1395, 65.3]

purchase_price = lis_pp[user_choice]
filled = lis_filled[user_choice]
# purchase_price = float(input("Enter the purchase Price: ")) # pp
# filled = float(input("Enter the filled quantity: "))
usdt = purchase_price*filled
print(
    f"You purchased 💲{round(usdt,8)} worth of {lis_names[user_choice]} tokens.")

print("-----------------------------------------------------\n")
print(
    f"To take out a profit of +40% you should sell your {lis_names[user_choice]} at: {round((0.4*purchase_price)+purchase_price,8)} and take out USDT worth of 💲{0.4*usdt}")

print("-----------------------------------------------------\n")
print(
    f"To take out a profit of +60% you should sell your {lis_names[user_choice]} at: {round((0.6*purchase_price)+purchase_price,8)} and take out USDT worth of 💲{0.6*usdt}")

print("-----------------------------------------------------\n")
print(
    f"To take out a profit of +80% you should sell your {lis_names[user_choice]} at: {round((0.8*purchase_price)+purchase_price,8)} and take out USDT worth of 💲{0.8*usdt}")

print("-----------------------------------------------------\n")
print(
    f"For 2x sell at {2*purchase_price} and take out USDT worth of 💲{usdt}")

print("-----------------------------------------------------\n")
print(
    f"For 3x sell at {3*purchase_price} and take out USDT worth of 💲{2*usdt}")

print("-----------------------------------------------------\n")
print(
    f"For 4x sell at {4*purchase_price} and take out USDT worth of 💲{3*usdt}")

""" 

python .\sell_zone.py --purchasePrice 39.301 --filled 7.633
"""
