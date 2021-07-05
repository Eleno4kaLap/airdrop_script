from web3 import Web3, HTTPProvider

import config


def sing_send_txn(recipient, nonce):
    transaction = {
            "to": recipient,
            "value": w3.toWei(str(config.VALUE), "ether"),
            "gas": config.GAS,
            "gasPrice": w3.toWei(str(config.GAS_PRICE), "gwei"),
            "nonce": nonce,
            "chainId": config.CHAIN_ID,
        }
    signed = w3.eth.account.sign_transaction(transaction, config.PRIVATE_KEY)
    hash_txn = w3.eth.send_raw_transaction(signed.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(hash_txn)
    return hash_txn


if __name__ == '__main__':
    HTTPProvider = HTTPProvider(config.ETH_PROVIDER)
    w3 = Web3(HTTPProvider)

    nonce = w3.eth.getTransactionCount(config.ADDRESS)
    nonce_list = list(range(nonce, nonce+len(config.RECIPIENTS)))
    result = list(map(sing_send_txn, config.RECIPIENTS, nonce_list))
    print(result)


