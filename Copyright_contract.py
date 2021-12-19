import solcx
from logzero import logger
from web3 import Web3
from solcx import compile_files

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
w3.eth.defaultAccount = w3.eth.accounts[0]

print('install solcx 0.8.0..')
solcx.install_solc('0.8.0')
def deploy(contract_file, contract_name):

	compiled_sol = compile_files([contract_file])
	interface = compiled_sol['{}:{}'.format(contract_file, contract_name)]
	
	contract = w3.eth.contract(abi = interface['abi'], 
										bytecode = '0x'+interface['bin'], 
										bytecode_runtime=interface['bin-runtime'])

	tx_hash = contract.constructor().transact()
	logger.info(f'tx_hash: {tx_hash}')

	tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
	logger.info(f'Copyright_tx_receipt: {tx_receipt}')
	
	contract_address = tx_receipt['contractAddress']
	logger.info(f'Copyright_contract_address: {contract_address}')
	
	contract_instance = contract(contract_address)
	logger.info(f'Copyright_contract_instance: {contract_instance}')

	return contract_instance
