#!/usr/bin/python
import argparse
import json
import web3
from eth_account import Account
import secrets

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', type=str, help='Path to output wallets file', default='wallets.json')

def __main__():

    wallets = []

    args = parser.parse_args()

    ofile = open(args.output, 'w')

    print('How many wallets to you want to create?')
    wallets_count = input()
    wallets_count = int(wallets_count)

    for w in range(wallets_count):
        w = secrets.token_hex(32)
        private_key = "0x" + w
        acct = Account.from_key(private_key)
        print("Address:", acct.address)
        wallets.append({'address':acct.address, 'private_key': private_key})

    wallets_to_json = json.dumps(wallets)
    ofile.write(wallets_to_json)

if __name__ == '__main__':
    __main__()