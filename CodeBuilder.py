from StringBuilder import StringBuilder

class CodeBuilder(StringBuilder): 
    
    def __init__(self):
        self.stringList=[]
        self.commentModel="#"

    def AppendComand(self,comand):
        self.AppendLine(comand)
        return self
    
    def AppendComandFormat(self, comand, formats, index =0):
        if index == -1:
            self.AppendLineAfterLast(comand.format(*formats))
        else:
            self.AppendLine(comand).Format(formats)
        return self
    
    def AppendCopyCommand(self, args):  
        self.AppendComandFormat("cp {0} {1}",args)
        return self

    def AppendRemoveCommand(self, args):  
        self.AppendComandFormat("rm {0}",args)
        return self

    def AppendCreateFolderCommand(self, args):  
        self.AppendComandFormat("mkdir {0}",args)
        return self

    def WithComment(self, comment):
        self.AppendComandFormat("{0}{1}",[self.commentModel, comment], -1)
        return self
    
    def AppendComment(self, comment):
        self.AppendComandFormat("{0}{1}",[self.commentModel, comment])
        return self


