import inspect
import sys
import os
currentFolder = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(currentFolder, '../util'))
sys.path.insert(0, os.path.join(currentFolder, '../moveNearReplace'))
import color
import os
import util
import filer2 as filer
class Iterations:


	def __init__(self):
		self.testFolder()


	def dataFile(self):
		return os.path.join (self.dataFolder, 'iterations.data')


	def currentFile(self):
		return os.path.join (self.dataFolder, 'current.data')


	def testFolder(self):
		self.dataFolder = os.path.join(currentFolder, 'testData')


	def realFolder(self):
		self.dataFolder =  os.path.join(currentFolder, 'data')


	def add(self, filenameLine):
		data = self.all()
		data = data + [filenameLine]
		filer.write(self.dataFile(), data)


	def remove(self, filenameLine):
		data = self.all()
		exist = filenameLine in data
		if exist:
			result = self.next()
			data.remove(filenameLine)
			self.setAll(data)
			return result
		else:
			return None


	def all(self):
		data = filer.readToObj(self.dataFile())
		if not data:
			data = []
		return data


	def setAll(self, li):
		filer.write(self.dataFile(), li)


	def clear(self):
		filer.write(self.dataFile(), [])


	def currentSet(self, current):
		filer.write(self.currentFile(), [current])


	def currentGet(self):
		data = filer.readToObj(self.currentFile())
		data = data[0] if len(data) else None
		return data


	def nextPrevTop(self, move):
		current = self.currentGet()
		allList = self.all()
		if not len(allList):
			return None
		if move == "top":
			chooseFileNamePath = allList[-1]
		else:
			inlist = util.itemInList(current, allList)
			if inlist:
				currentIndex = allList.index(current) 
				if (move == "next"):
					chooseNumber =  currentIndex + 1
					if chooseNumber >= len(allList):
						chooseNumber = 0
				elif move == "prev":
					chooseNumber =  currentIndex - 1
					if chooseNumber < 0:
						chooseNumber = -1
				chooseFileNamePath = allList[chooseNumber]
			elif len(allList):
				chooseFileNamePath = allList[-1]
			else:
				chooseFileNamePath = current
		self.currentSet(chooseFileNamePath)
		return chooseFileNamePath


	def next(self):
		return self.nextPrevTop("next")

	def status(self):
		current = self.currentGet()	
		allItems = self.all()
		if current in allItems:
			index = allItems.index(current)
			statusStr = '{0} of {1}'.format(index+1, len(allItems))
		else:
			statusStr = "no file"
		return statusStr	


	def prev(self):
		return self.nextPrevTop("prev")


	def top(self):
		return self.nextPrevTop("top")


	def command(self, commandName, arg=None):
		method = getattr(self, commandName)
		args = inspect.getargspec(method).args
		argsLen = len(args)
		if arg and argsLen == 2:
			return method(arg)
		else:
			return method()