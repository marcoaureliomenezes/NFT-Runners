//SPDX-License-Identifier: MIT
pragma solidity 0.8.13;

import "./NftRunners.sol";


contract NftRunnersFactory {

    NftRunners[] public nftRunnersArray;
    address public factoryDeployer;

    constructor() public {
        factoryDeployer = msg.sender;
    }

    function createNftRunner(uint64 _subscriptionId, address _vrfCoordinator, bytes32 _keyHash, uint32 _callbackGasLimit, uint16 _requestConfirmations) public returns (address) {
        NftRunners nftRunners = new NftRunners(_subscriptionId, _vrfCoordinator, _keyHash, _callbackGasLimit, _requestConfirmations);
        nftRunnersArray.push(nftRunners);
        return address(nftRunners);
    }

   

}