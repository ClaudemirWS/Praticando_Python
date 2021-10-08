import pygame #importa biblioteca pygame

pygame.init()
pygame.mixer.music.load('tocandomp3.mp3') #carrega música pelo nome
pygame.mixer.music.play() #inicia reprodução
input('Pressione ENTER para terminar a música') #termina a redrodução mediante input

