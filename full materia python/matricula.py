#matricula 
rut = input("Ingrese rut apoderado: ") 
nomAlum = input("ingrese el nombre del alumno: ") 
curso = input("Ingrese curso al cual el alumno debe matricularse: ") 
matricula = int(25000) 
mensualidad = int(30000) 
resultadoAnual = (mensualidad*10)+matricula

print(f"-----Detalle Anualidad Colegio----") 
print(f"NOMBRE ALUMNO:{nomAlum}") 
print(f"RUT APODERADO: {rut}") 
print(f"CURSO MATRICULADO: {curso}") 
print(f"VALOR MATRICULA: {matricula}") 
print(f"VALOR MENSUALIDAD: {mensualidad}") 
print(f"VALOR TOTAL A PAGAR: {resultadoAnual}")