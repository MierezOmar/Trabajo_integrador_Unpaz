import string
import random
import time


#GENERAR CONTASEÑA
dia_semana = input("\nPor favor, ingresa el día de la semana: ").capitalize()

def generarContra(longitud):
    letrasMayus = string.ascii_uppercase
    letrasMinus = string.ascii_lowercase
    numeros = string.digits

    contrasena = [
        random.choice(letrasMayus),
        random.choice(letrasMinus),
        random.choice(numeros)
    ]

    for i in range(longitud - 3):
        contrasena.append(random.choice(letrasMayus + letrasMinus + numeros))

    random.shuffle(contrasena)
    return ''.join(contrasena)

long_Selecc = 0
while long_Selecc < 4:
    long_Selecc = int(input("\nIntroducir cuantos caracteres deseada para la contraseña (debe tener al menos 4 caracteres): "))
    if long_Selecc < 4:
        print("\n***** La longitud debe ser al menos de 4 para incluir todos los tipos de caracteres *****")
    else:
        contraGenerada = generarContra(long_Selecc)
        print("\nTu contraseña aleatoria es:", contraGenerada)

#CATALOGO DE PRODUCTO
productos = {
    "Camisas": {"detalles": ["camisetas", "camisas de vestir", "camisas informales", "camisas de manga corta", "camisas de manga larga"], 
                "precios": [20000, 30000, 25000, 15000, 22000]},
    "Pantalones": {"detalles": ["pantalones vaqueros", "pantalones chinos", "pantalones de vestir", "pantalones cortos"], 
                   "precios": [40000, 35000, 45000, 25000]},
    "Vestidos": {"detalles": ["vestidos casuales", "vestidos de cóctel", "vestidos de noche", "vestidos formales", "vestidos estampados"], 
                 "precios": [50000, 60000, 80000, 70000, 55000]},
    "Trajes": {"detalles": ["trajes de dos piezas", "trajes de tres piezas", "trajes formales", "trajes de oficina"], 
               "precios": [100000, 150000, 120000, 110000]},
    "Ropa de abrigo": {"detalles": ["abrigos", "chaquetas", "chaquetones", "gabardinas", "chalecos"], 
                       "precios": [80000, 65000, 75000, 85000, 50000]},
    "Ropa deportiva": {"detalles": ["camisetas deportivas", "pantalones deportivos", "sudaderas", "leggings deportivos", "ropa de yoga"], 
                       "precios": [25000, 30000, 35000, 28000, 40000]},
    "Ropa de dormir": {"detalles": ["pijamas", "camisones", "batas", "pantalones de pijama", "conjuntos de dormir"], 
                       "precios": [30000, 35000, 40000, 25000, 45000]},
    "Accesorios": {"detalles": ["sombreros", "gorras", "bufandas", "guantes", "cinturones", "joyas", "bolsos"], 
                   "precios": [15000, 10000, 12000, 5200, 12000, 30000, 45000]}
}

#FUNCION DE LISTAR PRODUCTOS
def listarProductosYprecios(categoria):
    if categoria in productos:
        print(f"\nProductos en la categoría '{categoria}':")
        for detalle, precio in zip(productos[categoria]["detalles"], productos[categoria]["precios"]):
            print(f"- {detalle}: ${precio}")
    else:
        print("La categoría no existe.")

#MENU PRINCIPAL 
menu= """
MENU:

1-LISTAR PRODUCTOS
2-AGREGAR PRODUCTOS AL CARRITO
3-VER CARRITO
4-ELIMINAR PRODUCTOS DEL CARRITO
5-FINALIZAR LA COMPRA"""

#FUNCION AGREGAR AL CARRITO
product= ["Camisas","Pantalones","Vestidos","Trajes","Ropa de abrigo","Ropa deportiva","Ropa de dormir","Accesorios"]
carrito = []     

def agregarAlCarrito():
    print("\n*******CATEGORIAS*******")
    for i in range(len(product)):
        print(f"\n•{product[i]}")
    categoria = input("\nIntroduce la categoría del producto: ").title()
    if categoria in productos:
        listarProductosYprecios(categoria)
        detalle = input("\nIntroduce el detalle del producto que deseas agregar: ").lower()
        if detalle in productos[categoria]["detalles"]:
            indice = productos[categoria]["detalles"].index(detalle)
            precio = productos[categoria]["precios"][indice]
            contador = 1
            while True:
                cantidad = int(input("\nIntroduce la cantidad que deseas agregar: "))
                producto_encontrado = False
                if cantidad > 0:
                    for producto in carrito:
                        if producto['detalle'] == detalle:
                            producto['cantidad'] += cantidad
                            print(f"\nActualizaste la cantidad de {detalle} en el carrito.")
                            producto_encontrado = True
                            break
                    if not producto_encontrado:
                        carrito.append({'detalle': detalle, 'cantidad': cantidad, 'precio': precio})
                        print(f"\nAgregaste {cantidad} de {detalle} al carrito.")
                    for producto in carrito:
                        print(f"\nDetalle: {producto['detalle']}, Cantidad: {producto['cantidad']}, Precio: ${producto['precio']}")
                else:
                    if contador != 5: 
                        print("\n**** La cantidad debe ser entero positivo ****")
                        contador += 1
                    else:
                        print("***** USTED HA SIDO BLOQUEADO 60 SEGUNDOS, 5 INTENTOS MAL REALIZADO *****")
                        time.sleep(60)
        else:
            print("\n*********** El detalle del producto no existe en la categoría ************")
    else:
        print("\n******* La categoría no existe *******.")


