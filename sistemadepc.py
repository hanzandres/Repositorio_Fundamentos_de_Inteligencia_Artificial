print("==================================================")
print("     ¡BIENVENIDO AL ASISTENTE DE DIAGNÓSTICO!")
print("==================================================")

print("¿Qué tipo de equipo vamos a arreglar hoy?")
print("1. PC de Escritorio (Normal)")
print("2. PC Gamer (Con tarjeta gráfica dedicada)")
print("3. Laptop")
tipo_equipo = input("Ingresa el número de tu opción (1/2/3): ")

continuar = True

if continuar:
    resp = input("1. ¿El equipo tiene electricidad o batería con carga? (s/n): ").lower()
    if resp != "s":
        continuar = False
        print("\nFalla encontrada: Problema de energía.")
        if tipo_equipo == "1":
            print("Solución: Revisa que el enchufe de la pared funcione y el cable esté bien conectado.")
        elif tipo_equipo == "2":
            print("Solución: Revisa el interruptor trasero de la fuente de poder (PSU) y tu supresor de picos.")
        else:
            print("Solución: Conecta el cargador. Si no enciende el LED de carga, tu cargador o batería murieron.")

if continuar:
    resp = input("2. ¿El equipo enciende (giran ventiladores, encienden LEDs)? (s/n): ").lower()
    if resp != "s":
        continuar = False
        print("\nFalla encontrada: Sistema de arranque muerto.")
        if tipo_equipo == "1":
            print("Solución: Falla en el botón del gabinete o fuente de poder quemada. Revisa los cables frontales.")
        elif tipo_equipo == "2":
            print("Solución: Corto en la placa base o la fuente no tiene Watts suficientes. Desconecta componentes para probar.")
        else:
            print("Solución: Botón de encendido dañado. Quita la batería y presiona el botón por 30 segundos.")

if continuar:
    resp = input("3. ¿La placa base arranca SIN emitir pitidos de error o luces rojas? (s/n): ").lower()
    if resp != "s":
        continuar = False
        print("\nFalla encontrada: Error de POST en placa base.")
        if tipo_equipo == "1":
            print("Solución: La placa base detecta un hardware suelto. Saca la memoria RAM y vuélvela a poner.")
        elif tipo_equipo == "2":
            print("Solución: Revisa los LEDs 'EZ Debug' (CPU/DRAM/VGA/BOOT) de tu placa para ubicar exactamente qué componente falla.")
        else:
            print("Solución: Memoria RAM desoldada o floja por algún golpe. Requiere desarmar el equipo.")


if continuar:
    resp = input("4. ¿Muestra imagen o el logotipo de la marca en la pantalla? (s/n): ").lower()
    if resp != "s":
        continuar = False
        print("\nFalla encontrada: Ausencia de video.")
        if tipo_equipo == "1":
            print("Solución: Revisa el cable VGA/HDMI y asegúrate de que el monitor esté encendido.")
        elif tipo_equipo == "2":
            print("Solución: ¡Conectaste el monitor a la placa base! Conéctalo directo a los puertos de la Tarjeta Gráfica.")
        else:
            print("Solución: Pantalla rota o flex dañado. Conecta la laptop a un monitor externo con HDMI para comprobar.")

if continuar:
    resp = input("5. ¿Pasa del logotipo de la marca sin quedarse congelado? (s/n): ").lower()
    if resp != "s":
        continuar = False
        print("\nFalla encontrada: Congelamiento en el POST/BIOS.")
        if tipo_equipo == "1":
            print("Solución: Pila CMOS agotada. Cambia la pila de botón CR2032 de la tarjeta madre.")
        elif tipo_equipo == "2":
            print("Solución: Configuración de Overclock o XMP inestable. Haz un 'Clear CMOS' puenteando los pines de la placa.")
        else:
            print("Solución: BIOS corrupta o disco duro dañado frenando el arranque. Entra a la BIOS y revisa si detecta el disco.")

