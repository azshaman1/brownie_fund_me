from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account, 
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)

def deploy_fund_me():
    account = get_account()
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
        print(f"D_IF-price_feed_address is {price_feed_address}")
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        print(f"D_ELSE-price_feed_address is {price_feed_address}")
        
    fund_me = FundMe.deploy(
        # "0x694AA1769357215DE4FAC081bf1f309aDC325306",
        price_feed_address,
        {"from": account}, 
        publish_source = config["networks"][network.show_active()].get("verify"),
        )
    print(f"D-Contract deployed to fund_me.address {fund_me.address}")
    print(f"D-Contract deployed to fund_me {fund_me}")
    return fund_me


def main():
    deploy_fund_me()

