''' 
Una aplicación de delivery de comida rápida en el cual uno como usuario/cliente
puede registrarse con una cuenta con nombre, teléfono, y locación (para la entrega del
pedido) para posteriormente realizar pedidos de comida, bebida, postres, entre otros.
Para después pagar su pedido ingresando el número de su tarjeta de crédito para poder
confirmar la transacción y presentar una factura electrónica de su pedido como
confirmación final de este.
'''

import datetime 
import requests
import os
import argparse
import re
import json

from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd, FR
from holidays.constants import JAN, MAY, AUG, OCT, NOV, DEC
from holidays.holiday_base import HolidayBase


class FeriadoEcuador(HolidayBase):
    """
    Una clase que representa las vacaciones en Ecuador por provincia (FeriadoEcuador)
    Su objetivo es determinar si una fecha específica sea un feriado lo más rápido
    y flexible posible.
    https://www.turismo.gob.ec/wp-content/uploads/2020/03/CALENDARIO-DE-FERIADOS.pdf
    ...
    Atributos (Hereda la clase FeriadoEcuador)
    ----------
    prov: str
        código de provincia según ISO3166-2
    Metodos
    -------
    __init__(self, placa, date, time, online=False):
        Construye todos los atributos necesarios para el objeto FeriadoEcuador.
    _populate(self, year):
        Devuelve si una fecha es festiva o no
    """     
    # ISO 3166-2 códigos de las principales subdivisiones, 
    # llamadas provincias
    # https://es.wikipedia.org/wiki/ISO_3166-2:EC
    PROVINCES = ["EC-P"]  # TODO añadir más provincias

    def __init__(self, **kwargs):
        """
        Construye todos los atributos necesarios para el objeto FeriadoEcuador.
        """         
        self.pais = "ECU"
        self.prov = kwargs.pop("prov", "ON")
        HolidayBase.__init__(self, **kwargs)

    def _populate(self, year):
        """
        Comprueba si una fecha es festiva o no
        
        Parametros
        ----------
        year : str
            year of a date
        Retorna
        -------
        Devuelve True si una fecha es festiva, en caso contrario False 
        """                    
        # Año Nuevo
        self[datetime.date(year, JAN, 1)] = "Año Nuevo [New Year's Day]"
        
        # Navidad
        self[datetime.date(year, DEC, 25)] = "Navidad [Christmas]"
        
        # Semana Santa
        self[easter(year) + rd(weekday=FR(-1))] = "Semana Santa (Viernes Santo) [Good Friday)]"
        self[easter(year)] = "Día de Pascuas [Easter Day]"
        
        # Carnaval
        total_lent_days = 46
        self[easter(year) - datetime.timedelta(days=total_lent_days+2)] = "Lunes de carnaval [Carnival of Monday)]"
        self[easter(year) - datetime.timedelta(days=total_lent_days+1)] = "Martes de carnaval [Tuesday of Carnival)]"
        
        # Dia de trabajo
        name = "Día Nacional del Trabajo [Labour Day]"
        # (Ley 858/Ley de Reforma a la LOSEP (vigente desde el 21 de diciembre de 2016 /R.O # 906)) Si el feriado cae en 
        # sábado o martes el descanso obligatorio pasará al viernes o lunes inmediato anterior respectivamente
        if year > 2015 and datetime.date(year, MAY, 1).weekday() in (5,1):
            self[datetime.date(year, MAY, 1) - datetime.timedelta(days=1)] = name
        # (Ley 858/Ley de Reforma a la LOSEP (vigente desde el 21 de diciembre de 2016 /R.O # 906)) 
        # si el feriado cae en domingo el descanso obligatorio pasará al lunes siguiente
        elif year > 2015 and datetime.date(year, MAY, 1).weekday() == 6:
            self[datetime.date(year, MAY, 1) + datetime.timedelta(days=1)] = name
        # (Ley 858/Ley de Reforma a la LOSEP (vigente desde el 21 de diciembre de 2016 /R.O # 906)) Los feriados que sean
        # en miércoles o jueves se trasladarán al viernes de esa semana
        elif year > 2015 and  datetime.date(year, MAY, 1).weekday() in (2,3):
            self[datetime.date(year, MAY, 1) + rd(weekday=FR)] = name
        else:
            self[datetime.date(year, MAY, 1)] = name
        
        # Batalla del Pichincha, las reglas son las mismas que las del día del trabajo
        name = "Batalla del Pichincha [Pichincha Battle]"
        if year > 2015 and datetime.date(year, MAY, 24).weekday() in (5,1):
            self[datetime.date(year, MAY, 24).weekday() - datetime.timedelta(days=1)] = name
        elif year > 2015 and datetime.date(year, MAY, 24).weekday() == 6:
            self[datetime.date(year, MAY, 24) + datetime.timedelta(days=1)] = name
        elif year > 2015 and  datetime.date(year, MAY, 24).weekday() in (2,3):
            self[datetime.date(year, MAY, 24) + rd(weekday=FR)] = name
        else:
            self[datetime.date(year, MAY, 24)] = name        
        
        # Primer Grito de la Independencia, las reglas son las mismas que las del día del trabajo
        name = "Primer Grito de la Independencia [First Cry of Independence]"
        if year > 2015 and datetime.date(year, AUG, 10).weekday() in (5,1):
            self[datetime.date(year, AUG, 10)- datetime.timedelta(days=1)] = name
        elif year > 2015 and datetime.date(year, AUG, 10).weekday() == 6:
            self[datetime.date(year, AUG, 10) + datetime.timedelta(days=1)] = name
        elif year > 2015 and  datetime.date(year, AUG, 10).weekday() in (2,3):
            self[datetime.date(year, AUG, 10) + rd(weekday=FR)] = name
        else:
            self[datetime.date(year, AUG, 10)] = name       
        
        # Independencia de Guayaquil, las reglas son las mismas que las del día del trabajo
        name = "Independencia de Guayaquil [Guayaquil's Independence]"
        if year > 2015 and datetime.date(year, OCT, 9).weekday() in (5,1):
            self[datetime.date(year, OCT, 9) - datetime.timedelta(days=1)] = name
        elif year > 2015 and datetime.date(year, OCT, 9).weekday() == 6:
            self[datetime.date(year, OCT, 9) + datetime.timedelta(days=1)] = name
        elif year > 2015 and  datetime.date(year, MAY, 1).weekday() in (2,3):
            self[datetime.date(year, OCT, 9) + rd(weekday=FR)] = name
        else:
            self[datetime.date(year, OCT, 9)] = name        
        
        # Día de los difuntos
        namedd = "Día de los difuntos [Day of the Dead]" 
        # Independence of Cuenca
        nameic = "Independencia de Cuenca [Independence of Cuenca]"
        # (Ley 858/Ley de Reforma a la LOSEP (vigente desde el 21 de diciembre de 2016 /R.O # 906))
        # Para los feriados nacionales y/o locales que coincidan en días continuos,
        # se aplicarán las siguientes reglas:
        if (datetime.date(year, NOV, 2).weekday() == 5 and  datetime.date(year, NOV, 3).weekday() == 6):
            self[datetime.date(year, NOV, 2) - datetime.timedelta(days=1)] = namedd
            self[datetime.date(year, NOV, 3) + datetime.timedelta(days=1)] = nameic     
        elif (datetime.date(year, NOV, 3).weekday() == 2):
            self[datetime.date(year, NOV, 2)] = namedd
            self[datetime.date(year, NOV, 3) - datetime.timedelta(days=2)] = nameic
        elif (datetime.date(year, NOV, 3).weekday() == 3):
            self[datetime.date(year, NOV, 3)] = nameic
            self[datetime.date(year, NOV, 2) + datetime.timedelta(days=2)] = namedd
        elif (datetime.date(year, NOV, 3).weekday() == 5):
            self[datetime.date(year, NOV, 2)] =  namedd
            self[datetime.date(year, NOV, 3) - datetime.timedelta(days=2)] = nameic
        elif (datetime.date(year, NOV, 3).weekday() == 0):
            self[datetime.date(year, NOV, 3)] = nameic
            self[datetime.date(year, NOV, 2) + datetime.timedelta(days=2)] = namedd
        else:
            self[datetime.date(year, NOV, 2)] = namedd
            self[datetime.date(year, NOV, 3)] = nameic  
            
        # Fundación de Quito, se aplica sólo a la provincia de Pichincha, 
        # las reglas son las mismas que las del día del trabajo
        name = "Fundación de Quito [Foundation of Quito]"        
        if self.prov in ("EC-P"):
            if year > 2015 and datetime.date(year, DEC, 6).weekday() in (5,1):
                self[datetime.date(year, DEC, 6) - datetime.timedelta(days=1)] = name
            elif year > 2015 and datetime.date(year, DEC, 6).weekday() == 6:
                self[(datetime.date(year, DEC, 6).weekday()) + datetime.timedelta(days=1)] =name
            elif year > 2015 and  datetime.date(year, DEC, 6).weekday() in (2,3):
                self[datetime.date(year, DEC, 6) + rd(weekday=FR)] = name
            else:
                self[datetime.date(year, DEC, 6)] = name


