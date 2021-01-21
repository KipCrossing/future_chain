import json

def read_chain(chain_uri):
    with open(chain_uri) as chain_file:
        chain = json.load(chain_file)
        print(chain)

read_chain("chain.json")

def chain_write(chain_uri, info_dict):
    chain = []
    with open(chain_uri) as chain_file:
        chain: list = json.load(chain_file)
        chain.append(info_dict)
    chain_file.close()
    with open(chain_uri, "w") as chain_file:
        json.dump(chain, chain_file)

chain_write("chain.json", {"info":10})
