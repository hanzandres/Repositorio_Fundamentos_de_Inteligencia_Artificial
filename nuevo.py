# ==========================================================
# CASO DE ESTUDIO
# Sistema de autorización para examen -
# ==========================================================

print("=" * 55)
print("       SISTEMA DE AUTORIZACIÓN PARA EXAMEN")
print("=" * 55)

# ----------------------------------------------------------
# 1. ENTRADA DE DATOS
# ----------------------------------------------------------
asistencia = float(input("Ingresa el porcentaje de asistencia: "))
promedio = float(input("Ingresa el promedio: "))
proyecto = input("¿Entregó el proyecto? (si/no): ").lower()
adeudos = input("¿Tiene adeudos? (si/no): ").lower()
autorizacion = input("¿Tiene autorización especial? (si/no): ").lower()
lista_oficial = input("¿Aparece en la lista oficial? (si/no): ").lower()

# ----------------------------------------------------------
# 2. CREACIÓN DE LAS PROPOSICIONES
# ----------------------------------------------------------
P = asistencia >= 80  # Asistencia suficiente
Q = promedio >= 8     # Promedio aprobatorio
R = proyecto == "si"  # Proyecto entregado
S = adeudos == "no"   # Sin adeudos
T = autorizacion == "si" # Autorización especial
U = lista_oficial == "si" # Aparece en lista

# ----------------------------------------------------------
# 3. MOSTRAR LAS PROPOSICIONES
# ----------------------------------------------------------
print("\n" + "=" * 55)
print("             VALORES DE LAS PROPOSICIONES")
print("=" * 55)
print(f"P - Asistencia suficiente : {P} ({asistencia}%)")
print(f"Q - Promedio aprobatorio  : {Q} ({promedio})")
print(f"R - Proyecto entregado    : {R}")
print(f"S - Sin adeudos           : {S}")
print(f"T - Autorización especial : {T}")
print(f"U - Aparece en lista      : {U}")

# ==========================================================
# 4. NEGACIÓN
# ==========================================================
no_P = not P
print("\nNEGACIÓN")
print(f"¬P = {no_P} (No tiene asistencia suficiente)")

# ==========================================================
# 5. CONJUNCIÓN
# ==========================================================
conjuncion = P and Q
print("\nCONJUNCIÓN")
print(f"P ∧ Q = {conjuncion}")

# ==========================================================
# 6. DISYUNCIÓN
# ==========================================================
disyuncion = Q or T
print("\nDISYUNCIÓN")
print(f"Q ∨ T = {disyuncion}")

# ==========================================================
# 7. CONDICIONAL
# ==========================================================
condicional = (not P) or Q
print("\nCONDICIONAL")
print(f"P → Q = {condicional}")

# ==========================================================
# 8. BICONDICIONAL
# ==========================================================
bicondicional = P == Q
print("\nBICONDICIONAL")
print(f"P ↔ Q = {bicondicional}")

# ==========================================================
# 9. EXPRESIÓN CON PARÉNTESIS
# ==========================================================
resultado_parcial = (P and Q and R and S) or T
print("\nEXPRESIÓN CON PARÉNTESIS")
print(f"(P ∧ Q ∧ R ∧ S) ∨ T = {resultado_parcial}")

# ==========================================================
# 10. VALIDACIÓN DE AUTORIZACIÓN - CORRECCIÓN CLAVE
# ==========================================================
# Esto es: T → U  que es igual a (not T) or U

autorizacion_valida = (not T) or U

print("\nVALIDACIÓN DE AUTORIZACIÓN")
print(f"T → U = {autorizacion_valida}")
print("Se lee: Si tiene autorización especial, entonces debe aparecer en lista oficial")

# ==========================================================
# 11. RESULTADO FINAL - LÓGICA FINAL REAL
# ==========================================================
print("\n" + "=" * 55)
print("                  RESULTADO FINAL")
print("=" * 55)

# Regla final: Puede presentar por cumplir todo O por tener autorización,
# PERO si usa autorización, esa autorización debe ser válida (estar en lista)
resultado_final = resultado_parcial and autorizacion_valida

if resultado_final:
    print(" El alumno PUEDE presentar el examen.")
else:
    print(" El alumno NO puede presentar el examen.")

if not autorizacion_valida:
    print("  ADVERTENCIA: Tiene autorización especial pero NO aparece en la lista oficial. Autorización inválida.")
elif T and U:
    print(" La autorización especial es válida y coincide con la lista oficial.")