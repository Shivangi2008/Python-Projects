#let's roll adice
import random

def roll_dice():
  return random.randint(1, 6)
def rollingDice():
  print("Rolling the dice...")
  print(f"You got: {roll_dice()}")
