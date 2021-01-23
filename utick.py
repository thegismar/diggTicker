from brownie import *
import time
from dotenv import load_dotenv
import os

load_dotenv()

w3 = os.getenv( 'WEB3_PROVIDER' )
network.connect( 'w3 ' )

i = '0x9a13867048e01c663ce8ce2fe0cdae69ff9f35e3'

contract = web3.toChecksumAddress( i )
contract = Contract.from_explorer( contract )

token1 = contract.token1()
token0 = contract.token0()

token1_c = Contract.from_explorer( token1 )
token0_c = Contract.from_explorer( token0 )

decimals1 = token1_c.decimals()
decimals0 = token0_c.decimals()

symbol1 = token1_c.symbol()
symbol0 = token0_c.symbol()


def get_price():
    reserve1 = contract.getReserves()[1]
    reserve0 = contract.getReserves()[0]
    reserve1 = int( reserve1 ) / 10 ** int( decimals1 )
    reserve0 = int( reserve0 ) / 10 ** int( decimals0 )

    ts = int( time.time() )
    price = reserve0 / reserve1

    return f'{ts}:  {price:.8f} {symbol1}/{symbol0}'


if __name__ == '__main__':
    while True:
        print( get_price() )
        time.sleep( 1 )
