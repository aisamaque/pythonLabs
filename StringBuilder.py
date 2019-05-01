class StringBuilder(object):

	def __init__(self):
		self.stringList=[]
		self.lastIndexChanged=0

	@property
	def Count(self):
		return len(self.List)

	@property
	def List(self):
		return self.stringList

	def Append(self, string):
		if self.Count == 0:
			return self.AppendLine(string)
		else:
			return self.AppendLine(self.List.pop() + string)
	
	def AppendLine(self, string=""):
		self.List.append(string)
		self.lastIndexChanged = self.Count -1
		return self
	
	def Insert(self, string, index):
		self.List.insert(index, string) 
		self.lastIndexChanged = index
		return self

	def Format(self, formats):
		self.List[self.lastIndexChanged] = self.List[self.lastIndexChanged].format(*formats)
		return self
	
	def At(self, index, oldIndex = -1):
		self.Insert(index, self.stringList.pop(oldIndex))
		return self
	
	def AppendLineBeforeLast(self, string):
		self.Insert(string, self.Count-1)
		return self

	def ToString(self):
		return "\n".join(self.List)

	def ToList(self):
		return self.List