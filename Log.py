#
# https://github.com/jgarzik/pynode/blob/master/Log.py
#

import sys

class Log(object):
		def __init__(self, filename=None):
			if filename is not None:
					#self.fh = open(filename, 'w+', 0)
					self.fh = open(filename, 'w+')
			else:
					self.fh = sys.stdout

		def write(self, msg):
			line = "%s\n" % msg
			#print(msg)
			self.fh.write(line)