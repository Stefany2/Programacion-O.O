class Trabajador:
    def __init__(self):
        self.trab = input("\nTrabajador: ")
        self.cat = input("Categoria: ")
        self.HorExtr = input("Horas extras: ")
        self.tard = input("Tardanza: ")


class Boleta:
    def __init__(self):
        self.TrabajadorClass = Trabajador()
        self.nombre = self.TrabajadorClass.trab
        self.categoria = self.TrabajadorClass.cat
        self.horaExtra = self.TrabajadorClass.HorExtr
        self.tardanza = self.TrabajadorClass.tard

    def opera(self):
        worker = self.nombre
        category = self.categoria
        horaExtra = float(self.horaExtra)
        tardanza = float(self.tardanza)

        # VALIDACION DE TIPO EMPLEADO
        if category.lower() == "a":
            salary = 3000

            descuentoTardanza = ((salary/240)/60)*tardanza
            pagoPorHorasExtras = (salary/240)*horaExtra
            print(f"""\n
            NOMBRE: {worker} 
            CATEGORIA: {category}
            SUELDO BASICO: {salary}
            DESCUENTO TARDANZA: {descuentoTardanza:.2f}
            PAGO POR HORAS EXTRAS: {pagoPorHorasExtras:.2f}
            SUELDO NETO: {salary - descuentoTardanza + pagoPorHorasExtras:.2f}\n""")

        elif category.lower() == "b":
            salary = 2500
            descuentoTardanza = ((salary/240)/60)*tardanza
            pagoPorHorasExtras = (salary/240)*horaExtra
            print(f"""\n
            NOMBRE: {worker} 
            CATEGORIA: {category}
            SUELDO BASICO: {salary}
            DESCUENTO TARDANZA: {descuentoTardanza:.2f}
            PAGO POR HORAS EXTRAS: {pagoPorHorasExtras:.2f}
            SUELDO NETO: {salary - descuentoTardanza + pagoPorHorasExtras:.2f}\n""")

        elif category.lower() == "c":
            salary = 2000
            descuentoTardanza = ((salary/240)/60)*tardanza
            pagoPorHorasExtras = (salary/240)*horaExtra
            print(f"""\n
            NOMBRE: {worker} 
            CATEGORIA: {category}
            SUELDO BASICO: {salary}
            DESCUENTO TARDANZA: {descuentoTardanza:.2f}
            PAGO POR HORAS EXTRAS: {pagoPorHorasExtras:.2f}
            SUELDO NETO: {salary - descuentoTardanza + pagoPorHorasExtras:.2f}\n""")


a = Boleta()
a.opera()

