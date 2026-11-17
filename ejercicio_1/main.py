#Desarrolla ejercicio_1/main.py. Un estacionamiento cobra por hora según la duración total de la estancia: 
# Horas 
# Tarifa por hora 
# 1 a 2 
# $15.00
# 3 a 5 
# $12.00 
# Más de 5 
# $10.00 
# La tarifa del rango correspondiente se aplica a TODAS las horas registradas. 
# • Crear la clase Estacionamiento. Su constructor __init__ recibe horas y las guarda como propiedad. 
# • Crear calcularPago() para devolver el importe total calculado con if/elif/else. 
# • Crear mostrarRecibo() que utilice calcularPago() y muestre horas e importe con dos decimales. 
# • En el programa principal, solicitar las horas, comprobar que sea un entero mayor que cero, crear un objeto y 
# llamar a mostrarRecibo(). 
# • Ejecutar al menos los casos de 2, 4 y 6 horas; guardar capturas de dos ejecuciones. 
# Ejemplo (4 horas): 
# Horas estacionadas: 4 
# RECIBO DE ESTACIONAMIENTO 
# Horas: 4 
# Total a pagar: $48.00 

class Estacionamiento(object):
    def __init__(self, horas):
        self.horas = horas

    def calcularPago(self):
        if self.horas <= 2:
            return self.horas * 15
        elif self.horas < 5:
            return self.horas * 12
        else:
            return self.horas * 10

    def mostrarRecibo(self):
        pago = self.calcularPago()
        print(f"Horas: {self.horas}, Importe: ${pago:.2f}")

    
    

if __name__ == "__main__":
    horas = int(input("Ingrese las horas de estacionamiento: "))
    if horas > 0:
        estacionamiento = Estacionamiento(horas)
        estacionamiento.mostrarRecibo()
    else:
        print("Por favor, ingrese un número entero mayor que cero.")

