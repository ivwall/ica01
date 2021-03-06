import sys
import re

import Log
from bitcoin.core import *
from bitcoinlib.networks import *
#from bitcoin.coredefs import HETWORKS
#from bitcoin.serialize import *


settings = {}

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("Usage: node.py CONFIG-FILE")
		sys.exit(1)

	f = open(sys.argv[1])
	for line in f:
		m = re.search('^(\w+)\s*=\s*(\S.*)$',line)
		if m is None:
			continue
		settings[m.group(1)]=m.group(2)
	f.close()

	if 'host' not in settings:
		settings['host'] = '127.0.0.1'
	if 'port' not in settings:
		settings['port'] = 8333
	if 'rpcport' not in settings:
		settings['rpcport'] = 9332
	if 'db' not in settings:
		#settings['db'] = '/tmp/chaindb'
		#settings['db'] = '/home/dlt01/ica/ica01/chaindb'
		settings['db'] = '/home/dlt01/ica/ica01/chaindb'	
	if 'chain' not in settings:
		settings['chain'] = 'mainnet'
	chain = settings['chain']
	if 'log' not in settings or (settings['log'] == '-'):
		settings['log'] = None

	if ('rpcuser' not in settings or
		'rpcpass' not in settings):
			print("You must set the following in config: rpcuser, rpcpass")
			sys.exit(1)

	settings['port'] = int(settings['port'])
	settings['rpcport'] = int(settings['rpcport'])

	log = Log.Log(settings['log'])

	log.write("\n\n\n\n")

	if chain not in NETWORKS:
		log.write("invalid network")
		sys.exit(1)

	netmagic = NETWORKS[chain]



