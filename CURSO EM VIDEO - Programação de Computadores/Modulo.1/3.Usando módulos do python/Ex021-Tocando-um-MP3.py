import pygame
pygame.init()
pygame.mixer.music.load('Ex021-Tocando-um-MP3.mp3')
pygame.mixer.play()
pygame.event.wait()