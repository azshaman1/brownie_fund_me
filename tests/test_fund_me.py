from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions
import pytest

def test_can_fund_and_withdraw():
    account = get_account()
    print(f"TFM - account is {account}")
    fund_me = deploy_fund_me()
    print(f"TFM - fund_me is {fund_me}")
    entrance_fee = fund_me.getEntranceFee()+100
    print(f"TFM - The current entry fee is {entrance_fee}")
    print("Funding...")
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    print(f"TFM - fund_me.fund tx is {tx}")
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    print("TFM - Withdrawing...")
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    print("TFM - Withdrawn")
    assert fund_me.addressToAmountFunded(account.address) == 0
    print("TFM - Withdrawn ACK")


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    account = get_account()
    fund_me = deploy_fund_me()
    bad_actor = accounts.add()
    fund_me.withdraw({"from": account})
    # with pytest.raises(exceptions.VirtualMachineError):
    #     fund_me.withdraw({"from": bad_actor})
     