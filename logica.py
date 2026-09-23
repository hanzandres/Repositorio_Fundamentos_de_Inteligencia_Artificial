asistencia = float(
    input("Ingresa el porcentaje de asistencia: ")
)

promedio = float(
    input("Ingresa el promedio: ")
)

proyecto = input(
    "¿Entregó el proyecto? (si/no): "
).lower()

autorizacion = input(
    "¿Tiene autorización especial? (si/no): "
).lower()

lista_oficial = input("esta en la lista oficial").lower()

adeudo = input(
    "¿Tiene adeudos en pagos/biblioteca? (si/no): "
).lower()


j = asistencia >= 80

a = promedio >= 7 

q = proyecto == "si"

u = autorizacion == "si"

e = lista_oficial == "si"

l =  adeudo == "si" 



print("j- asistencias", j)
print("a- promedio",a)
print("q- proyecto", q)
print("u- autorizacion",u)
print("e- lista", e)
print("l - Tiene adeudos:", l)

print("uwu")

negacion_J = not j

print("\n negacion")
print("J=", negacion_J)

conjuncion = j and a

print("\n conjuncion")
print("j  ∧ a ", conjuncion)

disyuncion = q or u

print("\nDISYUNCIÓN")
print("Q ∨ U =", disyuncion)


condicinal = (not j) or a

print("\nCONDICIONAL")
print("J → A=", condicinal)


bicondicional = j == a

print("\nBICONDICIONAL")
print("J ↔ A =", bicondicional)


expre = (j and a) or u and e
expre = ((j and a) or (u and e)) and (not l)
print("\nEXPRESIÓN CON PARÉNTESIS")
print("(j ∧ a) ∨ u =", expre)



if expre:
    print("\nRESULTADO:")
    print("El alumno PUEDE presentar el examen.")
else:
    print("\nRESULTADO:")
    print("El alumno NO puede presentar el examen.")
