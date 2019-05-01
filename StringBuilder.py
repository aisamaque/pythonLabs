class StringBuilder(object):

	def __init__(self):
		self.stringList=[]

	def Append(self, string):
		if self.Count == 0:
			return self.AppendLine(string)
		else:
			return self.AppendLine(self.stringList.pop() + string)

	def Format(self, formats):
		self.AppendLine(self.stringList.pop().format(*formats))
		return self
	
	def At(self, index, oldIndex = -1):
		self.AppendLineInIndex(index, self.stringList.pop(oldIndex))
		return self

	def AppendLine(self, string=""):
		self.stringList.append(string) 
		return self
	
	def AppendLineInIndex(self, string, index):
		self.stringList.insert(index, string) 
		return self
	
	def AppendLineAfterLast(self, string):
		self.AppendLineInIndex(string, self.Count-1)
		return self

	@property
	def Count(self):
		return len(self.stringList)

	def ToString(self):
		return "\n".join(self.stringList)

	def ToList(self):
		return self.stringList