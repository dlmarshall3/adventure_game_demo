import time

def start():
  #initial prompts
  print("You open your eyes, confused. \nYou find yourself sitting in the middle of an open field, fog all around you. \nThe last place you remember being was...")
  time.sleep(2)
  print("A) A shark tank\nB) A burrito\nC) A monster truck rally")
  answer1 = input(">>> ")
  time.sleep(1)
  print(f"That's right, you remind yourself.\nYou had fallen asleep on your sofa chair watching Shark Week after a good Chipotle dinner and a night at the races.)")
  time.sleep(3)
  print('Anyway, you decide to brush off your Keds and evaluate your surroundings more. \n There are a few strange smells, you notice, but one sticks out more than the others.')
  time.sleep(3)
  print('1) Sulfur \n2) Meat on a grill \n3) Garbage')
  answer2 = input(">>> ")
  time.sleep(1)
  print('You realize the sulfur smell is unbearable, overpowering the smell of steak, and also the garbage. Thankfully.')
  time.sleep(2)
  print('Then it hits you.')
  time.sleep(2)
  print('You really thought the steak was the most powerful smell.')
  time.sleep(2)
  print('Do my choices here not really matter? you muse.')


start()