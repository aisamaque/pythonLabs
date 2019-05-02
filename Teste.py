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

pb.AppendLine("if teste:")

pb1 = PythonBuilder()
pb2 = PythonBuilder()
pb3 = PythonBuilder()
pb1.AppendLine("pass")
pb1.AppendLine("for i in b:")
pb2.AppendLine("print('a')").AppendLine("if b:")
pb3.Append("ue")

pb2.AppendBuilder(pb3)
pb1.AppendBuilder(pb2)
pb.AppendBuilder(pb1)

pb.AppendLine("print")

print(pb.ToString())