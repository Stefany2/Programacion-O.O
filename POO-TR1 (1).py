import os
class Trabajador:
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setCategoria(self, cat):
        self.cat = cat

    def getCategoria(self):
        return self.cat

    def setHorasExtras(self, HE):
        self.HE = HE

    def getHorasExtras(self):
        return self.HE

    def setTardanzas(self, tar):
        self.tar = tar

    def getTardanzas(self):
        return self.tar

class Boleta:

    def __init__(self, nombre, cat, HE, tar):
        self.nom = nombre
        self.categoria = cat
        self.HorasE = HE
        self.tardanza = tar
        self.SueldoB = 0
        self.PagoHora = 0
        self.PagoHoraExtra = 0
        self.HorasT = 0
        self.DescuentoT = 0
        self.SueldoN = 0

    def SueldoBasico(self):
        if self.categoria == "A":
            self.SueldoB = 3000
        elif self.categoria == "B":
            self.SueldoB = 2500
        else:
            self.SueldoB = 2000

        return self.SueldoB
            
        

    def PagoHoras(self):
        self.PagoHora = self.SueldoB/240
        
    def DescuentoTardanzas(self):
        self.HorasT = tar/60
        self.DescuentoT = self.HorasT *self.PagoHora

        return self.DescuentoT

    def PagoHorasExtras(self):
        self.PagoHoraExtra = self.PagoHora * self.HorasE
        return self.PagoHoraExtra

    def SueldoNeto(self):
        self.SueldoN = self.SueldoB + self.PagoHoraExtra - self.DescuentoT
        return self.SueldoN

print("*** DATOS DE ENTRADA ***")
nombre = input("TRABAJADOR: ")
a = True
while a:
    cat = input("CATEGORIA: ")
    if cat == "A" or cat == "B" or cat == "C":
        a = False
    else:
        print("Ingrese una categoria valida.")

a = True
while a:
    HE = int(input("HORAS EXTRAS: "))
    if HE >= 0:
        a = False
    else:
        print("Ingrese un numero entero positivo")
        
a = True
while a:
    tar = int(input("TARDANZAS: (minutos) "))
    if tar >= 0:
        a = False
    else:
        print("Ingrese un numero entero positivo")
        
obj1 = Trabajador()
obj1.setNombre(nombre)
obj1.setCategoria(cat)
obj1.setHorasExtras(HE)
obj1.setTardanzas(tar)

obj2 = Boleta(obj1.getNombre(),obj1.getCategoria(),obj1.getHorasExtras(),
              obj1.getTardanzas())
print("")
print("*** DATOS DE ENTRADA ***")
print("NOMBRE:",obj1.getNombre())
print("CATEGORIA:", obj1.getCategoria())
print("SUELDO BASICO:", obj2.SueldoBasico())
obj2.PagoHoras()
print("DESCUENTO TARDANZAS:", round(obj2.DescuentoTardanzas(), 2))
print("PAGO HORAS EXTRAS:",round(obj2.PagoHorasExtras(),2))
print("SUELDO NETO:", round(obj2.SueldoNeto(),2))
os.system("PAUSE")
