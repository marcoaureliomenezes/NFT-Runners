from brownie import NftRunners, NftRunnersFactory, config, network
from brownie import network, config
from scripts.utils import get_account


def create_nft_runners(char_id=0):
    env_vars = config["networks"][network.show_active()]
    subscription_id=9033
    callbackGasLimit = 2500000
    owner = get_account()
    #tx = NftRunnersFactory[-1].createNftRunner(subscription_id, callbackGasLimit, {"from": owner})
    children = NftRunnersFactory[-1].nftRunnersArray(0)
    nft_runners = NftRunners.at(children)
    nft_runners.safeMint(owner, char_id, {"from": owner})
    # NftRunners.publish_source(NftRunners.at(children))
    print(children)



def main():
    res = create_nft_runners(2)
    print(res)