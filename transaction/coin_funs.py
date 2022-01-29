from pycoin.networks.bitcoinish import create_bitcoinish_network
from pycoin.coins.tx_utils import create_tx
from pycoin.coins.bitcoin.Tx import Spendable
from pycoin.encoding.hexbytes import h2b, h2b_rev
import requests, json
from . import CONFIG

def get_utxo(address):
    utxo = requests.get(r"https://bcschain.info/api/address/{}/utxo".format(address))
    utxo = json.loads(utxo.text)[0]
    return utxo

def create_net():
    network = create_bitcoinish_network(symbol = 'BCS', network_name = 'Mainnet', subnet_name = 'my', 
        wif_prefix_hex="80", address_prefix_hex="19", pay_to_script_prefix_hex="32",
        bip32_prv_prefix_hex="0488ade4", bip32_pub_prefix_hex="0488B21E",
        bech32_hrp="bc", bip49_prv_prefix_hex="049d7878",
        bip49_pub_prefix_hex="049D7CB2",
        bip84_prv_prefix_hex="04b2430c", bip84_pub_prefix_hex="04B24746",
        magic_header_hex="F1CFA6D3", default_port=3666)
    return network

def create_tx_from_network(utxo, network, address):
    spendables = Spendable(coin_value=CONFIG.SATOSHI+CONFIG.ME+CONFIG.FEE,
                           script = h2b(utxo['scriptPubKey']), 
                           tx_hash = h2b_rev(utxo['transactionId']), 
                           tx_out_index=int(utxo['outputIndex']))
    
    unsigned_tx = create_tx(network, [spendables], [[address, CONFIG.SATOSHI], 
                                                    [CONFIG.MY_ADDRESS, CONFIG.ME]],
                            fee=0.01)

    return unsigned_tx

