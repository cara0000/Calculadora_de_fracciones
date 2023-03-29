import math

class Calculadora:
    def __init__(self):
        self.num1= 0
        self.den1= 0
        self.num2= 0
        self.den2= 0
        self.potenciar= 0
        self.operacion= 0
        self.resultadoNum= 0
        self.resultadoDen= 0
        self.divisor= 0
        self.posibleMCD= []
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
        self.resultadoNum= ((self.num1*self.den2) + (self.den1*self.num2))
        self.resultadoDen= (self.den1*self.den2)
    
    def resta(self):
        self.resultadoNum= ((self.num1*self.den2) - (self.den1*self.num2))
        self.resultadoDen= (self.den1*self.den2)

    def producto(self):
        self.resultadoNum= (self.num1*self.num2)
        self.resultadoDen= (self.den1*self.den2)
    
    def division(self):
        self.resultadoNum= (self.num1*self.den2)
        self.resultadoDen= (self.den1*self.num2)
    
    def raizCuadrada(self):
        self.resultadoNum= math.sqrt(self.num1)
        self.resultadoDen= math.sqrt(self.den1)

    def potencia(self):
        self.setPotencia()
        self.resultadoNum= math.pow(self.num1, self.potenciar)
        self.resultadoDen= math.pow(self.den1, self.potenciar)

    def setPotencia(self):
        self.potenciar= int(input("Ingrese la potencia a la que quiere elevar la fracción: "))

    def redondearResultado(self):
        self.resultadoNum= round(self.resultadoNum,2)
        self.resultadoDen= round(self.resultadoDen,2)

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
            self.potencia()
        if self.operacion == 6:
            self.raizCuadrada()
        self.redondearResultado()

    def rangoLoopForPosiblesMCD(self):
        if self.resultadoNum < self.resultadoDen and self.resultadoNum > 0:
            return self.resultadoNum
        if self.resultadoNum < self.resultadoDen and self.resultadoNum < 0:
            return self.resultadoNum * (-1)
        if self.resultadoNum > self.resultadoDen and self.resultadoDen > 0:
            return self.resultadoDen
        if self.resultadoNum > self.resultadoDen and self.resultadoDen < 0:
            return self.resultadoDen * (-1)

    def calcularPosiblesMCD(self):
        self.divisor= 0
        if self.resultadoNum < self.resultadoDen:
            for i in range(self.rangoLoopForPosiblesMCD()):
                self.divisor= self.divisor +1
                if self.resultadoNum % self.divisor == 0:
                    self.posibleMCD.append(i+1)
            print(self.posibleMCD) #prueba
        else:
            for i in range(self.rangoLoopForPosiblesMCD()):
                self.divisor= self.divisor +1
                if self.resultadoDen % self.divisor == 0:
                    self.posibleMCD.append(i+1)

    def rangoLoopForMCD(self):
        if self.resultadoNum < self.resultadoDen and self.resultadoNum > 0:
            return self.resultadoDen
        if self.resultadoNum < self.resultadoDen and self.resultadoNum < 0:
            return self.resultadoDen * (-1)
        if self.resultadoNum > self.resultadoDen and self.resultadoDen > 0:
            return self.resultadoNum
        if self.resultadoNum > self.resultadoDen and self.resultadoDen < 0:
            return self.resultadoNum * (-1)
        
    def obtenerMCD(self):
        num= self.resultadoNum
        den= self.resultadoDen
        if num > den:
            for i in range(len(self.posibleMCD)):
                if num % self.posibleMCD[i] == 0:
                    self.maximoDivisorComun= self.posibleMCD[i]
        if num < den:
            for i in range(len(self.posibleMCD)):
                if den % self.posibleMCD[i] == 0:
                    self.maximoDivisorComun= self.posibleMCD[i]

    def simplificarFracciones(self):
        self.resultadoNum= int(self.resultadoNum/self.maximoDivisorComun)
        self.resultadoDen= int(self.resultadoDen/self.maximoDivisorComun)

    def mostrarResultado(self):
        if self.operacion == 1:
            print("La suma entre "+ str(self.num1) +"/"+ str(self.den1)+" y "+str(self.num2)+"/"+str(self.den2)+" da como resultado",str(self.resultadoNum) + "/" + str(self.resultadoDen))
        if self.operacion == 2:
            print("La resta entre "+ str(self.num1) +"/"+ str(self.den1)+" y "+str(self.num2)+"/"+str(self.den2)+" da como resultado",str(self.resultadoNum) + "/" + str(self.resultadoDen))
        if self.operacion == 3:
            print("El producto entre "+ str(self.num1) +"/"+ str(self.den1)+" y "+str(self.num2)+"/"+str(self.den2)+" da como resultado",str(self.resultadoNum) + "/" + str(self.resultadoDen))
        if self.operacion == 4:
            print("La division de "+ str(self.num1) +"/"+ str(self.den1)+" por "+str(self.num2)+"/"+str(self.den2)+" da como resultado",str(self.resultadoNum) + "/" + str(self.resultadoDen))
        if self.operacion == 5:
            print("La potencia de "+ str(self.num1) +"/"+ str(self.den1)+" da como resultado",str(self.resultadoNum) + "/" + str(self.resultadoDen))
        if self.operacion == 6:
            print("La raiz cuadrada de "+ str(self.num1) +"/"+str(self.den1)+" da como resultado",str(self.resultadoNum) + "/" + str(self.resultadoDen))


#funciones----------------------------------------------------------------------------------------------------------------------------------
def Q_realizarOperaciones():
    q= input("¿Desea realizar operaciones? s/n: ").lower()
    if q == "s":
        return True
    else:
        return False

def off():
    print("Gracias por utilizar el software <3")

#main---------------------------------------------------------------------------------------------------------------------------------------
calc0000= Calculadora()
on= Q_realizarOperaciones()
while on == True:
    calc0000.menu()
    calc0000.ingresarOpcion()
    if calc0000.getOperacion() >0 and calc0000.getOperacion() <5:
        calc0000.setFracciones()
        calc0000.procesarOperaciones()
        calc0000.calcularPosiblesMCD()
        calc0000.obtenerMCD()
        calc0000.simplificarFracciones()
    if calc0000.getOperacion() >=5:
        calc0000.setFraccion()
        calc0000.procesarOperaciones()
    calc0000.mostrarResultado()
    on= Q_realizarOperaciones()
off()