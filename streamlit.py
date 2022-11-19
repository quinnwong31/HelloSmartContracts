import json
from web3 import Web3
import streamlit as st

contract = ''

# 
# Initialize the smart contract. 
#
def init_smartcontract(web3):
    # Set default account for paying gas fees
    web3.eth.defaultAccount = web3.eth.accounts[0]

    # Deploy smart contract 
    abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]');
    bytecode = '608060405234801561001057600080fd5b506040805190810160405280600581526020017f48656c6c6f0000000000000000000000000000000000000000000000000000008152506000908051906020019061005c929190610062565b50610107565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106100a357805160ff19168380011785556100d1565b828001600101855582156100d1579182015b828111156100d05782518255916020019190600101906100b5565b5b5090506100de91906100e2565b5090565b61010491905b808211156101005760008160009055506001016100e8565b5090565b90565b61046f806101166000396000f3fe608060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063a41368621461005c578063cfae321714610124578063ef690cc0146101b4575b600080fd5b34801561006857600080fd5b506101226004803603602081101561007f57600080fd5b810190808035906020019064010000000081111561009c57600080fd5b8201836020820111156100ae57600080fd5b803590602001918460018302840111640100000000831117156100d057600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290505050610244565b005b34801561013057600080fd5b5061013961025e565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561017957808201518184015260208101905061015e565b50505050905090810190601f1680156101a65780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b3480156101c057600080fd5b506101c9610300565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156102095780820151818401526020810190506101ee565b50505050905090810190601f1680156102365780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b806000908051906020019061025a92919061039e565b5050565b606060008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102f65780601f106102cb576101008083540402835291602001916102f6565b820191906000526020600020905b8154815290600101906020018083116102d957829003601f168201915b5050505050905090565b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156103965780601f1061036b57610100808354040283529160200191610396565b820191906000526020600020905b81548152906001019060200180831161037957829003601f168201915b505050505081565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106103df57805160ff191683800117855561040d565b8280016001018555821561040d579182015b8281111561040c5782518255916020019190600101906103f1565b5b50905061041a919061041e565b5090565b61044091905b8082111561043c576000816000905550600101610424565b5090565b9056fea165627a7a72305820280206cc425ea4191575111dd13cb9ade1ceab18c35ab84ffe67740e06ecab790029'
    Greeter = web3.eth.contract(abi=abi, bytecode=bytecode)

    # Create smart contract
    tx_hash = Greeter.constructor().transact()

    # Get transaction receipt
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    # print(tx_receipt)

    # Get reference to smart contract
    contract = web3.eth.contract(
        address=tx_receipt.contractAddress,
        abi=abi
    )

    return contract

# Connect to Ganache blockchain
ganache_url = 'http://127.0.0.1:7545'
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Init smart contract
contract = init_smartcontract(web3)

# 
# UI for Hello World for Smart Contracts
#
st.write("# Hello World for Smart Contracts")

greeting = st.text_input('Greeting', 'Hello World')

# Call 'setGreeting()' function
tx_hash = contract.functions.setGreeting(greeting).transact()
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

st.write('tx_hash', tx_hash)
st.write('tx_receipt', tx_receipt)
st.write('contract.functions.greet()', contract.functions.greet().call())

# st.write('The current greeting is', greeting)

# (contract.functions.greet().call())
