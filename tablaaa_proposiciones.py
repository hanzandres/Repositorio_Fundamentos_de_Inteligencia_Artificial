
cantidad = int(input("Cuantas proposiciones deseas evaluar: "))


valores = [True, False]

if cantidad == 1:
    print("\nP \t RESULTADO (P)")
    print("-" * 25)
    
    for P in valores:
        resultado = P
        print(f"{P} \t {resultado}")

elif cantidad == 2:
   
   
    print("\nP \t Q \t P AND Q")
    print("-" * 35)
    
    for P in valores:
        for Q in valores:
            resultado = P and Q
            print(f"{P} \t {Q} \t {resultado}")

elif cantidad == 3:
    
    print("\nP \t Q \t R \t P AND Q AND R")
    print("-" * 50)
    
    for P in valores:
        for Q in valores:
            for R in valores:
                resultado = P and Q and R
                print(f"{P} \t {Q} \t {R} \t {resultado}")
                
                
elif cantidad == 4:
    
    print("\nP \t Q \t R \t P AND Q AND R AND E")
    print("-" * 50)

    for P in valores:
            for Q in valores:
                for R in valores:
                    for E in valores:
                        resultado = P and Q and R and E
                        print(f"{P} \t {Q} \t {R} \t{E} \t {resultado}")
                    
                    
else:
    print("Número no soportado. Por favor ingresa 1, 2 o 3.")