def Menu():
    '''
    Para la creacion del menu principal se hace la utiliza de un bucle While 
    con condicion de True la cual pobroca bucle infinito, en el cual si ingresa
    una opcion mal siguira pidiendo el dato hasta que ingrese uno correcto.
    1. como primera opcion se registra unba cuentade usuario en la aplicacion delibery
    2. como segunda opcion se llama al metodo de iniciar sesion,
       para despues continuar con el menu de pedidos
    3. como tercera opcion se ejecuta un break y se cierra el programa
    '''
    while(True): # bucle infinito mientras que el valor de la condicion devuelva false
        print("==============================================")
        print("||               EASY SERVICE               ||")
        print("==============================================")
        print("|| 1.- CREAR CUENTA                         ||")
        print("|| 2.- INICIO SESION                        ||") 
        print("|| 3.- SALIR                                ||")
        print("==============================================")
        opcion=int(input("Bienvenido, ¿Qué desea realizare hoy?: "))
        if(opcion == 1):
            cliente1.crearCuenta()
        elif(opcion == 2):
            # como segunda opcion se llama al metodo de iniciar sesion,
            # para despues continuar con el menu de pedidos
            #cliente1.iniciarSesion()
            usuario1.MenuCompras()
        elif(opcion == 3):
            # como tercera opcion se ejecuta un break y se cierra el programa
            print("Gracias por visitarnos :)")
            break

