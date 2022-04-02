import random

def main():

  # Get the number of dice to roll
  dice_rolls = 2
  dice_sum = 0
  for i in range(dice_rolls):
    # Roll the dice
    roll = random.randint(1,6)
    dice_sum += roll
    print(f'You rolled a {roll}')

  print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":
  main()