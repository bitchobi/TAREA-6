# Método para introducir puntuación y comentarios
def introducir_puntuacion():
    while True:  # Bucle para asegurar que la puntuación es válida
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()  # Entrada de puntuación
        if point.isdecimal():  # Verifica si la entrada es un número
            point = int(point)  # Convierte la entrada a un entero
            if point <= 0 or point > 5:  # Verifica si la puntuación está fuera de rango
                print('Indíquelo en una escala de 1 a 5')  # Mensaje de error
            else:
                print('Introduzca sus comentarios.')
                comment = input()  # Entrada de comentarios
                post = f'punto: {point} comentario: {comment}'  # Formatea la entrada
                with open("data.txt", 'a') as file_pc:  # Abre el archivo en modo agregar
                    file_pc.write(f'{post}\n')  # Escribe la entrada en el archivo
                break  # Sale del bucle si la entrada es válida
        else:
            print('Introduzca los puntos de valoración como números')  # Mensaje de error si la entrada no es un número

# Método para comprobar los resultados guardados
def comprobar_resultados():
    print('Resultados hasta la fecha.')
    with open("data.txt", "r") as read_file:  # Abre el archivo en modo lectura
        print(read_file.read())  # Imprime el contenido del archivo

# Método para terminar el programa
def terminacion():
    print('Terminación.')

# Método principal para seleccionar el proceso
def seleccionar_proceso():
    while True:  # Bucle principal para seleccionar la acción
        print('Seleccione el proceso que desea aplicar')
        print('1: Introduzca los puntos de valoración y los comentarios.')
        print('2: Comprueba los resultados obtenidos hasta ahora.')
        print('3: Terminación.')
        num = input()  # Entrada de selección

        if num.isdecimal():  # Verifica si la entrada es un número
            num = int(num)  # Convierte la entrada a un entero

            if num == 1:
                introducir_puntuacion()  # Llama al método para introducir puntuación
            elif num == 2:
                comprobar_resultados()  # Llama al método para comprobar resultados
            elif num == 3:
                terminacion()  # Llama al método de terminación
                break  # Sale del bucle principal
            else:
                print('Introduzca de 1 a 3')  # Mensaje de error si la selección no es válida
        else:
            print('Introduzca de 1 a 3')  # Mensaje de error si la entrada no es un número

# Llamada a la función principal para iniciar el programa
seleccionar_proceso()  # Inicia el bucle principal para la selección del proceso