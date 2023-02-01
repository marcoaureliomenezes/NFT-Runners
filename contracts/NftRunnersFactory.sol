//SPDX-License-Identifier: MIT
pragma solidity 0.8.13;

import "./NftRunners.sol";


contract NftRunnersFactory {

    NftRunners[] public nftRunnersArray;
    address public factoryDeployer;
    address vrfCoordinator;
    bytes32 keyHash;
    uint16 requestConfirmations;

    constructor(address _vrfCoordinator, bytes32 _keyHash, uint16 _requestConfirmations) public {

        factoryDeployer = msg.sender;
        vrfCoordinator = _vrfCoordinator;
        keyHash = _keyHash;
        requestConfirmations = _requestConfirmations;
    }

    function createNftRunner(uint64 _subscriptionId, uint32 _callbackGasLimit) public payable returns (address) {
        NftRunners nftRunners = new NftRunners(_subscriptionId, vrfCoordinator, keyHash, _callbackGasLimit, requestConfirmations);
        nftRunnersArray.push(nftRunners);
        return address(nftRunners);
    }

   

}