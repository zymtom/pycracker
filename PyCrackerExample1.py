import os
def include(filename):
    if os.path.exists(filename): 
        execfile(filename)
		return True
	else:
		return False
include("PyCrackerBase.py")

cracker = PyCracker()
cracker.setThreads(1)
cracker.setConfig('/configs/origin.py')
