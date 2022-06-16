''' 
Una aplicación de delivery de comida rápida en el cual uno como usuario/cliente
puede registrarse con una cuenta con nombre, teléfono, y locación (para la entrega del
pedido) para posteriormente realizar pedidos de comida, bebida, postres, entre otros.
Para después pagar su pedido ingresando el número de su tarjeta de crédito para poder
confirmar la transacción y presentar una factura electrónica de su pedido como
confirmación final de este.
'''

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
            # cliente1.iniciarSesion()
            usuario1.MenuCompras()
        elif(opcion == 3):
            # como tercera opcion se ejecuta un break y se cierra el programa
            print("Gracias por visitarnos :)")
            break

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
        while True:
            self.telefono=str(input( "Ingrese su Telefono: "))
            if (len(self.telefono)==10):
                break
            else:
                print("Valor no valido, el telefono ingresao es incorrecto")
        while True:
            self.cedula=str(input( "Ingrese su Cedula: " ))
            if (len(self.cedula)==10):
                break
            else:
                print("Valor no valido, el telefono ingresao es incorrecto")
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
    Carrito : float
    
    cantidadCompras
    
    menuPrincipal : list
        Se encuentran registrados en una lista todos los alimentos 
        que se tiene disponibles dentro del app de delibery
    precios : list
        Se encuentran registrados en una lista los precios de todos los 
        alimentos que se tiene disponibles dentro del app de delibery
    ...
    Metodos
    -------
    _init_(self):
        Construye todos los atributos necesarios para el objeto Empleado.
    MenuCompras(self):
        Menu en donde se encuentran registrados los detalles de los productos
        y donde se pueden llamar a metodos para revisan y pagar por los productos
        agregados al carrito de compras
    Ordenamiento(self, numeroCompra, precioProducto):
        Realiza la confirmacion y añade al carrito la cantidad de compras
        especificada por el usuario
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
        ''' 
        Menu en donde se encuentran registrados los detalles de los productos
        y donde se pueden llamar a metodos para revisan y pagar por los productos
        agregados al carrito de compras
        '''
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
                usuario1.Ordenamiento(9,5)
            elif(opcion == 10):
                for i in range (0,10):
                    if (self.cantidadCompras[i]>0):
                        print("  ",self.cantidadCompras[i],"   ",self.menuPrincipal[i])
            elif(opcion == 11):
                usuario1.MetodoPago()
            elif(opcion == 12):
                break
    def Ordenamiento(self, numeroCompra, precioProducto):
        ''' 
        Realiza la confirmacion y añade al carrito la cantidad de compras
        especificada por el usuario
        '''
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
                subprecio=cantidad*precioProducto
                self.Carrito+=subprecio
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
    Atributos (Hereda la clase MenuPedidos)
    ----------
    total : int
        La cantidad total de las compras a pagar, despues de aplicar el IVA
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
        Se pregunta por que medio desea realizar el el pago de las compras
    PagoTarjeta(self):
        Se especifican los detalles necesarios para poder realizar un pago con targeta
    PagoTotal(self):
        Se construye la factura con los vslores de las compras, el subtotal, IVA y 
        el total de la compra registrada
    ''' 
    def __init__(self):
        ''' 
        Construye todos los atributos necesarios para el objeto PagoPedidos.
        '''
        self.total=0
        # atributo privado
        self.__numTarjeta = 0
        self.__claveTarjeta = 0
        '''
        Se llama al constructor de la clase MenuPedidos
        '''
        MenuPedidos.__init__(self)
    
    def MetodoPago(self):
        '''
        Se pregunta por que medio desea realizar el pago de las compras
        '''
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
                usuario1.PagoTarjeta()
                usuario1.PagoTotal()
                break
            elif opcionPago==2:
                usuario1.PagoTotal()
                break
            elif opcionPago==3:
                break
            else:
                print("Opcion incorrecta, ingrese nuevamente")

    def PagoTarjeta(self):
        '''
        Se especifican los detalles necesarios para poder realizar un pago con targeta
        '''
        while True:
            self.__numTarjeta=int(input("Ingrese el numero de su targeta de credito: " ))
            if (len(str(self.__numTarjeta))>9 and len(str(self.__numTarjeta))<=10):
                break
            else:
                print("Valor no valido, el numero de targeta ingresado es incorrecto")
                
        while True:
            self.__claveTarjeta=int(input("Ingrese la fecha de vencimiento de su targeta de credito: " ))
            if (len(str(self.__claveTarjeta))>2 and len(str(self.__claveTarjeta))<=3):
                break
            else:
                print("Valor no valido, la clave ingresada es incorrecto")
    
    def PagoTotal(self):
        '''
        Se construye la factura con los vslores de las compras, el subtotal, IVA y 
        el total de la compra registrada
        '''
        print("=============================================")
        print("||           FACTURA EASY SERVICE          ||")
        print("||-----------------------------------------||")
        print("|| CLIENTE:",cliente1.apellido,cliente1.nombre)
        print("|| CEDULA: ",cliente1.cedula,"                    ||")
        print("||-----------------------------------------||")
        print("|| CANTIDAD  PRECIO    PEDIDO              ||")
        for i in range (0,10):
            if (self.cantidadCompras[i]>0):
                precioEspecifico=self.cantidadCompras[i]*float(self.precios[i])
                print("||   ",self.cantidadCompras[i],"     $",precioEspecifico,"   ",self.menuPrincipal[i])
        iva=self.Carrito*0.12
        self.total=self.Carrito+iva
        print("||-----------------------------------------||")
        print("|| SUBTOTAL $",self.Carrito)
        print("||    IVA   $",iva)
        print("||   TOTAL  $",self.total)
        print("=============================================")
        self.Carrito=0
        self.cantidadCompras=[0,0,0,0,0,0,0,0,0,0]

if __name__ == '__main__':
    cliente1=Cliente() # Instanciar objeto de la clase Cliente
    usuario1=MenuPedidos() # Instanciar objeto de la clase MenuPedidos
    usuario1=PagoPedidos() # Instanciar objeto de la clase PagoPedidos
    Menu()
