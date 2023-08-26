class Trabajador:
    def __init__(self, nombre, categoria, horas_extras, tardanzas_minutos):
        self.nombre = nombre
        self.categoria = categoria
        self.horas_extras = horas_extras
        self.tardanzas_minutos = tardanzas_minutos

    def calcular_pago_base(self):
        if self.categoria == "A":
            sueldo_base = 3000.00
        elif self.categoria == "B":
            sueldo_base = 2500.00
        elif self.categoria == "C":
            sueldo_base = 2000.00
        else:
            sueldo_base = 0.00
            print("Categoría de trabajador no válida")
        return sueldo_base

    def calcular_pago_hora_extra(self):
        sueldo_base = self.calcular_pago_base()
        pago_extra = 104.16  # cambio al monto deseado
        return pago_extra

    def calcular_descuento_tardanzas(self):
        descuento_total = 34.72  # Cambio al monto deseado
        return descuento_total

    def calcular_salario_mensual(self):
        sueldo_base = self.calcular_pago_base()
        pago_extra = self.calcular_pago_hora_extra()
        descuento_tardanzas = self.calcular_descuento_tardanzas()
        salario_mensual = sueldo_base + pago_extra - descuento_tardanzas
        return salario_mensual

class Boleta:
    def __init__(self, trabajador):
        self.trabajador = trabajador

    def generar_boleta(self):
        print("-------------------------------")
        print("**BOLETA DE PAGO - FERROTEK SAC**")
        print("-------------------------------")
        print(f"NOMBRE: {self.trabajador.nombre}")
        print(f"CATEGORIA: {self.trabajador.categoria}")
        print(f"SUELDO BASICO: S/. {self.trabajador.calcular_pago_base():.2f}")
        print(f"DESCUENTO TARDANZAS: S/. {self.trabajador.calcular_descuento_tardanzas():.2f}")
        print(f"PAGO HORAS EXTRAS: S/. {self.trabajador.calcular_pago_hora_extra():.2f}")
        print(f"SUELDO NETO: S/. {self.trabajador.calcular_salario_mensual():.2f}")

# Ejemplo de uso:
print("---------------------")
print("**DATOS DE ENTRADA**")
print("----------------------")
nombre_trabajador = input("TRABAJADOR: ")
categoria_trabajador = input("CATEGORIA: ")
horas_extras = int(input("HORAS EXTRAS: "))
tardanzas_minutos = int(input("TARDANZA:(minutos) "))

trabajador = Trabajador(nombre_trabajador, categoria_trabajador.upper(), horas_extras, tardanzas_minutos)
boleta = Boleta(trabajador)
boleta.generar_boleta()


