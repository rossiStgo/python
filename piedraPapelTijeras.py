import random

opciones=["piedra","papel","tijeras"]

    
def jugar(rondas):

    pts_usr=0
    pts_maq=0

    for i in range(rondas):
        print(f"\nRonda {i+1}\n")
        
        while True:
            opc_usr= input("Escriba su selección (piedra, papel, tijeras): ")    
            if opc_usr.lower() in opciones:
                print(f"\nUsted ha elegido {opc_usr.upper()}")
                break
            else:
                print("La opción elegida no es válida. Intente de nuevo...")

        opc_maq=random.choice(opciones)
        print(f"La máquina ha elegido {opc_maq.upper()}\n")
        
        if opc_maq==opc_usr.lower():
            pts_usr+=1
            pts_maq+=1
            print(f"Mano empatada, puntaje: usted: {pts_usr} - máquina: {pts_maq}")
        elif opciones.index(opc_maq)==opciones.index(opc_usr)-1:
            pts_usr+=2
            print("Usted ha ganado la ronda, puntuación parcial:")
        else:
            pts_maq+=2
            print("Usted ha perdido la ronda, puntación parcial:")
            
        print(f"""
usted: {pts_usr}
máquina: {pts_maq}

===========================================================""")
              
    if pts_usr==pts_maq:
        mensaje="La partida ha finalizado empatada"
    elif pts_usr>pts_maq:
        mensaje="Felicitaciones!!! Ha ganado la partida"
    else:
        mensaje="Usted ha sido derrotado por la máquina. Puede intentarlo nuevamente."
        
    return f"""
            {mensaje.center(70)}
            ========================================================================

            Puntajes finales:

            Usted: {pts_usr}
            Máquina: {pts_maq}
            
            ========================================================================
            """

def ingresarManos():

    while True:
        rondas=input("Ingrese cantidad de manos que desa jugar: ")

        if rondas.isdigit():
            print(f"Usted jugará con la máquina {rondas} rondas")
            break
        else:
            print("La cantidad ingresada de rondas no es correcta, ingrese un número entero")
            continue
    return int(rondas)


def menu():
    return """
                Juego de Piedra, papel o tijeras
            =======================================

            1. Jugar contra la máquina
            2. Salir

            """

while True:

    print(menu())
    opcion=input("Seleccione una opción del menú anterior: ")
    
    if opcion=="1":
        print(jugar(ingresarManos()))
    elif opcion=="2":
        print("Saliendo del juego...")
        break
    else:
        print("Opción incorrecta, intente nuevamente.")
    

        