if continuar:
    resp = input("6. ¿Carga el sistema operativo y llega al escritorio? (s/n): ").lower()
    if resp != "s":
        continuar = False
        print("\nFalla encontrada: Problema de Software o Almacenamiento.")
        if tipo_equipo == "1":
            print("Solución: Windows corrupto. Repáralo usando una memoria USB booteable.")
        elif tipo_equipo == "2":
            print("Solución: Disco SSD NVMe fallando o conflicto de drivers de video. Entra en 'Modo Seguro'.")
        else:
            print("Solución: Disco duro (HDD) dañado por movimiento. Reemplázalo por un SSD nuevo.")


if continuar:
    resp = input("7. ¿El equipo se mantiene encendido SIN apagarse de repente? (s/n): ").lower()
    if resp != "s":
        continuar = False
        print("\nFalla encontrada: Apagones repentinos.")
        if tipo_equipo == "1":
            print("Solución: El procesador se está sobrecalentando o la fuente genérica no aguanta.")
        elif tipo_equipo == "2":
            print("Solución: Falla en la refrigeración líquida o pasta térmica seca. Monitorea las temperaturas.")
        else:
            print("Solución: Rejillas de ventilación obstruidas. Destapa la laptop, limpia el ventilador y cambia la pasta térmica.")


# --- PREGUNTA 8: PANTALLAS AZULES ---
if continuar:
    resp = input("8. ¿El sistema funciona SIN lanzar Pantallazos Azules (BSOD)? (s/n): ").lower()
    if resp != "s":
        continuar = False
        print("\nFalla encontrada: Inestabilidad del sistema (BSOD).")
        if tipo_equipo == "1":
            print("Solución: Driver genérico fallando o Windows sin actualizar.")
        elif tipo_equipo == "2":
            print("Solución: Memoria RAM inestable. Baja los MHz en la BIOS o revisa el voltaje del procesador.")
        else:
            print("Solución: Conflicto entre las dos tarjetas de video (Intel/AMD). Reinstala los drivers de fábrica.")


# --- PREGUNTA 9: RUIDOS FÍSICOS ---
if continuar:
    resp = input("9. ¿El equipo funciona de forma silenciosa, SIN ruidos mecánicos fuertes? (s/n): ").lower()
    if resp != "s":
        continuar = False
        print("\nFalla encontrada: Ruido físico anormal.")
        if tipo_equipo == "1":
            print("Solución: Un cable está chocando con un ventilador o tu disco mecánico hace 'clic' (está a punto de morir).")
        elif tipo_equipo == "2":
            print("Solución: 'Coil Whine' (zumbido eléctrico) en la tarjeta de video por alto consumo. Es normal, pero molesto.")
        else:
            print("Solución: El ventilador está rozando por exceso de polvo o la bisagra rota está presionando el chasis.")


# --- PREGUNTA 10: RED Y PERIFÉRICOS ---
if continuar:
    resp = input("10. ¿Reconoce correctamente el internet (Wi-Fi/Ethernet) y los puertos USB? (s/n): ").lower()
    if resp != "s":
        continuar = False
        print("\nFalla encontrada: Problemas de conectividad.")
        if tipo_equipo == "1":
            print("Solución: El chip de red de la placa base se quemó. Instala una tarjeta de red por PCIe o USB.")
        elif tipo_equipo == "2":
            print("Solución: Antena Wi-Fi de la placa base floja o saturación de ancho de banda. Actualiza los drivers LAN.")
        else:
            print("Solución: Tarjeta de red M.2 Wi-Fi suelta internamente o tienes el Modo Avión activado por error.")


# --- RESULTADO PERFECTO ---
if continuar:
    print("\n==================================================")
    print(" ¡FELICIDADES! TU EQUIPO PASÓ TODAS LAS PRUEBAS.")
    print("El hardware, software y temperaturas están en perfecto estado.")
    print("==================================================")