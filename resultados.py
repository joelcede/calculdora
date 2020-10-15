from funciones import Operaciones

class Calculadora(Operaciones):

    def __init__(self):
        self.valor1 = int(input("ingrese un valor: "))
        self.valor2 = int(input("ingrese un valor: "))

    def ver_suma(self):
        print("{} + {} = {}".format(self.valor1,self.valor2,
                                    self.sumar(self.valor1,self.valor2)))
    
    def ver_resta(self):
        print("{} - {} = {}".format(self.valor1,self.valor2,
                                    self.restar(self.valor1,self.valor2)))

    def ver_multiplicacion(self):
        print("{} * {} = {}".format(self.valor1,self.valor2,
                                    self.multiplicar(self.valor1,self.valor2)))
    def ver_division(self):
        print("{} % {} = {}".format(self.valor1,self.valor2,
                                    self.dividir(self.valor1,self.valor2)))                                                                      

calular = Calculadora()
calular.ver_suma()
