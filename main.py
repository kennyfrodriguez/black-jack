import random
from art import logo
import os 

#Init
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def init():
  print(logo)
def player_start():
  player_hand = []
  player_hand.append(check_face(deal_card()))
  player_hand.append(check_face(deal_card()))
  print(f"This is your starting hand: {player_hand}")
  return player_hand
def computer_start():
  computer_hand = []
  computer_hand.append(check_face(deal_card()))
  print(f"This is the computer's first card: {computer_hand}")
  return computer_hand



#Checks and Actions
def check_face(card):
  if card == 11:
    return "Jack"
  elif card == 12:
    return "Queen"
  elif card == 13:
    return "King"
  elif card == 1:
    return "Ace"
  else:
    return card

def get_score(hand):
  total = 0
  for card in hand:
    if card == "Jack" or card == "Queen" or card == "King":
      card = 10
      total += card
    elif card == "Ace":
      if total + 11 > 21:
        card = 1
        total += card
      else:
        card = 11
        total += card
    else:
      total += card

  return total

def deal_card():
  card = random.choice(cards)
  return card

def get_hit(hand):
  hand.append(check_face(deal_card()))
  return hand

def deal_and_win(player_hand):
  player_score = get_score(player_hand)
  if player_score == 21:
    return "Player-W"
  elif player_score > 21:
    return "Player-L"

def win_conditions(player_hand,computer_hand):
  player_score = get_score(player_hand)
  computer_score = get_score(computer_hand)
  if computer_score > 21 or player_score == 21 or player_score > computer_score and player_score <= 21:
    return "Player-W"
  elif player_score > 21 or computer_score == 21 or computer_score > player_score and computer_score <= 21:
    return "COM-W"
  else:
    return "Draw"

def computer_deals(computer_hand):
  computer_score = get_score(computer_hand)
  while computer_score < 17:
    computer_hand.append(check_face(deal_card()))
    computer_score = get_score(computer_hand)
  return computer_hand

#Game
def main():
  init()
  player = player_start()
  hit = "y"  #default value
  print(f"This is your total score:{get_score(player)}")
  computer = computer_start()
  print("\n")

  #Check 
  check_win = win_conditions(player,computer)


  
  while hit == "y":
    #hit?
    hit = input("Type 'y' to get another card, type 'n' to pass: ")
    print("\n")
    hit = hit.lower()
    #check if hit
    if hit == "y":
      player = get_hit(player)
      print(f"This is your hand: {player}")
      print(f"This is your new score:{get_score(player)}")
      print("\n")
      if deal_and_win(player) == "Player-W":
        print("You win!")
        break
      elif deal_and_win(player) == "Player-L":
        print("You lose!")
        break
        
    if hit == "n":
      computer = computer_deals(computer)
      check_win = win_conditions(player,computer)
      if(check_win == "Player-W"):
        print(f"This is your total score:{get_score(player)}")
        print(f"Computer's Hand:{computer}")
        print(f"Computer:{get_score(computer)}")
        print("You win!")
        break
      elif(check_win == "COM-W"):
        print(f"This is your total score:{get_score(player)}")
        print(f"Computer's Hand:{computer}")
        print(f"Computer's Score:{get_score(computer)}")
        print("You lose!")
        break
      else:
        print("Draw! Push!")
  play_again = input("Would you like to play again? (y/n): ")
  play_again = play_again.lower()
  if(play_again == "y"):
    os.system('clear')
    return main()
  else:
    print("Thanks for playing!")

main()