##Ejercicio 1 
nombres = ['Bryan', 'Juan', 'Maria']
notas = [95, 88, 92]
for nombre, nota in zip(nombres, notas):
    print(f"Estudiante: {nombre} | Nota: {nota}")


##Ejercicio 2 
edades = [15, 20, 12, 18, 30, 17]
# Solo dejamos pasar a los mayores de edad (18+)
mayores = list(filter(lambda x: x >= 18, edades))
print(mayores)

def saludar(nombre, mensaje="Bienvenido al curso"):
    print(f"Hola {nombre}, {mensaje}")

saludar("bryan")  # usar el mensaje por defecto
saludar("jack", "hoy toca aprender a codificar")  # mensaje personalizado

#Ejercicio 3

def tabla_de_multiplicar(n):
    for i in range(1, 11):
        print(n, "*", i, "=", i * n)

tabla_de_multiplicar(5)
