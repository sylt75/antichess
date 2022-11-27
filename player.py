import chess
import sys


player_type = ""
player_color = False

while player_type != "white" and player_type!="black":
    #print("\nEnter 'white' or 'black' only\n")
    player_type = input("black or white?\n")



if player_type == "white":
    player_color = True
    #print("true")
elif player_type == "black":
    player_color = False
    #print("false")




