valores = [True, False]

print("P \t Q \t P AND Q")
print("- "* 25)

for P in valores:
    
    for Q in valores:
        
        resulltado = P and Q
        print(P, "\t" , Q, "\t", resulltado)