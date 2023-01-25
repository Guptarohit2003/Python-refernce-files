#ACCOUNT CREATION
'''from algosdk import account, mnemonic

def generate_algorand_keypair():
    private_key, address = account.generate_account()

    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))

generate_algorand_keypair()'''

#CHECKING TEST ALGO(test tokens)
'''from algosdk.v2client import algod

# Connecting to the Algod Client on the Algorand sandbox
algod_address = "http://localhost:4001"
algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algod_client = algod.AlgodClient(algod_token, algod_address)

# Declare your Address
my_address = "SSFXGTBUXO5MNMOJIP7JHQERJI647B4IIISHDLBFKHRGWLINLOCCIDFFOE"

account_info = algod_client.account_info(my_address)
print("Account balance: {} microAlgos".format(account_info.get('amount')))'''

#TRANSACTION
'''from algosdk.future import transaction
from algosdk import constants, mnemonic
from algosdk.v2client import algod
import json
import base64

def getting_started_example():
    # Connect to the Algod Client on the Algorand sandbox
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)

    # Declare your address and passphrase
    my_address = "SSFXGTBUXO5MNMOJIP7JHQERJI647B4IIISHDLBFKHRGWLINLOCCIDFFOE"
    my_passphrase = "fire crystal clown always absorb vanish check chief hobby scheme echo when ghost series casual skin kiss faculty cattle much now blue output abandon shove"

    # Derive your private key from your passphrase
    private_key = mnemonic.to_private_key(my_passphrase)

    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    #params.flat_fee = True
    #params.fee = constants.MIN_TXN_FEE
    receiver = "SNEIYRBB4SL6MIHANPDTN2FPGVJFFNFVKE4SRZHBYQHQ6FE7PXGCEI4VKE"
    note = "First PythonSDK Transaction dood1e".encode()
    amount = 1000000
    unsigned_txn = transaction.PaymentTxn(my_address, params, receiver, amount, None, note)


    # sign transaction
    signed_txn = unsigned_txn.sign(private_key)

    # submit transaction
    txid = algod_client.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))
    
    # wait for confirmation
    try:
        confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)
    except Exception as err:
        print(err)
        return

    account_info = algod_client.account_info(my_address)

    print("Transaction information: {}".format(
        json.dumps(confirmed_txn, indent=4)))
    print("Decoded note: {}".format(base64.b64decode(
        confirmed_txn["txn"]["txn"]["note"]).decode()))
    print("Starting Account balance: {} microAlgos".format(account_info.get('amount')) )
    print("Amount transferred: {} microAlgos".format(amount) )
    print("Fee: {} microAlgos".format(params.fee) )
    print("Final Account balance: {} microAlgos".format(account_info.get('amount')))

getting_started_example()'''

