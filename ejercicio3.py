notas = []


for i in range(5):
    nota = float(input("INGRESE UNA NOTA: "))
    i = i+1
    while nota < 0 or nota >10:
        nota = float(input("Ingrese una nota valida  (entre 0 y 10: )"))
    notas.append(nota)
    
    
print("Todas las notas: ", notas)
print("Nota media: ", {sum(notas)/len(notas)})
print("Nota mas Alta: ", {max(notas)})
print("Nota mas baja: ", {min(notas)})