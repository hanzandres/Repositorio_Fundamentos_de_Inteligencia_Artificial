assistencia = float(input("ingrese asistencia:"))
promedio = float(input("ingrese promedio:"))
proyecto = input("entrego proyecto:").lower()
dual = input("es dual").lower()

p = assistencia > 80 
q = promedio > 8
r = proyecto == "si"
d = dual == "si"

resultado = p and q and r
resultado_dual = p and q and r or d

print("tu asitencia es:",p)
print("tu promedio es:",q)
print("entegastes proyecto",r)

if resultado: 
    print("el alumno pasa")
elif resultado_dual:
    print("es dual")
else:
    print("no pasa")
    
    
if d:
    print("El alumno es dual (pasa automáticamente).")
elif p and q and r: 
    print("El alumno pasa.")
else:
    print("No pasa.")