from time import time
import hashlib
import json

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # init
        self.new_block(proof=1, previous_hash=100)

    def new_transaction(self, sender, receiver, amount):
        return self.current_transactions.append({
            "sender": sender,
            "receiver": receiver,
            "amount": amount
        })

    def generate_proof(self, last_proof):
        proof = 0

        while self.valid_proof(last_proof, proof) is False:
            # print(proof)
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = "{0}{1}".format(last_proof, proof).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        # print("guess_hash {}".format(guess_hash))
        return guess_hash[:4] == "0000"

    def new_block(self, proof, previous_hash=None):

        block = {
            "index": len(self.chain) + 1,
            "transactions": self.current_transactions,
            "timestamp": time(),
            "previous_hash": previous_hash or self.hash(self.last_block),
            "proof": proof
        }

        self.current_transactions = []

        self.chain.append(block)

        return block

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]
