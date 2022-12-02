#Herencia y Polimorfismo
class padre:
    def __init__(self, numero):
        self.numero = numero

    def mensaje1(self):
        print("hola buenos dias")
        print("-")

    def mensaje2(self):
        print("hola buenas tardes")
        print("--")

    def mensaje3(self):
        print("hola buenas noche")
        print("---")

class hijo(padre):
    def __init__(self, numero):
        super().__init__(numero)

    def mensaje4(self):
        print("como has estado")
        print(self.numero + 10)
        print("-")

    def mensaje5(self):
        print("como va la vida")
        print("--")

    def mensaje6(self):
        print("hasta otra oportunidad")
        print("---")

ejemplo = hijo(10)
ejemplo.mensaje1()
ejemplo.mensaje5()
ejemplo.mensaje2()
ejemplo.mensaje6()
ejemplo.mensaje4()