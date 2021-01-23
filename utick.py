from brownie import *
import time
import sys

network.connect( 'alchemy' )

i = str(sys.argv[1])

contract = web3.toChecksumAddress(i)
contract = Contract.from_explorer( contract )

token1 = contract.token1()
token0 = contract.token0()

token1_c = Contract.from_explorer( token1 )
token0_c = Contract.from_explorer( token0 )

decimals1 = token1_c.decimals()
decimals0 = token0_c.decimals()

symbol1 = token1_c.symbol()
symbol0 = token0_c.symbol()

while True:
    reserve1 = contract.getReserves()[1]
    reserve0 = contract.getReserves()[0]
    reserve1 = int( reserve1 ) / 10 ** int( decimals1 )
    reserve0 = int( reserve0 ) / 10 ** int( decimals0 )
    ts = int(time.time())
    price = reserve0 / reserve1

    print( f'{ts}:  {price:.8f} {symbol1}/{symbol0}' )

    with open( f'{symbol1}_{symbol0}.csv', 'a' ) as f:
        f.write( f'{ts},{price:.8f} \n' )

    time.sleep( 0.5 )
