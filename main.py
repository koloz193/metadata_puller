from web3 import Web3
import requests

RPC_URL = ""

CONTRACT_ADDRESS = "0xb932a70A57673d89f4acfFBE830E8ed7f75Fb9e0"
START_TOKEN_ID = 4435 # first token id on this contract
END_TOKEN_ID = 4435

if __name__ == '__main__':
  w3 = Web3(Web3.HTTPProvider(RPC_URL))
  erc721 = w3.eth.contract(
    address=w3.toChecksumAddress(CONTRACT_ADDRESS), 
    abi=[
        { 
            "inputs": [{ "internalType": "uint256", "name": "tokenId", "type": "uint256" }],
            "name": "tokenURI",
            "outputs": [{"internalType": "string","name": "","type": "string"}],
            "stateMutability": "view",
            "type": "function"
        }
    ]
  )

  for i in range (START_TOKEN_ID, END_TOKEN_ID + 1):
    print(f"Processing tokenId: {i}")
    uri = erc721.functions.tokenURI(i).call()
    r = requests.get(uri)

    with open(f"output/{i}.json",'wb') as f:
        f.write(r.content)
