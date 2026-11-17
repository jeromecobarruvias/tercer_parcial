# 1. ¿Cuál es el nombre de la clase? 
#  Producto
# 2. ¿Cuáles son sus propiedades?
#  nombre, precio, total
# 3. ¿Cuáles son sus métodos?
#  calcularTotal, mostrarTotal
# 4. ¿Qué función cumple __init__?
#  Inicializa las propiedades del objeto.
# 5. ¿Para qué se utiliza self?
#  Se utiliza para referirse a las propiedades y métodos del objeto actual.
# 6. ¿En qué instrucción se crea un objeto?
#  En la instrucción "producto1 = Producto("Cuaderno", 35)".
# 7. ¿Cuál es el nombre del objeto?
#  producto1
# 8. ¿Cómo se llama a calcularTotal()?
#  producto1.calcularTotal()
# 9. ¿Qué valores recibe el constructor cuando se crea el objeto?
#  "Cuaderno", 35
# 10. ¿Qué resultado mostrará el programa?
#  El nombre del producto y el total de la compra.



class Rectangulo(object): 
    def __init__(self, base, altura): 
        # COMPLETAR: guardar las propiedades
        self.base = base
        self.altura = altura

    def calcularArea(self):
        # COMPLETAR: regresar el área
        return self.base * self.altura

    def mostrarArea(self):
        # COMPLETAR: mostrar el resultado
        print(f"Área del rectángulo: {self.calcularArea()}")

# COMPLETAR: crear un objeto con base 8 y altura 5
rectangulo1 = Rectangulo(8, 5)
# COMPLETAR: llamar al método para mostrar el área
rectangulo1.mostrarArea()




# 1. ¿Cuál es la clase padre? 
#  Operacion
# 2. ¿Cuál es la clase hija? 
#  Multiplicacion
# 3. ¿Cómo se indica la herencia? 
#  Con la sintaxis "class Hija(Padre):"
# 4. ¿Qué propiedades utiliza la clase hija? 
#  numero1, numero2
# 5. ¿Por qué puede utilizarlas sin definir su propio __init__? 
#  Porque hereda el __init__ de la clase padre.
# 6. ¿Por qué los métodos calcular() tienen resultados distintos? 
#  Porque la clase hija sobrescribe el método calcular() para realizar una operación diferente.
# 7. ¿Qué valores se imprimen? 
# 12
# 32
# 8. ¿Qué sucedería si eliminamos calcular() de Multiplicacion?
#  Se llamaría al método calcular() de la clase padre, Operacion.