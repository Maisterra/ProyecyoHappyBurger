#Módulo Main
from pedidos import BaseDatosPedidos
from clientes import BaseDatosClientes
from menu import BaseDatosMenu

def main():
    """Imprimir un menú que permite al usuario elegir la opción deseada y se direcciona al módulo seleccionado
    """
    while True:
        #imprimir el menú
        print("¿Qué módulo desea utilizar?")
        print("1. Módulo de Pedidos")
        print("2. Módulo de Clientes")
        print("3. Módulo de Menú")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        #Mandar mensaje de la opción seleccionada y direccionar al módulo correspondiente
        if opcion == '1':
            print("Has seleccionado Pedidos")
            pedidos=BaseDatosPedidos()
            pedidos.gestion_pedidos()
        elif opcion == '2':
            print("Has seleccionado Clientes")
            clientes=BaseDatosClientes()
            clientes.gestion_clientes()
        elif opcion == '3':
            print("Has seleccionado Menú")
            menu=BaseDatosMenu()
            menu.gestion_menu()
        elif opcion == '4':
            print("Hasta Luego!!!!")
            break
        else:
            #En caso de opción inválida pedir selección valida
            print("Opción inválida. Seleccione una opción válida.")

if __name__ == "__main__":
    main()