#FUNCION ELIMINAR DEL CARRITO
def eliminarDelCarrito():
    for producto in carrito:
        print(f"\nDetalle: {producto['detalle']}, Cantidad: {producto['cantidad']}, Precio: ${producto['precio']}")
    detalle = input("\nIntroduce el detalle del producto que deseas eliminar: ").lower()
    cant_eliminar = int(input("\nIntroduce la cantidad que deseas eliminar: "))
    
    for item in carrito:
        if item['detalle'].lower() == detalle:
            if item['cantidad'] >= cant_eliminar:
                item['cantidad'] -= cant_eliminar
                print(f"Se eliminaron {cant_eliminar} unidades de {detalle} del carrito.")
                if item['cantidad'] == 0:
                    carrito.remove(item)
                return
            else:
                print(f"\nNo se puede eliminar {cant_eliminar} unidades porque solo hay {item['cantidad']} en el carrito.")
                return
    print("\n ******* El producto no está en el carrito *******")

#LISTAR PRODUCTOS AGREGADOS EN EL CARRITO
def verCarrito():
    if carrito ==  []:
        print("\n ************** NO HAY PRODUCTOS EN EL CARRITO ******************")
    else:
        for producto in carrito:
            print(f"\nDetalle: {producto['detalle']}, Cantidad: {producto['cantidad']}, Precio: ${producto['precio']}")

#FUNCION PARA FINALIZAR LA COMPRA
def finalizarCompra():
    def calcular_total_por_detalle(carrito):
        for item in carrito:
            total_detalle = item['cantidad'] * item['precio']
            print(f"\nDetalle: {item['detalle']}, Cantidad: {item['cantidad']}, Precio unitario: {item['precio']}, Total por detalle: {total_detalle}")

    def calcular_total_general(carrito):
        total_general = sum(item['cantidad'] * item['precio'] for item in carrito)
        return total_general

    calcular_total_por_detalle(carrito)
    total_general = calcular_total_general(carrito)
    print(f"\nTotal general de ventas: ${total_general}")
    return total_general

descuentos_tarjeta_dia = {
    'Domingo': {'VISSA BNNA': 0.15},
    'Lunes': {'MASTERCARD PRV': 0.20},
    'Martes': {'CENNSOCUD MNP': 0.15},
    'Miércoles': {'CLARESEN KFC': 0.30},
    'Jueves': {'OFFIOTA LUCRA': 0.20},
    'Viernes': {'TREVVI CIR': 0.10},
    'Sábado': {'PUETRA COM': 0.05}
}

#FUNCION PARA FORMA DE PAGOS
def forma_pago():
    def informacion_pagos():
    
        medio_de_pago = input("\nIngresa la forma de pago (Efectivo, Tarjeta de crédito, Bitcoin): ").capitalize()
        
        tarjeta = None
        cuotas = None
        if medio_de_pago == 'Tarjeta de credito':
            tarjeta = input("\nIngresa la tarjeta del Cliente: ").upper()
            cuotas = int(input("\nIngresa el número de cuotas (1,3, 6, 12): "))    
        return dia_semana, medio_de_pago, tarjeta, cuotas

    def pago_final(total_general, dia_semana, medio_de_pago, tarjeta=None, cuotas=None):
        if medio_de_pago == 'Efectivo':
            total_general *= 0.90  
        elif medio_de_pago == 'Bitcoin':
            pass  
        elif medio_de_pago == 'Tarjeta de credito':
            descuento = descuentos_tarjeta_dia.get(dia_semana, {}).get(tarjeta, 0)
            total_general *= (1 - descuento)
            if cuotas == 1:
                total_general *= 1.00
            elif cuotas == 3:
                total_general *= 1.12 
            elif cuotas == 6:
                total_general *= 1.18  
            elif cuotas == 12:
                total_general *= 1.36  
        return total_general

    dia_semana, medio_de_pago, tarjeta, cuotas = informacion_pagos()
    total_compra = finalizarCompra() 
    total_final = pago_final(total_compra, dia_semana, medio_de_pago, tarjeta, cuotas)
    print(f"\nEl total final a pagar es: ${total_final:.2f}")

#FUNCION PRINCIPAL TIENDA (MAIN)
def actividad_tienda():
    contador=1
    while True:
        print(menu)
        opcion = input("\nSeleccione una opción: ")
        if opcion == "1":
            for i in range(len(product)):
                listarProductosYprecios(product[i])
        elif opcion == "2":
            agregarAlCarrito()
        elif opcion == "3":
            verCarrito()
        elif opcion == "4":
            eliminarDelCarrito()
        elif opcion == "5":
            if carrito != []:
                finalizarCompra()
                forma_pago()
                break
            else:
                print("\n***** NO A AGREGADO PRODUCTOS AL CARRITO ******")
        else:
            if contador != 5: 
                print("\n **************** Opción no válida. Intente de nuevo ****************")
                contador+=1
            else:
                print("***** USTED HA SIDO BLOQUEADO 60 SEGUNDOS, 5 INTENTOS MAL REALIZADO *****")
                time.sleep(60)
                contador=1

#INICIO SESION 
cont=1 
while True:
    sesion= input("\nINGRESE CONTRASEÑA PARA INICIAR SESION: ")

    if contraGenerada == sesion:
        print ("\n ********** USTED A INISIADO SESION **********")
        actividad_tienda()
        break
    else:
        if cont == 5:
            print("\n ********* FIN DEL PROGRAMA A LLEGADO AL MAXIMO INTENTO 5 ***********")
            time.sleep(60)
            cont=1
        else:
            print(f"Intente la contraseña nuevamente {cont} ")
            cont+=1
