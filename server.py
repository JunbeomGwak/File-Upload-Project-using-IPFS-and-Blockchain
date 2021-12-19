import os
import json
import hashlib
import Owner_contract
import ipfs
from werkzeug.utils import secure_filename
from web3 import Web3
from logzero import logger
from flask import Flask, request, Response
from flask_socketio import SocketIO, emit
from os.path import getsize
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test_password'
socketio = SocketIO(app, binary=True)

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545')) # can be fix
w3.eth.defaultAccount = w3.eth.accounts[0]

CON_IDX = None

UPLOAD_FOLDER = './savedfile/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'py'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # limit max size(16MB)
Copy = list(range(5))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#return file hash
def sha256_checksum(filename, block_size=65536):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)

    return sha256.hexdigest()

@socketio.on('uploadfile', namespace='/flask')
def uploadfile(data, filename):
	global Copy
	
	#recv file and save
	filename = secure_filename(filename)
	path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
	with open(path, mode='wb') as f:
		f.write(data)
	f.close()

	ipfs_hash = ipfs.addipfsfile(filename)
	filehash = sha256_checksum(path)
	filesize = getsize(filename)
	owner = Copy[4]
	fileupload_tx = CON_IDX.functions.fileupload(owner, filehash, filename, filesize).transact()
	fileupload_tx = Web3.toHex(fileupload_tx)
	timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	copyright = CON_IDX.functions.addCopyright(Copy[0], Copy[1], Copy[2], Copy[3], timestamp, owner, filehash).transact()

	emit('recvdata', (filename, fileupload_tx, ipfs_hash, copyright, filehash), namespace='/flask')

	return Response(200)

@app.route('/getfileowner', methods=['POST'])
def getfileowner():
	if request.method == 'POST':
		global CON_IDX
		filehash = request.form['filehash']
		fileowner = CON_IDX.functions.getOwnerName().transact()
		fileowner_receipt = w3.eth.getTransactionReceipt(fileowner)
		fileowner = fileowner_receipt['from']
		return fileowner

@socketio.on('recvcopyright', namespace='/flask')
def recvf(data):
	global Copy
	copy = json.loads(data)

	Copy[0] = str(copy['Artist'])
	Copy[1] = str(copy['Createdtime'])
	Copy[2] = str(copy['Type'])
	Copy[3] = str(copy['Description'])
	Copy[4] = str(copy['Owner'])

if __name__ == '__main__':
	CON_IDX = Owner_contract.deploy("smartcontract.sol", "StorefileHash") 
	socketio.run(app, port=5000)

