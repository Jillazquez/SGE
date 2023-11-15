import random
import time

# Definimos las dimensiones de la pantalla
WIDTH, HEIGHT = 80, 24

# Creamos una lista para almacenar las gotas
drops = [0] * WIDTH

def main():
    while True:
        # Dibujamos cada gota
        for i in range(WIDTH):
            # Si la gota llegó al final de la pantalla, la reiniciamos en la parte superior
            if drops[i] >= HEIGHT or random.random() > 0.95:
                drops[i] = 0

            # Borramos la gota en su posición actual
            draw(i, drops[i], ' ')

            # Movemos la gota hacia abajo
            drops[i] += 1

            # Dibujamos la gota en su nueva posición
            draw(i, drops[i], chr(9608))  # El carácter 9608 es un bloque sólido

        # Hacemos una pausa antes de dibujar el siguiente cuadro
        time.sleep(0.1)

def draw(x, y, char):
    # Movemos el cursor a la posición especificada
    print('\033[%d;%dH' % (y + 1, x + 1), end='')

    # Dibujamos el carácter
    print(char, end='')

    # Movemos el cursor fuera de la pantalla para evitar problemas con el desplazamiento del texto
    print('\033[25;0H', end='')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
