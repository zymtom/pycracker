print 'You\'re about to start your cracking session.'
import os
import threading

def include(filename):
    if os.path.exists(filename): 
        execfile(filename)
		return True
	else:
		return False

class PyCracker:
	def __init__(self):
		self.proxyMethod = ''
		self.threadAmount = ''
		self.crackingMethod = ''
		self.list = ''
		self.userWordlist = ''
		self.passwordWordlist = ''
		self.debug = 0
	def is_number(n):
		try:
			int(n)
			return True
		except ValueError:
			if getDebug():
				print "Invalid number"
			return False
			
	def setThreads(threadAmount):
		if is_number(threadAmount):
			self.threadAmount = threadAmount
			return True
		else:
			if getDebug():
				print "Invalid amount"
			return False
			
	def setConfig(configName):
		if include(configName):
			try:
				checkacc()
				return True
			except Exception:
				if getDebug():
					print "The checkacc() function does not exist in your file."
				return False
		else:
			if getDebug():
				print "Something went wrong when including the config file."
			return False
			
	def setProxyMethod(methodValue):
		self.proxyMethod = methodValue
		return True
		
	def setCrackingMethod(methodValue):
		if methodValue == 'wordlist':
			self.crackingMethod = 2
			return True
		elif methodValue == 'combolist':
			self.crackingMethod = 1
			return True
		elif methodValue == 'brute':
			self.crackingMethod = 3
			return True
		elif is_number(methodValue):
			self.crackingMethod = methodValue
			return True
		else:
			if getDebug():
				print "No valid values. Lookup documentation or refer to the code."
			return False
		
	def setComboList(combolist):
		try:
			combolist = open(combolist, 'r')
			self.list = combolist.readlines()
			return True
		except Exception:
			return False
	def setUserWordlist(userlist):
		try:
			userlist = open(userlist, 'r')
			self.userWordlist = userlist.readlines()
			return True
		except Exception:
			return False
	def setUserWordlist(passwordlist):
		try:
			password = open(passwordlist, 'r')
			self.passwordWordlist = passwordlist.readlines()
			return True
		except Exception:
			return False
	def setDebug(i):
		self.debug = i
	def getDebug():
		if self.debug == 1:
			return True
		elif self.debug == 0:
			return False
		return self.debug
	
	def start():
		for x in range(self.threadAmount):
			if self.crackingMethod == 1:
				threading.Thread(target=threadsCombo(self.amountOfCombos/self.threadAmount, x)).start()
			elif self.crackingMethod == 2:
				#Do something here
			elif self.crackingMethod == 3:
				#Do something here
			
	def threadsCombo(combosForThread, multiplier):
		if self.crackingMethod == 1:
			startindex = combosForThread*multiplier
			while 1:
				for i in range(combosForThread):
					combo = self.list[startindex+i]
					checkacc(combo.split(":")[0], combo.split(":")[0])
					startindex = startindex+1
				if startindex-(combosForThread*multiplier) == combosForThread:
					break
	def threadsWordlist():
		#Do something here
			
