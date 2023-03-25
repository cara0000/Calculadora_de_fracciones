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
        self.resultadoNum= 0
        self.resultadoDen= 0
        self.resultado= 0
        self.operacion= 0
        self.potenciar= 2
        self.divisor= 0
        self.cantDecimales= 0
        self.unidadDecimal= 0
        self.resultadoNum= 0
        self.resultadoDen= 0
        self.posiblesMaxDivCom= []
        self.maxDivisorComun= 0

    def setNumerador1(self):
        self.num1= int(input("Ingrese el numerador de la primer fraccion: "))

    def setDenominador1(self):
        self.den1= int(input("Ingrese el denominador de la primer fraccion: "))

    def setNumerador2(self):
        self.num2= int(input("Ingrese el numerador de la segunda fraccion: "))

    def setDenominador2(self):
        self.den2= int(input("Ingrese el denominador de la segunda fraccion: "))

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
    
    def ingresarOpcion(self):
        opc= int(input("Ingresar: "))
        if opc >0 and opc <7:
            self.operacion= opc
        else:
            print("Operacion invalida. Intente nuevamente.")
            return self.ingresarOpcion()

    def menu(self):
        menu= "Operaciones disponibles:\n1. Suma\n2. Resta\n3. Producto\n4. Division\n5. Potencia\n6. Raiz cuadrada"
        print(menu)

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
    
    def potencia(self):
        operacion= math.pow(self.num1, self.potenciar) / math.pow(self.den1, self.potenciar)
        self.resultado= operacion
    
    def ingresarPotencia(self):
        self.potenciar= int(input("Ingrese la potencia a la que quiere elevar la fracción: "))

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
            self.potencia() #tengo que poner la potencia
        if self.operacion == 6:
            self.raizCuadrada()

    #pasar de decimal a fraccion:

    def calcularCantidadDecimales(self):
        self.cantDecimales= len(str(self.resultado).split(".")[1])
        self.unidadDecimal= "1"

    def generarNumeroDecimal(self):
            for i in range(self.cantDecimales):
                self.unidadDecimal= self.unidadDecimal + "0"

    def obtenerResultadoEnFraccion(self):
        self.resultadoNum= self.resultado * int(self.unidadDecimal)
        self.resultadoDen= 1 * int(self.unidadDecimal)

    def obtenerPosiblesMaximoDivisorComun(self):#error
        for i in range(self.resultadoDen):
            self.divisor= self.divisor + 1
            print(self.resultadoDen)
            print(self.divisor)
            if self.resultadoDen % self.divisor == 0:
                self.posiblesMaxDivCom.append(i)

    def obtenerMaximoDivCom(self):
        for i in range(self.resultadoNum):
            if self.resultadoNum %i == 0:
                if i in self.posiblesMaxDivCom:
                    self.maxDivisorComun == i
    
    def obtenerResultadoEnFraccionSimplificada(self):
        self.resultadoNum= round((self.resultadoNum / self.maxDivisorComun),2)
        self.resultadoDen= round((self.resultadoDen / self.maxDivisorComun),2)

    def pasarDecimalAFraccion(self):
        self.calcularCantidadDecimales()
        self.generarNumeroDecimal()
        self.obtenerResultadoEnFraccion()
        if self.resultadoDen > self.resultadoNum:
            self.obtenerPosiblesMaximoDivisorComun()
            self.obtenerMaximoDivCom()
            self.obtenerResultadoEnFraccionSimplificada
    #-----------------------------------------------------

    def mostrarResultado(self):
        if self.operacion == 1:
            print("La suma entre  ",self.num1,"/",self.den1,"  y  ",self.num2,"/",self.den2,"  da como resultado: ",self.resultado, "o bien",int(self.resultadoNum),"/",int(self.resultadoDen))
        if self.operacion == 2:
            print("La resta entre  ",self.num1,"/",self.den1,"  y  ",self.num2,"/",self.den2,"  da como resultado: ",self.resultado, "o bien",int(self.resultadoNum),"/",int(self.resultadoDen))
        if self.operacion == 3:
            print("El producto entre  ",self.num1,"/",self.den1,"  y  ",self.num2,"/",self.den2,"  da como resultado: ",self.resultado, "o bien",int(self.resultadoNum),"/",int(self.resultadoDen))
        if self.operacion == 4:
            print("La division de  ",self.num1,"/",self.den1,"  por  ",self.num2,"/",self.den2,"  da como resultado: ",self.resultado, "o bien",int(self.resultadoNum),"/",int(self.resultadoDen))
        if self.operacion == 5:
            print("La potencia de  ",self.num1,"/",self.den1,"  da como resultado: ",self.resultado, "o bien",int(self.resultadoNum),"/",int(self.resultadoDen))
        if self.operacion == 6:
            print("La raiz cuadrada de  ",self.num1,"/",self.den1,"  da como resultado: ",self.resultado, "o bien",int(self.resultadoNum),"/",int(self.resultadoDen))


#funciones-------------------------------------------------------------------------------------
def Q_realizarOperaciones():
    q= input("¿Desea realizar operaciones? s/n: ").lower()
    if q == "s":
        return True
    else:
        return False

def off():
    print("¡Gracias por utilizar el software!")

#main------------------------------------------------------------------------------------------
calc0000= Calculadora()
on= Q_realizarOperaciones()
while on == True:
    calc0000.menu()
    calc0000.ingresarOpcion()
    opc= calc0000.getOperacion()
    if opc >0 and opc <5:
        calc0000.setFracciones()
    if opc >=5:
        calc0000.setFraccion()
    calc0000.procesarOperaciones()
    #pasar decimal a fraccion
    calc0000.pasarDecimalAFraccion()
    calc0000.mostrarResultado()
    print(calc0000.resultadoNum)
    print(calc0000.resultadoDen)
    on= Q_realizarOperaciones()
off()