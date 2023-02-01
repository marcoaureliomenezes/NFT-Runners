from brownie import NftRunners, NftRunnersFactory, config, network
from brownie import network, accounts, config
from scripts.utils import get_account


def deploy_nft_runners():
    env_vars = config["networks"][network.show_active()]
    subscription_id = 9033
    callback_gas_limit = 2500000
    request_confirmations = 3
    owner = get_account()
    vrf_coordinator = env_vars["vrfCoordinator"]
    key_hash = env_vars["keyHash"]
    is_verified = env_vars.get("verify")
    args = [subscription_id, vrf_coordinator, key_hash, callback_gas_limit, request_confirmations]
    tx = NftRunners.deploy(*args, {'from': owner}, publish_source=is_verified)
    return tx  

def deploy_nft_runners_factory():
    env_vars = config["networks"][network.show_active()]
    request_confirmations = 3
    owner = get_account()
    vrf_coordinator = env_vars["vrfCoordinator"]
    key_hash = env_vars["keyHash"]
    is_verified = env_vars.get("verify")
    tx = NftRunnersFactory.deploy(vrf_coordinator, key_hash, request_confirmations, {'from': owner}, publish_source=is_verified)
    return tx  


def main():
    res = deploy_nft_runners()
    print(res)