'''def MenuUsuario():
    
    Para la creascion del menu principal se hace la utiliza de un bucle While 
    con condicion de True la cual pobroca bucle infinito, en el cual si ingresa
    una opcion mal siguira pidiendo el dato hasta que ingrese uno correcto.
    1. como primera opcion se ingresa a la opcion de compras de la aplicacion delibery
    2. como segunda opcion se ingresa a la opcion de pagos de la aplicacion delibery
    3. como tercera opcion se ejecuta un break y se regresa al menu principal
    
    while(True): # bucle infinito mientras que el valor de la condicion devuelva false
        print("==============================================")
        print("||        BIENVENIDO A EASY SERVICE         ||")
        print("||==========================================||")
        print("|| 1.- MENU DE COMPRAS                      ||")
        print("|| 2.- MENU DE PAGOS                        ||")
        print("|| 3.- SALIR DE SESION                      ||")
        print("==============================================")
        opcion=int(input("Bienvenido, ¿Qué desea realizar el dia de hoy?: "))
        if(opcion == 1):
            usuario1.MenuCompras() #Llamada al metodo de Menu Compras
        elif(opcion == 2):
            # como segunda opcion se llama al metodo de iniciar sesion,
            # para despues continuar con el menu de pedidos
            usuario1.MetodoPago()
            ''''''
        elif(opcion == 3):
            # como tercera opcion se ejecuta un break y se cierra el programa
            break
''' 

