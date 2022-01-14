import socketio
import os
import requests
import hashlib
import json
import collections
from tkinter.filedialog import askopenfilename
from tkinter import *
from logzero import logger

sio = socketio.Client()
sio.connect('http://127.0.0.1:5000', namespaces='/flask')
url = 'http://127.0.0.1:5000/'
window = Tk()
window.title("Blockchain Copyright")

filepath = None
obj = collections.OrderedDict()

def main_destory():
	window.quit()
	window.destroy()

def InputCopyright():
	newWindow = Toplevel(window)
	newWindow.title("Input Copyright")

	txt1 = StringVar()
	txt2 = StringVar()
	txt3 = StringVar()
	txt4 = StringVar()
	txt5 = StringVar()

	def destory():
		newWindow.destroy()

	sio.on('recvfile', namespace='/flask')
	def store():
		global obj
		obj['Artist'] = txt1.get()
		obj['Createdtime'] = txt2.get()
		obj['Type'] = txt3.get()
		obj['Description'] = txt4.get()
		obj['Owner'] = txt5.get()
		
		Copyright = json.dumps(obj, ensure_ascii=False, sort_keys=False)
		sio.emit('recvcopyright', Copyright, namespace='/flask')

	Label(newWindow, text="Input Artist name: ").pack()
	Entry(newWindow, textvariable=txt1).pack()
	
	Label(newWindow, text="Input Created_time: ").pack()
	Entry(newWindow, textvariable=txt2).pack()
	
	Label(newWindow, text="Input Type: ").pack()
	Entry(newWindow, textvariable=txt3).pack()

	Label(newWindow, text="Input Description: ").pack()
	Entry(newWindow, textvariable=txt4).pack()

	Label(newWindow, text="Input Owner name: ").pack()
	Entry(newWindow, textvariable=txt5).pack()
	
	Button(newWindow, text="Submit", command=lambda:[store(), destory()]).pack() # store() -> destory()

def Load():
	global filepath
	filepath = askopenfilename()
	filename = str(os.path.basename(filepath))
	logger.info(f'filename: {filename}')
	with open(filepath, mode='rb') as f:
		data = f.read()

	sio.emit('uploadfile', (data, filename), namespace='/flask')

def getfileowner():
	global filepath
	filehash = StringVar()
	getfilewindow = Toplevel(window)
	getfilewindow.title("Input filehash")

	def destory():
		getfilewindow.destroy()
	
	def send():
		value = {'filehash': filehash.get()}
		requests.post(url+'getfileowner', data=value)

	Label(getfilewindow, text="Input filehash: ").pack()
	Entry(getfilewindow, textvariable=filehash).pack()

	Button(getfilewindow, text="Submit", command=lambda:[send(), destory()]).pack()

def get_file_hash(filepath):
	data = filepath.read() 
	hash = hashlib.md5(data).hexdigest() 
	return hash

@sio.on('recvdata', namespace='/flask')
def recvdata(*args):
	def destory():
		newWindow.destroy()

	newWindow = Toplevel(window)
	newWindow.title("Recvived Data")
	newWindow.geometry("1000x200")
	
	ipfs_filehash = StringVar()
	filename = StringVar()
	fileupload_tx = StringVar()
	copyright_tx = StringVar()
	filehash = StringVar()

	label = Label(newWindow, textvariable=filename, font=("Times", 14)).pack()
	filename.set(f'Filename: {args[0]}')

	label1 = Label(newWindow, textvariable=fileupload_tx, font=("Times", 14)).pack()
	fileupload_tx.set(f'Fileupload_tx: {args[1]}')
	
	label2 = Label(newWindow, textvariable=copyright_tx, font=("Times", 14)).pack()
	ipfs_filehash.set(f'IPFS_hash: https://gateway.ipfs.io/ipfs/{args[2]}')
	
	label3 = Label(newWindow, textvariable=ipfs_filehash, font=("Times", 14)).pack()
	copyright_tx.set(f'Copyright_tx: 0x{args[3].hex()}')

	label4 = Label(newWindow, textvariable=filehash, font=("Times", 14)).pack()
	filehash.set(f'Filehash: {args[4]}')

	btn = Button(newWindow, text="Close", command=destory)
	btn.pack()

btn1 = Button(window, text="Input Copyright", command=InputCopyright)
btn1.pack()

btn2 = Button(window, text="Open file", command=Load)
btn2.pack()

btn3 = Button(window, text="Get file owner", command=getfileowner)
btn3.pack()

btn4 = Button(window, text="Close", command=main_destory)
btn4.pack()

window.mainloop()
