from StringBuilder import StringBuilder
from CodeBuilder import CodeBuilder
from PythonBuilder import PythonBuilder

# sb = CodeBuilder()

# sb.AppendComand("teste")\
#     .AppendComandFormat("{0}{1}", ["#comentario\n","array"])

# sb.AppendComment("iniciando copias")
# sb.AppendLine()

# sb.AppendCopyCommand(["origem", "destino"]).WithComment("testando copy").WithComment("Testando nova linha")\
#     .AppendRemoveCommand(["origem", "destino"])\
#     .AppendCreateFolderCommand(["origem", "destino"])

pb = PythonBuilder()

pb.AppendLine("Teste Python")

print(pb.ToString())