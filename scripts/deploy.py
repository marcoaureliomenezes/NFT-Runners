from brownie import NftRunners, NftRunnersFactory, config, network
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

def deploy_nft_runners(subscription_id, callback_gas_limit, request_confirmations):
    env_vars = config["networks"][network.show_active()]
    owner = get_account()
    vrf_coordinator = env_vars["vrfCoordinator"]
    key_hash = env_vars["keyHash"]
    is_verified = env_vars.get("verify")
    args = [subscription_id, vrf_coordinator, key_hash, callback_gas_limit, request_confirmations]
    tx = NftRunners.deploy(*args, {'from': owner}, publish_source=is_verified)
    return tx  


def deploy_nft_runners_factory(subscription_id, callback_gas_limit, request_confirmations):
    env_vars = config["networks"][network.show_active()]
    owner = get_account()
    vrf_coordinator = env_vars["vrfCoordinator"]
    key_hash = env_vars["keyHash"]
    is_verified = env_vars.get("verify")
    tx = NftRunnersFactory.deploy({'from': owner}, publish_source=is_verified)
    return tx  

def main():
    subscription_id=9033
    callbackGasLimit = 2500000
    requestConfirmations = 3
    res = deploy_nft_runners_factory(subscription_id, callbackGasLimit, requestConfirmations)
    print(res)