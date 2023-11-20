#Rock paper scissor ASCII

Rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
Scissor = """ 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

#Klasifikasi

import random

print("WELCOME TO RPS THE GAME")

#PLAYER COMMAND
PlayerRPS = input("Pilih Batu, Kertas dan Gunting dengan memasukkan 0,1 dan 2  ")
playerRPS1 = int(PlayerRPS)

if playerRPS1 == 0:
    print("Anda Memilih Batu")
    print (Rock)
    
elif playerRPS1 == 1:
    print("Anda Memilih Kertas")
    print (Paper)
else:
    print("Anda Memilih Gunting")
    print (Scissor)
 

    
#COMPUTER COMMAND

RPScomp = random.randint(0,2)

if RPScomp == 0:
    print("Komputer Memilih Batu")
    print (Rock)
elif RPScomp == 1:
    print("Komputer Memilih kertas")
    print (Paper)
else:
    print("Komputer Memilih Gunting")
    print(Scissor)
   
int(RPScomp) 

#Fitur Game
if RPScomp == playerRPS1:
    print("HASIL SERI")
elif RPScomp == 0 and playerRPS1 == 1:
    print("Anda Menang")
elif RPScomp == 0 and playerRPS1 == 2:
    print("Anda Kalah")
elif RPScomp == 1 and playerRPS1 == 0:
    print("Anda Kalah")
elif RPScomp == 1 and playerRPS1 ==2:
    print("Anda Menang")
elif RPScomp == 2 and playerRPS1 == 0:
    print("Anda Menang")
elif RPScomp == 2 and playerRPS1 ==1:
    print("Anda Kalah")
    
print("Made By YUMANA")   