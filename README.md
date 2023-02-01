## NFTRunners com Framework Brownie

NFTRunners implementado na penúltima aula do bootcamp Chainlink com as seguintes alterações:


    - Smart Contract NFTRunners Factory implementado.
    - Parâmetrização no construtor de atributos setados como constantes no contrato visto em aula. Especificamente o endereço do VRFCoordinator, Keyhash, CallbackGasLimit e requestConfirmations.
    - Implementação de rotina para realização de deploy dos contratos.
    - Implementação de VRFCoordinator2Mock para realização de testes nas redes mainnet-fork, polygon-mainnet-fork, goerli e 

## Build 

Pasta para dados gerados quando contratos ou interfaces são compiladas.

# Contracts

Pasta onde o brownie procura os smart contracts para compilar.

# Interfaces

Pasta onde o brownie procura os smart contracts para compilar. Após compilação a ABI das interfaces é escrita em build/interfaces.

# Scripts

Diretório onde ficam rotinas escritas em python para realizar o deploy dos smart contracts e também rotinas para interagir com o smart contract via python.

# Tests

Pasta onde são escritos testes

## brownie-config.yml

Arquivo com configurações base para o framework 