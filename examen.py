# ==========================================================
# CASO DE ESTUDIO:
# Sistema de autorización para examen
# ==========================================================

print("==============================================")
print(" SISTEMA DE AUTORIZACIÓN PARA EXAMEN FINAL")
print("==============================================")

# ----------------------------------------------------------
# 1. ENTRADA DE DATOS
# ----------------------------------------------------------

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

lista_oficial = input(
    "¿Está en la lista oficial? (si/no): "
).lower()

adeudo = input(
    "¿Tiene adeudos en pagos/biblioteca? (si/no): "
).lower()


# ----------------------------------------------------------
# 2. CONVERTIMOS LOS DATOS EN PROPOSICIONES
# ----------------------------------------------------------

P = asistencia >= 80              # Verdadera si asistencia es >= 80
Q = promedio >= 7                 # Verdadera si promedio es >= 7
R = proyecto == "si"              # Verdadera si entregó proyecto
S = autorizacion == "si"          # Verdadera si tiene autorización
h = lista_oficial == "si"         # Falsa si está en la lista oficial (por la regla anterior)


T = adeudo == "si"                


# ----------------------------------------------------------
# 3. MOSTRAMOS LAS PROPOSICIONES
# ----------------------------------------------------------

print("\n==============================================")
print(" VALORES DE LAS PROPOSICIONES")
print("==============================================")

print("P - Asistencia suficiente:", P)
print("Q - Promedio aprobatorio:", Q)
print("R - Proyecto entregado:", R)
print("S - Autorización especial:", S)
print("h - lista oficial:", h)
print("T - Tiene adeudos:", T)


# ----------------------------------------------------------
# 4. DECISIÓN FINAL CON LA NUEVA LÓGICA
# ----------------------------------------------------------


expresion_final = ((P and Q) or (S and h)) and (not T)

print("\nEXPRESIÓN FINAL EVALUADA")
print("((P ∧ Q) ∨ (S ∧ h)) ∧ ¬T =", expresion_final)

if expresion_final:
    print("\nRESULTADO:")
    print("El alumno PUEDE presentar el examen.")
else:
    print("\nRESULTADO:")
    print("El alumno NO puede presentar el examen.")