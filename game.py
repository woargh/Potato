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
        "resources": {
            "food":                 round(random.random(), 2),
            "medicine":             round(random.random(), 2),
            "art":                  round(random.random(), 2),
        },
        "effects": {
            "damage":               round(random.random(), 2),
            "Antediluvian horrors": round(random.random(), 2),
        },
    }

def dict_string(d):
    return "".join([
        "[",
        ", ".join(f"{key}={d[key]}" for key in sorted(d.keys())),
        "]"
    ])

def show_dict(title, d):
    print(title)
    for key in sorted(d.keys()):
        val = d[key]
        if isinstance(val, dict):
            val = dict_string(val)

        print(f"- {key}: {val}")
        
def game_step(player):
    location = create_location()        
    show_dict("You stumble upon a new location:", location)
    
    while (action := input("Explore? (y/n): ").lower()) not in ["y", "n"]:
        print("Invalid input")
    
    if action == "n":
        print("You decided to keep walking")
        return

    location_content = {
        kind: {
            key: (random.random() < val)*random.randint(1,10)
            for key,val in location[kind].items()
        }
        for kind in ["resources", "effects"]
    }
    
    show_dict("You explore the location:", location_content)

    autoresolve(player,location_content)
    show_dict("Status:", player)
    pickup_items(player, location_content)
    
    # will manipulate the dictionary created here in a way so that stats are saved for the character.
    return

def autoresolve(player, location_content):
    player["health"] -= location_content["effects"]["damage"]
    player["sanity"] -= location_content["effects"]["Antediluvian horrors"]

def pickup_items(player, location_content):
    while True:        
        command = input("What do you choose to store in your backpack?")
        if command == "quit": return
        
        resource, num = command.split()        
        num = int(num)
        
        if resource not in ["art", "food", "medicine"] or location_content["resources"][resource] < num:
            print("Fuck you!")
            continue

        print(f"You pick up {num} {resource}")
        
        player["backpack"][resource] += num
        location_content["resources"][resource] -= num
        
        show_dict("Location:", location_content)
        show_dict("Backpack:", player["backpack"])

def main():
    character = input("Choose an adventurer: Warrior, mage, ranger or bottlefighter?").lower()
    if character not in ["warrior", "mage", "ranger", "bottlefighter"]:
        print("You actually managed to fail to choose a character! Well done Stanley!")

    player = create_player(character)

    while True:
        print("Another day begins ##############################################")
        game_step(player)

if __name__ == "__main__" : main()
