from StringBuilder import StringBuilder

class PythonBuilder(StringBuilder): 

    def __init__(self):
        self.stringList=[]
        self.indentModel="\t"
        self.commentModel="#"
        self.level =0
        self.builderList=[]
    
    @property
    def Level(self):
        return self.level
    
    def AppendBuilder(self,builder):
        for a in builder.List:
            self.AppendLine("{0}{1}").Format([str((self.Level + 1) * self.indentModel),a])

    # def ToString(self):
    #     for a in self.builderList:
    #         print("{0}{1}".format(a.level*a.indentModel,a.ToString()))
    #         for b in a.builderList:
    #             b.ToString()
