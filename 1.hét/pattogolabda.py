#Pyton 3.5.3

import os
from time import sleep

a = 0

while True:
    sleep(0.06)
    os.system('clear')
    height, width = os.popen('stty size', 'r').read().split()

    height = int(height)-3
    width = int(width)


    x = abs( ( a % ( ( width - 3 ) * 2 ) ) - ( ( a * 2 ) % ( ( width - 3 ) * 2 ) ) ) + 1
    y = abs( ( a % ( ( height - 2 ) * 2 ) ) - ( ( a * 2 ) % ( ( height - 2 ) * 2 ) ) ) + 1

    a += 1

    # Felso vonal
    for i in range (0, width):
        print ('-', end=''),


    # Sorok a labda folott
    for i in range (0, y-1):
        print ('|', end=''),
        for j in range(1, width-1):
            print (' ', end=''),
        print ('|', end='')


    # A labda sora
    print ('|', end=''),
    for i in range (0, x-1):
        print (' ', end=''),
    print ('x', end=''),
    for j in range (1, width-x-1):
        print (' ', end=''),
    print ('|', end='')

    # Sorok a labda alatt
    for i in range (0, height-y-1):
        print ('|', end=''),
        for j in range(1, width-1):
            print (' ', end=''),
        print ('|', end='')

    # Also vonal
    for u in range (0, width):
        print ('-', end='')

    # Labda pozicioja
    print ('Labda', x, y)
