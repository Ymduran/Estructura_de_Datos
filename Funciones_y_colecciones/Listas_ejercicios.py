print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" * Durán Breceda Lourdes Jamileth                                   * ")
print(" *                                                                  * ")
print(" * Fecha: 12 noviembre del 24                                       * ")
print(" *                                                                  * ")
print(" * Descripción:                                                     * ")
print(" * listas                                                           * ")
print(" * * * * * * * * * * * * * * * * * * * * * * * * * * *  * * * * * * * ")
print(" ")
print(" ")

'''
'''

def menu ():
    print(" Favoritos; Videos de youtube")
    print(" ** Menú: ** ")
    print("[1].- Ver lista de videos por añadidos")
    print("[2].- Ver lista de videos por orden A-Z")
    print("[3].- Ver lista de videos por orden Z-A")
    print("[4].- Añadir video ")
    print("[5].- Añadir varios videos")
    print("[6].- Eliminar videos")
    print("[7].- Salir")

nombre_video = [ ]



def lista_a_mostrar(opcion):
    if opcion == 1:
        len(nombre_video)  # ver lista por añadidos
    elif opcion == 2:
        nombre_video.sort()  # ver lista por A-Z
    elif opcion == 3:
        nombre_video.sort(reverse=True) #Ver lista por Z-A
    elif opcion == 4: #Añadir video
        video_añadir = input("Ingrese nombre del video a añadir: ")
        nombre_video.append(video_añadir)
    elif opcion == 5: #Añadir varios videos
        cantidad_videos_anadir = int(input("ingrese cuántos videos añadirá: "))
        for i in range (0,cantidad_videos_anadir ):
            video_añadir = input("Ingrese nombre del video a añadir: ")
            nombre_video.append(video_añadir)
    elif opcion == 6: #Eliminar videos
        video_eliminar = input("ingrese nombre del video a eliminar: ")
        nombre_video.remove(video_eliminar) # eliminación por referecia

    return nombre_video

#FUNCI
def mostrar_lista (nombre_video):
    print(nombre_video, end = " ")
    print(" ")
    print(" ")




flag = 0
while flag == 0:
    menu()
    opcion = int(input("Elige una opción: "))
    lista_a_mostrar(opcion)
    if opcion == 7:
        print("Saliendo...")
        flag = 1
    else:
        mostrar_lista(nombre_video)





