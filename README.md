# -NRC_6181-_JhosueChica_ProyectoUnidad1
'''
El programa comenzará dando la bienvenida al cliente con un menú de inicio el cual contará con 3 opciones al elegir una, 
el valor de la respuesta pasará por varias estructuras de control IF en la cual dependiendo del valor de esta respuesta 
se presentará alguna de las opciones del menú. Caso contrario: si la opción que se ingresó no existe en el menú, 
simplemente no presentará un mensaje de que la opción no existe y volverá al principio. 
.
Caso 1: En el primer caso se llamara al método crearCuenta de la clase Cliente en donde el cliente creara su usuario 
a partir de ingresar su nombre, apellido, dirección, teléfono y cédula, en donde el usuario tomara distintos valores 
de sus datos para crear un usuario y una clave de este mismo para el cliente, para después volver al menú principal. 
.
Caso 2: En el segundo caso el programa se le pedirá al cliente un usuario y una clave para poder iniciar sesión, estos 
valores se compararan con el usuario y la clave ya registrados anteriormente y el programa no continuara hasta ingresar 
correctamente el usuario y la clave. Después de validar el usuario y la clave se llamará al método de la clase MenuPedidos 
en donde se presentaran un menú en donde se podrá escoger que producto agregar al carrito y la cantidad de este mismo. 
Además, contará con una opción para presentar los alimentos ya agregados al carrito, otra la cual llamara al método de la 
clase PagoPedidos para poder realizar el pago en donde al finalizar este se presentara una factura electrónica. 
.
Caso 3: En el tercer caso se saldrá del programa sin ningún tipo de problema.
'''
