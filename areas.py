#encoding:UTF-8
#Autor: Lenin Silva Gutirrez, A01373214 
#Calcula áreas y perímetros de rectángulos

from Graphics import *

def calcularArea(b,h): #Calcula el área
    area=b*h
    return area

def calcularPerimetro(b,h): #Calcula el perímetro
    perimetro=(2*b)+(2*h)
    return perimetro
    
def compararAreas(area1,area2): #Define qué área es mayor 
  
    if area1>area2:
        return area1, area2
    elif area1<area2:
        return area2,area1
    return 0,0

def dibujarMitad(b,h,t,color): #dibuja la mitad de un rectángulo
    t.penDown()
    t.pen.color=Color(color)
    t.forward(b)
    t.rotate(90)
    t.forward(h)
    t.rotate(90)
            
def dibujarRectangulo(b,h,t,color): #Dibuja un rectángulo completo
    for i in range(2): #Ejecuta dos veces la función dibujarMitad() para completar el rectángulo
        dibujarMitad(b,h,t,color)
     
    
def dibujarDosRectangulos(b,h,b2,h2,color1,color2):
    v=Window("Rectángulos",b+b2+300,h+h2+300)#Hace que el tamaño de la ventana dependa de las dimensiones de los rectángulos
    t=Arrow((100,h+h2+200),0)#La posición de la flecha depende de la altura de los rectángulos
    t.draw(v)
    dibujarRectangulo(b,h,t,color1)#Dibuja el primer rectángulo con el color especificado por el usuario
    t.penUp()
    t.forward(b+100)
    dibujarRectangulo(b2,h2,t,color2)#Dibuja el segundo rectángulo con el color especificado por el usuario 
    
def main():
    #El programa lee la base y altura de ambos rectángulos. El usuario elige el color de cada rectángulo
    #con minúsculas y en inglés
    b=float(input("Base 1"))
    h=float(input("Altura 1"))
    color1=str(input("Color rectángulo 1"))
    b2=float(input("Base 2"))
    h2=float(input("Altura 2"))
    color2=str(input("Color rectángulo 2"))
    
    #Calcular perímetros
    perimetro1=calcularPerimetro(b,h)
    perimetro2=calcularPerimetro(b2,h2)
    print ("El perímetro del rectángulo 1 es: %.2f"%(perimetro1))
    print ("El perímetro del rectángulo 2 es: %.2f"%(perimetro2))
    
    #Calcular áreas
    area1=calcularArea(b,h)
    area2=calcularArea(b2,h2)
    mayor,menor=compararAreas(area1,area2)
    if mayor==0 and menor==0:
        print ("El área 1 es %.2f y el área 2 es %.2f, por lo que son iguales"%(area1, area2))
    else:
        print ("El área 1 es: %.2f"%(area1))
        print ("El área 2 es: %.2f"%(area2))
        print ("El área mayor es %.2f y la menor es %.2f"%(mayor,menor))
        
    #Dibujar Rectángulos
    dibujarDosRectangulos(b,h,b2,h2,color1,color2)
    
main()
    