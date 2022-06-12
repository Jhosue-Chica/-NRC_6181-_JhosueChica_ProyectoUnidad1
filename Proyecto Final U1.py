''' 
Una aplicación de delivery de comida rápida en el cual uno como usuario/cliente
puede registrarse con una cuenta con nombre, teléfono, y locación (para la entrega del
pedido) para posteriormente realizar pedidos de comida, bebida, postres, entre otros.
Para después pagar su pedido ingresando el número de su tarjeta de crédito para poder
confirmar la transacción y presentar una factura electrónica de su pedido como
confirmación final de este.
'''

class Restaurante():
    ''' 
    Clase en sonde se guardaran todos los productos que se pueden
    llegar a comprar como comida, bebida, postres, entre otros.
    ...
    Atributos
    ----------
    menuLista : list
        Se encuentran registrados todos los alimentos que se tiene 
        disponibles dentro del app de delibery
    Metodos
    -------
    _init_(self, nombre, salario, proyecto):
        Construye todos los atributos necesarios para el objeto Restaurante.
    '''
    def _init_(self):
        self.menuPrincipal=["Combo 1",
                            "Combo 2",
                            "Combo 3",
                            "Combo Snack",
                            "Hamburguesa Crispy",
                            "Hamburguesa Bacon",
                            "Alitas picantes",
                            "Ensalada Easy",
                            "Festin Familiar",]
        
        self.menuAgregados=["Papas fritas",
                            "Cola",
                            "Ensalada",
                            "Helado",]
        
class Cliente():
    def __init__(self, usuario, clave):
        ''' 
        Construye todos los atributos necesarios para el objeto Cliente.
        ...
        Parametros
        ----------
        usuario : str 
            Usuario del cliente registrado en el sistema 
        clave : int
            Clave referente al usuario del cliente
        proyecto : str
            Proyecto en el que se encuentra registrado el empleado
        '''
        # atributos publicos
        self.usuario = usuario
        self.clave = clave
        # atributo protegido

    
class MenuPedidos(Restaurante):
    """
    Una clase que representa el menu de pedidosen donde el cliente
    a travez de su usuario pude realizar sus pedidos de comida
    haciendo uso de los atributos publicos y protegidos
    ...
    Atributos
    ----------
    nombre : str 
        Nombre del empleado registrado 
    salario : float
        Salario del empleado reistrado
    proyecto : str
        Proyecto en el que se encuentra registrado el empleado
    self._correo
        Correo de la empresa en la que trabaja el empleado, 
        la cual actua como un Atributo protegido
    self.__contrsena
        Contraseña del correo de la empresa en la que trabaja el empleado,
        la cual actua como un Atributo privado
    Metodos
    -------
    _init_(self, nombre, salario, proyecto):
        Construye todos los atributos necesarios para el objeto Empleado.
    mostrar(self):
        Se muestrra el nombre, el salario y el correo del empleado
    ingresarContra(self):
        Se ingresa la contraseña la cual funje como un atributo privado,
        Si la contraseña es ingresada correctamente continuara con la ejecucion
        en caso contrario se repitira hasta que se ingrese correctamente.
    trabajo(self):
        Muestra el estado actual del empleado dentro de la empresa
    """ 

    
class PagoPedidos():
    ''' 
    Clase en sonde se realizan los pagos de los productos y se guardaran
    todos los pedidos realizados por el cliente al momento de realizar
    su compra.
    ...
    Atributos
    ----------
    menuLista : list
        Se encuentran registrados todos los alimentos que se tiene 
        disponibles dentro del app de delibery
    Metodos
    -------
    _init_(self, nombre, salario, proyecto):
        Construye todos los atributos necesarios para el objeto Restaurante.
    ''' 




