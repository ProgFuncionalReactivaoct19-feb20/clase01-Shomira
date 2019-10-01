#Importacion las funciones en los metodos
from practica import*

print(metodoUno(3))

print(metodoDos(metodoUno(4)))

print(metodoTres(metodoDos(metodoTres(5))))

print(metodoCuatro(metodoTres(metodoDos(metodoUno(2)))))

