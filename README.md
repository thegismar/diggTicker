# Digg Ticker

Get free web3 node access through infura: https://infura.io -> register -> settings -> keys -> http endpoints for mainnet -> that will be the <INFURA HOST URL> 

Next steps:

* `pip install -r requirements`
* `brownie add networks Ethereum alchemy chainid=1 host=<INFURA HOST URL> explorer=https://api.etherscan.io/api`
* `python ticker.py`

if you use another name for the brownie network change it in the .env file
