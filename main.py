""""
Name(s): Darren
Name of Project: FlotSam
"""
import pygame
import sys
pygame.init()
width, height = 500, 500
background = 0,  0,  0
screen = pygame.display.set_mode((width, height))
sam = pygame.image.load("boy.png")
samRect = sam.get_rect()
print("NOTE: THERE WERE A LOT OF THINGS I COULDN'T PUT INTO THIS PROJECT THAT I WANTED TO. FOR INSTANCE, THE PROGRAM WOULD NOT LET ME ADD A GIF, SO I WASN'T ABLE TO DISPLAY ALL THE FRAMES I WANTED AND THE CHARACTER IS JUST A STILL PICTURE. SORRY FOR THE LACKLUSTER GAME.")
while True: 
  screen.fill(background)
  screen.blit(sam, samRect)
  pygame.display.flip()
  import page1