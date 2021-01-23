# White Paper

The future chain is a cryptographically linked chan (using only hashing) that is used to confirm th validity of an event that will happen in the future. This is done by revealing the hash of a past link with some salt in it and using that salt to verify the validity of a future event. The flow for creating a future chain is as follows:

1. Make a genesis message
2. Hash salt + message (called future_hash)
3. Send message + future_hash packet (genesis event)
4. Make a new message
5. Hash the salt + previous future_hash + new message (new future_hash)
6. Send message + new future_hash + past_salt 
7. repeat 4 - 7

Flow for verifying messages on the future chain:

1. Read **current** packet (message + future_hash + past_salt)
2. Read the **previous** packet in the chain (message + future_hash + past_salt)
3. Hash the previous message and current past_salt and check it is equal to the previous future_hash
4. **current** = **previous**
5. repeat *1* - *5* until genesis event

This can also be done in reverse order starting at the genesis event

## Proof of Concept 

To see a really basic implementation of adding messages to a future chain, run:

```
python future_chain/chain.py
python future_chain/chain.py
python future_chain/chain.py
```
