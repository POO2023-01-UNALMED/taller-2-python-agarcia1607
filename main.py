class Asiento():
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro
    def cambiarColor(self,color):
        if color=="rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco":
          self.color=color
        else:
          pass

class Motor():
    def __init__(self,numeroCilindros,tipo,registro):
       self.numeroCilindros=numeroCilindros
       self.tipo=tipo
       self.registro=registro
    def cambiarRegistro(self,numero):
        self.registro=numero
    def asignarTipo(self,cambio):
        if cambio=="electrico" or cambio=="gasolina":
            self.tipo=cambio
        else:
            pass
class Auto():
  cantidadCreados=0
  def __init__(self,modelo,precio,asientos,marca,motor,registro):
     self.modelo=modelo
     self.precio=precio
     self.asientos=asientos
     self.marca=marca
     self.motor=motor
     self.registro=registro
  def cantidadAsientos(self):
    return (len(self.asientos))
  def verificarIntegridad(self):
    x=self.asientos[0].registro
    if self.asientos!=None
        for i in self.asientos:
        if i.registro==x==self.motor.registro:
            pass
        else:
            return "Las piezas no son originales"
        return "Auto original"
    else:
        return "Auto original"
