import json
import hashlib
import random
import pprint



def chain_write(chain_uri, message):
    chain = []
    with open(chain_uri) as chain_file:
        chain: list = json.load(chain_file)
    chain_file.close()


    s_f = open("past_salt.txt", "r")
    past_salt = s_f.read()
    print(past_salt)
    s_f.close()

    salt = str(random.random())
    future_hash = hashlib.sha256((message + salt).encode('utf-8')).hexdigest()

    packet = {
        "message": message,
        "future_hash": future_hash,
        "past_salt": past_salt
    }
    chain.append(packet)
    
    s_f = open("past_salt.txt", "w")
    s_f.write(salt)
    s_f.close()

    

    with open(chain_uri, "w") as chain_file:
        json.dump(chain, chain_file)

chain_write("chain.json", "A nice message")


def read_chain(chain_uri):
    with open(chain_uri) as chain_file:
        chain = json.load(chain_file)
        pprint.pprint(chain)

read_chain("chain.json")