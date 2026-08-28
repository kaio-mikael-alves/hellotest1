import pygame, os, random
pygame.init()
pygame.mixer.init()
music = [R"c:\Users\alves\Music\Playlists\power_of_love_future.mp3.mp3",
         r'c:\Users\alves\Music\Playlists\Never_gonna_give_you_up.mp3',
         r'c:\Users\alves\Music\Playlists\eye_of_the_tiger.mp3.mp3',
         r'c:\Users\alves\Music\Playlists\IRON_MAN_black_sabbad.mp3'
         ]

indice = 0
tocando = True
tempo = 0
pygame.mixer.music.load(music[indice])

while True:

    print('\n1-tocar \n2-pausar \n3-continuar \n4-parar \n5-próxima \n6-anterior \n7-volume \n8-end \n9-aleátorio')

    opction = input('escolha: ')
    

    if opction == '1':

        pygame.mixer.music.play()
        print(os.path.basename(music[indice]))
        tocando = True

    elif opction == '2':

        pygame.mixer.music.pause()

    elif opction == '3':

        pygame.mixer.music.unpause()
    
    elif opction == '4':

        pygame.mixer.music.stop()
        tocando = False

    elif opction == '5':
        indice +=1
        if indice >= len(music):
            indice = 0
        pygame.mixer.music.load(music[indice])
        pygame.mixer.music.play()
        print(os.path.basename(music[indice]))
    elif opction == '6':
        indice -=1
        if indice <= len(music):
            indice = 0
        pygame.mixer.music.load(music[indice])
        pygame.mixer.music.play()
        print(os.path.basename(music[indice]))
    elif opction == '7':

        vol=float(input('selecione o volume de 0.0 a 1.0: \n'))
        pygame.mixer.music.set_volume(vol)
    elif opction == '8':

        break
    elif opction == '9':
        indice = random.randint(0, len(music) - 1)
        pygame.mixer.music.load(music[indice])
        pygame.mixer.music.play()
        print(os.path.basename(music[indice]))

    if not pygame.mixer.music.get_busy():
        indice += 1
        if indice >= len(music):
           indice = 0

        pygame.mixer.music.load(music[indice])
        pygame.mixer.music.play()
    