class Cliente():
    ''' 
    Clase en donde se guardaran todos los datos que ingresa el 
    Clienta como el usuario y la clave de este mismo.
    ...
    Atributos
    ----------
    apellido : str
        Usuario del cliente registrado en el sistema 
    telefono : int
        Telefono del cliente registrado en el sistema 
    cedula : int
        Cedula del cliente registrado en el sistema 
    direccion : str
        Direccion del cliente registrado en el sistema en la cual el
        pedido del delibery sera entregado
    _usuario: str
        El usuario del cliente asignada por el sistema a partir del
        resto de datos ingresados por el cliente
    _clave: str
        La clave del cliente asignada por el sistema a partir del
        resto de datos ingresados por el cliente
    ...
    Metodos
    -------
    __init__(self):
        Construye todos los atributos necesarios para el objeto Cliente.
    crearCuenta(self):
        Se realizan el ingreso de los datos principales del cliente para
        poder crear el usuario y la clave a partir de estos datos.
    iniciarSesion(self):
        Se realiza el ingreso de usuario y la clave, y se los compara con
        los valores de usuario y clave anteriormente registrados en el sistema
    '''
    def __init__(self):
        ''' 
        Construye todos los atributos necesarios para el objeto Cliente.
        '''
        # atributos publicos
        # atributo protegido
        self._usuario = "usuario"
        self._clave = "clave"
        
    def crearCuenta(self):
        '''
        Se realizan el ingreso de los datos principales del cliente para
        poder crear el usuario y la clave a partir de estos datos.
        '''
        self.nombre=str(input( "Ingrese su Nombre: " ))
        self.apellido=str(input( "Ingrese su Apellido: " ))
        self.direccion=str(input( "Ingrese su Dirrecion de domicilio: " ))
        self.telefono=str(input( "Ingrese su Telefono: "))
        self.cedula=str(input( "Ingrese su Cedula: " ))
        self._usuario=self.nombre+self.apellido+self.cedula[7:]
        self._clave=self.direccion[:3]+self.telefono[6:8]+self.cedula[7:]
        print("================================================================")
        print("   REGISTRO SATISFACTORIO, DESDE AHORA ERES NUESTRO/A CLIENTE   ")
        print("================================================================")
        print("Su usuario sera: ", self._usuario)
        print("Su clave sera: ", self._clave)
        
    def iniciarSesion(self):
        '''
        Se realiza el ingreso de usuario y la clave, y se los compara con
        los valores de usuario y clave anteriormente registrados en el sistema
        '''
        while True:
            usuarioIngresado=str(input( "Ingrese su usuario: " ))
            if usuarioIngresado!=self._usuario:
                print("Valor no valido, el usuario ingresado es incorrecto")
            else:
                break
        while True:
            claveIngresado=str(input( "Ingrese su usuario: " ))
            if claveIngresado!=self._clave:
                print("Valor no valido, la clave ingresada es incorrecto")
            else:
                break
        print("Bienvenido Señor/a ",self.apellido,". Usted a ingresado su cuenta correctamente")
    
class MenuPedidos():
    '''
    Una clase que representa el menu de pedidosen donde el cliente
    a travez de su usuario pude realizar sus pedidos de comida
    haciendo uso de los atributos publicos y protegidos
    ...
    Atributos
    ----------
    Carrito : int
        
    menuPrincipal : list
        Se encuentran registrados todos los alimentos que se tiene 
        disponibles dentro del app de delibery
    ...
    Metodos
    -------
    _init_(self):
        Construye todos los atributos necesarios para el objeto Empleado.
    MenuCompras(self):
        Se muestrra el nombre, el salario y el correo del empleado
    ''' 
    def __init__(self):
        ''' 
        Construye todos los atributos necesarios para el objeto Cliente.
        '''
        self.Carrito=0
        self.cantidadCompras=[0,0,0,0,0,0,0,0,0,0]
        self.menuPrincipal=[
                "Combo 1",
                "Combo 2",
                "Combo 3",
                "Combo Snack",
                "Hamburguesa Crispy",
                "Hamburguesa Bacon",
                "Alitas picantes",
                "Ensalada Easy",
                "Festin Familiar"]
        self.precios=["2.00","2.00","2.00","2.50","3.00","3.00","4.00","2.50","5.00"]

    def MenuCompras(self):
        while(True):
            print("===================================================================")
            print("||                       MENU DE COMPRAS                         ||")
            print("||===============================================================||")
            print("|| 1.- Combo 1            $ 2.00 || 6.- Hamburguesa Bacon $ 3.00 ||")
            print("|| 2.- Combo 2            $ 2.00 || 7.- Alitas picantes   $ 4.00 ||")
            print("|| 3.- Combo 3            $ 2.00 || 8.- Ensalada Easy     $ 2.50 ||")
            print("|| 4.- Combo Snack        $ 2.50 || 9.- Festin Familiar   $ 5.00 ||")
            print("|| 5.- Hamburguesa Crispy $ 3.00 ||                              ||")
            print("||---------------------------------------------------------------||")
            print("|| 10.- REVISAR CARRITO          || 11.- REALIZAR PAGO           ||")
            print("||---------------------------------------------------------------||")
            print("||                       12.- VOLVER ATRAS                       ||")
            print("===================================================================")
            opcion=int(input("¿Qué desea comprar el dia de hoy?: "))
            if (opcion == 1):
                usuario1.Ordenamiento(1,2)
            elif(opcion == 2):
                usuario1.Ordenamiento(2,2)
            elif(opcion == 3):
                usuario1.Ordenamiento(3,2)
            elif(opcion == 4):
                usuario1.Ordenamiento(4,2.5)
            elif(opcion == 5):
                usuario1.Ordenamiento(5,3)
            elif(opcion == 6):
                usuario1.Ordenamiento(6,3)
            elif(opcion == 7):
                usuario1.Ordenamiento(7,4)
            elif(opcion == 8):
                usuario1.Ordenamiento(8,2.5)
            elif(opcion == 9):
                usuario1.Ordenamiento(9,2.5)
            elif(opcion == 10):
                print(self.cantidadCompras)
            elif(opcion == 11):
                usuario1.MetodoPago()
            elif(opcion == 12):
                break
    def Ordenamiento(self, numeroCompra, precioProducto):
        print(self.menuPrincipal[numeroCompra-1])
        while(True):
            confirmacion=str(input("Desea ordenar (si/no): " ))
            confirmacion=confirmacion.lower()
            if confirmacion=="si":
                while True:
                    cantidad=int(input("¿Cuantos desea ordenar?: " ))
                    if cantidad<=0:
                        print("Valor no valido, la clave ingresada es incorrecto")
                    else: break
                self.Carrito=cantidad*precioProducto
                print("Su cuenta Es hora es de: ",self.Carrito)
                self.cantidadCompras[numeroCompra-1]+=cantidad
                break
            elif confirmacion=="no":
                break
            else:
                print("Opcion incorrecta, ingrese nuevamente")


