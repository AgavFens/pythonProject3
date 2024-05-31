from web3 import Web3
from web3.middleware import geth_poa_middleware
from agavking import abi, address

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

def main():
    addr1 = w3.to_checksum_address('0x236702918254ccfc43ff0a166c9facdb497762b4')
    addr2 = w3.to_checksum_address('0xaa5e98377abf20928b70c9c9c224c98f5b6f63c7')
    addr3 = w3.to_checksum_address('0x87620de0cf895ca1f8a64c88175cbfefb414ff08')
    addr4 = w3.to_checksum_address('0xdcfdf55a7ec00b3442e646ad49adac19b1d0ceb3')
    addr5 = w3.to_checksum_address('0x24e10db3036dd69888b2c3f93635a8e268264ed7')

    print(f"Первый акк: {w3.eth.get_balance(addr1)}\n"
          f"Второй акк: {w3.eth.get_balance(addr2)}\n"
          f"Третий акк: {w3.eth.get_balance(addr3)}\n"
          f"Четвертый акк: {w3.eth.get_balance(addr4)}\n"
          f"Пятый акк: {w3.eth.get_balance(addr5)}\n")

if __name__ == '__main__':
    main()
