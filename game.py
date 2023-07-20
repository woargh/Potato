import random

# make a dictonary with the character stats.

stats = {"adventurer" : None, "health": None, "food": None, "sanity": None}


# add characters with different stats - K
def create_player(character): 
  if character == "warrior" :
    return {
        "health": 150,
        "hunger": 100,
        "sanity": 100,
        "backpack": {"food": 0, "medicine": 0, "art": 0},
        "backpack_capacity": 12
    }
  elif character == "mage":
    return {
        "health": 50,
        "hunger": 100,
        "sanity": 200,
        "backpack": {"food": 0, "medicine": 0, "art": 0},
        "backpack_capacity": 5
    }
  elif character == "ranger":
    return {
        "health": 80,
        "hunger": 150,
        "sanity": 120,
        "backpack": {"food": 0, "medicine": 0, "art": 0},
        "backpack_capacity": 7
    }
  elif character == "bottlefighter":
    return {
        "health": 100,
        "hunger": 300,
        "sanity": 1,
        "backpack": {"food": 0, "medicine": 0, "art": 0},
        "backpack_capacity": 10
    }


def create_location():
    return {
        "food":    round(random.random(), 2),
        "medicine": round(random.random(), 2),
        "art":     round(random.random(), 2),
        "damage":  round(random.random(), 2),
        "Antediluvian horrors":   round(random.random(), 2),
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

    location_content = {
        key: (random.random() < val)*random.randint(1,10) for key,val in location.items()
    }
    show_dict(location_content)

    autoresolve(player,location_content)
    print("Status")
    show_dict(player)
    pickup_items(player, location_content) 
 

    input("Press ENTER to continue")    

    # will manipulate the dictionary created here in a way so that stats are saved for the character.  


def autoresolve(player, location_content):
   player["health"] -= location_content["damage"]
   player["sanity"] -= location_content["Antediluvian horrors"]

def pickup_items(player, location_content):
   while True:
      resource, num = input("What do you choose to store in your backpack?").split()
      num = int(num)
      if location_content[resource] < num:
        print("You cheeky bastard!")
        continue
      player["backpack"][resource] += num
      location_content[resource] -= num
      show_dict(player["backpack"])
      show_dict[location_content]

    





def main():
    character = input("Choose an adventurer: Warrior, mage, ranger or bottlefighter ?").lower()
    if character not in ["warrior", "mage", "ranger", "bottlefighter"]:
        print("You actually managed to fail to choose a character! Well done Stanley!")

    player = create_player(character)

    while True:
        print("Another day begins ##############################################")
        game_step(player)

if __name__ == "__main__" : main()
