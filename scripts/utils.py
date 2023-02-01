from brownie import config, network
from brownie import network, accounts, config

NON_FORKED_LOCAL_CHAIN = ["development", "ganache-dadaia"]
FORKED_LOCAL_CHAIN = ["mainnet-fork"]
LOCAL_CHAIN_ENV = NON_FORKED_LOCAL_CHAIN + FORKED_LOCAL_CHAIN



def get_account(**kwargs):
    is_local = network.show_active() in LOCAL_CHAIN_ENV
    if is_local and kwargs.get('index'): return accounts[kwargs["index"]]
    elif is_local and not kwargs.get('index'): return accounts[0]
    elif not is_local and kwargs.get("id"): return accounts.load(kwargs["id"])
    else: return accounts.add(config["wallets"]["from_key"])


def get_vrf_coordinator():
    if network.show_active() in LOCAL_CHAIN_ENV:
        print("DEPLOY MOCK VRF COORDINATOR")
    else:
        return config["networks"][network.show_active()]["vrfCoordinator"]