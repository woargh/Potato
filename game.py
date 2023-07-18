import random

def create_player(): # adding characters with different stats.
  character = input("Choose an adventurer: Warrior, mage or ranger?").lower()
  if character not in ["warrior", "mage", "ranger"]:
    print("You actually managed to fail to choose a character!Well done Stanley!")
  if character == "warrior" :
    return {
        "health": 150,
        "food": 100,
        "sanity": 100,
    }
  elif character == "mage":
    return {
        "health": 50,
        "food": 100,
        "sanity": 200,
    }
  elif character == "ranger":
    return {
        "health": 80,
        "food": 150,
        "sanity": 120,
    }

def create_location():
    return {
        "food":    round(random.random(), 2),
        "medicine": round(random.random(), 2),
        "art":     round(random.random(), 2),
        "damage":  round(random.random(), 2),
        "WTF!?":   round(random.random(), 2),
    }

def show_dict(d):
    for key in (d.keys()):
        print(f"- {key}: {d[key]}")

def game_step(player):    
    print("You stumble upon a new location:")
    location = create_location()    
    show_dict(location)

    while (action := input("Explore? (y/n): ").lower()) not in ["y", "n"]:
        print("Invalid input")

    if action == "n":
        print("You decided to keep walking")
        return
    else:
        print("You explore the location:")

    result = {
        key: (random.random() < val) for key,val in location.items()
    }  #items ? location.items? that comma thingy?

    show_dict(result)
    input("Press ENTER to continue")    

def main():
    player = create_player()

    while True:
        print("Another day begins ##############################################")
        game_step(player)

main()



