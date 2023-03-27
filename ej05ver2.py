""" Ejercicio 5: Calculadora de fracciones
El jefe del departamento de matemática de una escuela nos pide que diseñemos una calculadora de fracciones.
Debemos representar una fracción con numerador y denominador enteros.
El usuario podrá realizar todos los cálculos que quiera.
Ofrecer un menú.

Mostrar el resultado de manera elegante  (como una fracción).

Utilizar método constructor."""

import math

class Calculadora:
    def __init__(self):
        self.num1= 0
        self.den1= 0
        self.num2= 0
        self.den2= 0
        self.potenciar= 0       #numero al que la funcion potencia va a potenciar la fraccion ingresada.
        self.operacion= 0       #resultados de suma, resta, producto, etc
        self.resultado= 0       #resultado de la operacion de operacion
        self.unidadDecimal= 0   #por la que voy a multiplicar el resultado de las operaciones para obtener los resultados en forma de fraccion de la siguiente manera::
        self.cantDecimales= 0   #la cantidad de 0 que le voy a tener que agregar a el atributo de arriba
        self.resultadoNum= 0    #numerador que queda como resultado de la conversion a fraccion de resultado
        self.resultadoDen= 0    #denominador que queda como resultado de la conversion a fraccion de resultado
        self.divisor= 0         #todos los numeros que haya en el rango del for i in range. Sirve para iterar no mas.
        self.posibleMCD= []     #posibles maximo comun divisores del numerador
        self.maximoDivisorComun= 0

    def setNumerador1(self):
        self.num1= int(input("Ingrese el numerador de la primer fracción: "))

    def setDenominador1(self):
        self.den1= int(input("Ingrese el denominador de la primer fracción: "))

    def setNumerador2(self):
        self.num2= int(input("Ingrese el numerador de la segunda fracción: "))

    def setDenominador2(self):
        self.den2= int(input("Ingrese el denominador de la segunda fracción: "))

    def setFraccion(self):
        self.setNumerador1()
        self.setDenominador1()

    def setFracciones(self):
        self.setNumerador1()
        self.setDenominador1()
        self.setNumerador2()
        self.setDenominador2()

    def getOperacion(self):
        return self.operacion
    

    def menu(self):
        menu= "Operaciones disponibles:\n1. Suma\n2. Resta\n3. Producto\n4. Division\n5. Potencia\n6. Raiz cuadrada"
        print(menu)

    def ingresarOpcion(self):
        opc= int(input("Ingrese el número de operación elegida: "))
        if opc >0 and opc <7:
            self.operacion= opc
        else:
            print("Operación inválida. Intente nuevamente.")
            return self.ingresarOpcion()

    def suma(self):
        operacion= ((self.num1*self.den2) + (self.den1*self.num2)) / (self.den1*self.den2)
        self.resultado= operacion
    
    def resta(self):
        operacion= ((self.num1*self.den2) - (self.den1*self.num2)) / (self.den1*self.den2)
        self.resultado= operacion

    def producto(self):
        operacion= (self.num1*self.num2) / (self.den1*self.den2)
        self.resultado= operacion
    
    def division(self):
        operacion= (self.num1*self.den2) / (self.den2*self.num1)
        self.resultado= operacion
    
    def raizCuadrada(self):
        operacion= math.sqrt(self.num1) / math.sqrt(self.den1)
        self.resultado= operacion
        self.resultadoNum= math.sqrt(self.num1)
        self.resultadoDeb= math.sqrt(self.den1)

    def potencia(self):
        self.ingresarPotencia()
        operacion= math.pow(self.num1, self.potenciar) / math.pow(self.den1, self.potenciar)
        self.resultado= operacion
        self.resultadoNum= math.pow(self.num1, self.potenciar)
        self.resultadoDeb= math.pow(self.den1, self.potenciar)

    def ingresarPotencia(self):
        self.potenciar= int(input("Ingrese la potencia a la que quiere elevar la fracción: "))

    def redondearResultado(self):
        self.resultado= round(self.resultado,2)

    def procesarOperaciones(self):
        if self.operacion == 1:
            self.suma()
        if self.operacion == 2:
            self.resta()
        if self.operacion == 3:
            self.producto()
        if self.operacion == 4:
            self.division()
        if self.operacion == 5:
            self.ingresarPotencia()
        if self.operacion == 6:
            self.raizCuadrada()
        self.redondearResultado()


    def obtenerCantidadDeDecimales(self):
        self.cantDecimales= len(str(self.resultado).split(".")[1])
        self.unidadDecimal= "1"

    def agregar0aUnidadDecimal(self):
        for i in range(self.cantDecimales):
            self.unidadDecimal= self.unidadDecimal + "0"
        self.unidadDecimal= int(self.unidadDecimal)

    def obtenerUnidadDecimal(self):
        """obtengo n (n= cantidad de n° que hay despues de la coma en el resultado), inicializo cantDecimales en "1",
        y con un ciclo for en un rango de n voy agregando "0" a la string, para terminar pasandola a int."""
        self.obtenerCantidadDeDecimales()
        self.agregar0aUnidadDecimal()

    #pasar de decimal a fraccion:
    def obtenerNumYDenEnteros(self):
        self.resultadoNum= int(self.resultado * self.unidadDecimal)
        self.resultadoDen= int(1 * self.unidadDecimal)

    def calcularPosiblesMCD(self):
        self.divisor= 0
        for i in range(self.resultadoNum):
            self.divisor= self.divisor +1
            if self.resultadoNum % self.divisor == 0:
                self.posibleMCD.append(i+1)
        print(self.posibleMCD) #prueba

    def obtenerMCD(self):
        self.divisor= 0
        print(self.divisor) #prueba
        for i in range(self.resultadoDen):
            self.divisor= self.divisor +1
            if self.resultadoDen % self.divisor == 0 and i+1 in self.posibleMCD:
                self.maximoDivisorComun= i+1
        print(self.maximoDivisorComun)

    def simplificarFracciones(self):
        self.resultadoNum= self.resultadoNum/self.maximoDivisorComun
        self.resultadoDen= self.resultadoDen/self.maximoDivisorComun

    def pasarDecimalAFraccion(self):
        self.obtenerNumYDenEnteros()
        self.calcularPosiblesMCD()
        self.obtenerMCD()
        self.simplificarFracciones()

    def mostrarResultado(self):
        if self.operacion == 1:
            print("La suma entre "+ str(self.num1) +"/"+str(self.den1)+" y "+str(self.num2)+"/"+str(self.den2)+" da como resultado:\nEntero:", str(self.resultado), "\nFraccion: "+str(self.resultadoNum) + "/" + str(self.resultadoDen))
        if self.operacion == 2:
            print("La resta entre "+ str(self.num1) +"/"+str(self.den1)+" y "+str(self.num2)+"/"+str(self.den2)+" da como resultado:\nEntero:", str(self.resultado), "\nFraccion: "+str(self.resultadoNum) + "/" + str(self.resultadoDen))
        if self.operacion == 3:
            print("El producto entre "+ str(self.num1) +"/"+str(self.den1)+" y "+str(self.num2)+"/"+str(self.den2)+" da como resultado: "+ str(self.resultado), "o bien "+str(self.resultadoNum) + "/" + str(self.resultadoDen))
        if self.operacion == 4:
            print("La division de "+ str(self.num1) +"/"+str(self.den1)+" por "+str(self.num2)+"/"+str(self.den2)+" da como resultado: "+ str(self.resultado), "o bien "+str(self.resultadoNum) + "/" + str(self.resultadoDen))
        if self.operacion == 5:
            print("La potencia de "+ str(self.num1) +"/"+str(self.den1)+" da como resultado: ",self.resultado, "o bien "+str(self.resultadoNum) + "/" + str(self.resultadoDen))
        if self.operacion == 6:
            print("La raiz cuadrada de "+ str(self.num1) +"/"+str(self.den1)+" da como resultado: ",self.resultado, "o bien "+str(self.resultadoNum) + "/" + str(self.resultadoDen))


#funciones-------------------------------------------------------------------------------------
def Q_realizarOperaciones():
    q= input("¿Desea realizar operaciones? s/n: ").lower()
    if q == "s":
        return True
    else:
        return False

def off():
    print("Gracias por utilizar el software <3")

#main------------------------------------------------------------------------------------------
calc0000= Calculadora()
on= Q_realizarOperaciones()
while on == True:
    calc0000.menu()
    calc0000.ingresarOpcion()
    if calc0000.getOperacion() >0 and calc0000.getOperacion() <5:
        calc0000.setFracciones()
    if calc0000.getOperacion() >=5:
        calc0000.setFraccion()
    calc0000.procesarOperaciones()
    calc0000.obtenerUnidadDecimal()
    calc0000.pasarDecimalAFraccion()
    calc0000.mostrarResultado()
    on= Q_realizarOperaciones()
off()
