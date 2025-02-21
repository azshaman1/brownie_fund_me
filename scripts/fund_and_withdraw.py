from brownie import FundMe
from scripts.helpful_scripts import get_account

def fund():
    fund_me = FundMe[-1]
    print(f"FAW-fund_me is {fund_me}")
    account = get_account()
    print(f"FAW-account is {account}")
    entrance_fee = fund_me.getEntranceFee()
    # entrance_fee = 25000000000000000
    print(entrance_fee)
    print(f"FAW-The current entry fee is {entrance_fee}")
    print("FAW-Funding")
    fund_me.fund({"from": account, "value": entrance_fee})

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from": account})
    print("FAW-Withdrawing")

# 0.025000000000000000
def main():
    fund()
    withdraw()