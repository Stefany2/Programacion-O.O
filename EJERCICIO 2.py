class Usuario:
    def __init__(self, nombre, apellidos, email, contraseña):
        self._nombre = nombre
        self._apellidos = apellidos
        self._email = email
        self._contraseña = contraseña

    # Propiedades para obtener los atributos privados
    @property
    def nombre(self):
        return self._nombre

    @property
    def apellidos(self):
        return self._apellidos

    @property
    def email(self):
        return self._email

    @property
    def contraseña(self):
        return self._contraseña

    # Métodos de acceso para modificar los atributos privados
    @nombre.setter 
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @apellidos.setter
    def apellidos(self, nuevos_apellidos):
        self._apellidos = nuevos_apellidos

    @email.setter
    def email(self, nuevo_email):
        self._email = nuevo_email

    @contraseña.setter   #para controlar el acceso y modificación de los atributos privados de la clase.
    def contraseña(self, nueva_contraseña):
        self._contraseña = nueva_contraseña

    def modificar(self, nombre=None, apellidos=None, email=None, contraseña=None):
        if nombre is not None:
            self.nombre = nombre
        if apellidos is not None:
            self.apellidos = apellidos
        if email is not None:
            self.email = email
        if contraseña is not None:
            self.contraseña = contraseña

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellidos: {self.apellidos}\nEmail: {self.email}\nContraseña: {self.contraseña}"


# Ejemplo de uso:
usuario = Usuario("Mariana", "Perez", "1459565@gmail.com", "contraseña_segura")

print("Información del usuario:")
print(usuario)

# Modificar el usuario
usuario.modificar(apellidos="Martinez", contraseña="nueva_contraseña")

print("\nInformación actualizada del usuario:")
print(usuario)
