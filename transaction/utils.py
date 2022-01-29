from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from . import CONFIG, coin_funs

def make_transaction():
    rpc_connection = AuthServiceProxy(CONFIG.IP)
    #получем адресс отправки
    to_address = rpc_connection.getnewaddress()
    #получем utxo транзакции
    utxo = coin_funs.get_utxo(CONFIG.MY_ADDRESS)
    
    #создаем сеть для транзакции
    net = coin_funs.create_net()
    #создаем транзакцию с сетью
    unsigned_tx = coin_funs.create_tx_from_network(utxo, net, to_address)
    
    #преобразуем транзакцию в hex
    unsign_hex = unsigned_tx.as_hex()
    #декодируем транзакцию для проверки корректности    
    #txid = rpc_connection.decoderawtransaction(unsign_hex)
    
    #подписываем транзакцию
    hex_ = rpc_connection.signrawtransactionwithkey(unsign_hex, CONFIG.SECRET_KEY)
    
    #получем само значение hex
    hex_value = hex_['hex']
    
    try:
        id_transaction = rpc_connection.sendrawtransaction(hex_value)
        #print("ID - {}".format(id_transaction))
    except JSONRPCException as e:
        id_transaction = e.message
        return id_transaction
    
    return str(id_transaction)


