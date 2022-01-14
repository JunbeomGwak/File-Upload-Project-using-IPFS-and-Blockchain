import ipfshttpclient
from logzero import logger
def addipfsfile(filepath):
    with ipfshttpclient.connect() as client:
	    hash = client.add(filepath)
	
    logger.debug(f"IPFS Hash: {hash['Hash']}")
    return hash['Hash']

    

