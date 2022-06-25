import pygame
import time
import sys
pygame.init
print("[?]: Hi.")
time.sleep(1)
yourName = input("[?]: My name is Sam. What's your name? ")
if yourName == "Sam" or yourName == "sam":
  print("[Sam]: Oh! We have the same name! (Not for long though...)")
else:
  print("[Sam]: Nice to meet you, "+ yourName + ".")
time.sleep(2)
print("[Sam]: ...")
time.sleep(2)
hearRain = input("[Sam]: Do you...hear that? [Y/N]")
print("Droplets of water begin raining down the screen.")
if hearRain == "Y" or hearRain == "y":
  print("[Sam]: Yeah? You hear it too, right? Come to think of it, this space is pretty cramped. If there's more water, this place will be flooded.")
  time.sleep(3)
  print("Water starts pouring at a rapid rate.")
  time.sleep(4)
  print("[Sam]: Help me, " + yourName +"!")
  time.sleep(1)
  saveSam= input("Press a to break a hole in the window.")
  if saveSam== "a":
    print("The water drains out of the room. Sam looks at you with sad eyes.")
    time.sleep(4)
    print("[Sam]: Thank you so much. I owe you my life.")
    time.sleep(3)
    discover = input("[You]: Don't mention it. [Stay/Leave]")
    if discover == "stay" or discover=="Stay":
      print("Something seems off about Sam. You stay.")
      time.sleep(3)
      print("Sam closes his eyes and smiles a sad smile.")
      time.sleep(2)
      print("[Sam]: You get it don't you. You haven't saved me.")
      time.sleep(4)
      print("[Sam]: The truth is, I'm dying of an illness. That's why I'm so blue all the time.")
      time.sleep(3)
      print("[Sam]: I guess I'm cursed to live...for now.")
      time.sleep(5)
      print("End: You saved a boy. But he tells you otherwise.")
    elif discover == "leave" or discover == "Leave":
      print("End: You leave, satisfied that you saved Sam. You don't hear the slumping of a weakened body in the background.")
  else:
    print("Sam's room overfills until you start getting flooded as well.")
    time.sleep(3)
    print("End: You both know this is how it was meant to be. Sam smiles his last smile at you.")

else:
  print("[Same]: What was that? You don't hear anything? Must be my imagination then, I guess.")
  time.sleep(3)
  print("Water starts filling up the room.")
  time.sleep(2)
  print("[Sam]: Wha-what's going on?")
  time.sleep(0.5)
  print("[Sam]: H-HELP!")
  time.sleep(2)
  print("You don't hear him.")
  print("The water is coming up to his chin.")
  time.sleep(3)
  print(yourName+" please! Why can't you hear me? I'm drowngguguglugrrgrurgrg")
  time.sleep(3)
  print("You watch as Sam struggles in the water. Soon, his screams can't be heard, for real this time. His blue body becomes one with the water.")
  time.sleep(7)
  print("You turn to leave, but as you start to walk, you feel a droplet on the back of your neck.")
  time.sleep(5)
  print("End: You let a boy drown. But at what cost?")