class PagoPedidos(MenuPedidos):
    ''' 
    Una clase en donde se realizan los pagos de los productos y se guardaran
    todos los pedidos realizados por el cliente al momento de realizar
    su compra.
    ...
    Atributos
    ----------
    _numTarjeta : int
        El numero de la targeta del usuario registrado al sistema con la
        cual se pagan los pedidos.
    _claveTarjeta : int
        La clave de la targeta del usuario y la cual da la confirmacion
        de que se pueda realizar el pago.
    ...
    Métodos
    -------
    _init_(self):
        Construye todos los atributos necesarios para el objeto PagoPedidos.
    MetodoPago(self):
    
    PagoTotal(self):
        
    ''' 
    def __init__(self):
        ''' 
        Construye todos los atributos necesarios para el objeto PagoPedidos.
        '''
        self.subTotal=0
        # atributo privado
        self.__numTarjeta = 0
        self.__claveTarjeta = 0
        MenuPedidos.__init__(self)
    
    def MetodoPago(self):
        while(True):
            print("==============================================")
            print("||             METODO DE PAGO               ||")
            print("==============================================")
            print("|| 1.- TARJETA                              ||")
            print("|| 2.- EFECTIVO                             ||")
            print("|| 3.- CANCELAR                             ||")
            print("==============================================")
            opcionPago=int(input("¿Por cual metodo de pago desea seguir?: " ))
            if opcionPago==1:
                usuario1.TipoPago()
                usuario1.PagoTotal()
                break
            elif opcionPago==2:
                usuario1.PagoTotal()
                break
            elif opcionPago==3:
                break
            else:
                print("Opcion incorrecta, ingrese nuevamente")

    def TipoPago(self):
        while True:
            self._numTarjeta=int(input("Ingrese el numero de su targeta de credito: " ))
            if self.__numTarjeta<10 and self.__numTarjeta>10:
                print("Valor no valido, el numero de targeta ingresado es incorrecto")
            else:
                break
        while True:
            self._claveTarjeta=int(input("Ingrese la fecha de vencimiento de su targeta de credito: " ))
            if self.__claveTarjeta<3 and self.__claveTarjeta>3:
                print("Valor no valido, la clave ingresada es incorrecto")
            else:
                break
    
    def PagoTotal(self):
        '''
        '''
        
        print("=============================================")
        print("||           FACTURA EASY SERVICE          ||")
        print("||-----------------------------------------||")
        print("|| CLIENTE:",cliente1.apellido,cliente1.nombre)
        print("|| CEDULA: ",cliente1.cedula,"                   ||")
        print("||-----------------------------------------||")
        print("|| CANTIDAD  PRECIO    PEDIDO              ||")
        for i in range (0,10):
            if (self.cantidadCompras[i]>0):
                precioEspecifico=self.cantidadCompras[i]*float(self.precios[i])
                self.subTotal+=precioEspecifico
                print("||   ",self.cantidadCompras[i],"     $",precioEspecifico,"   ",self.menuPrincipal[i])
        
        print("|| SUBTOTAL ",self.subTotal,"                          ||")
        
        print("||                                         ||")
        print("=============================================")

        
if __name__ == '__main__':
    cliente1=Cliente() # Instanciar objeto de la clase Cliente
    usuario1=MenuPedidos() # Instanciar objeto de la clase MenuPedidos
    usuario1=PagoPedidos() # Instanciar objeto de la clase PagoPedidos
    Menu()



