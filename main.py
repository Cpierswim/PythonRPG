from character import *
import random

def get_main_player():
    return Character("Hercules", 100)

def get_opponents():
    temp_list = []
    for i in range(0, 1):
        attacker_name = f"Attacker{i + 1}"
        temp_list.append(Character(attacker_name, 30))
    return temp_list

def all_opponents_alive():
    for opponent in opponents:
        if(not opponent.is_alive()):
            return False
    return True

def get_string_of_actions(player):
    return_string = f"The hero {player.name} can "
    list_of_attack_types = list(player.attack_types.keys())
    for i in range(len(list_of_attack_types)):
        return_string += list_of_attack_types[i] + ", "
    return_string = return_string.removesuffix(", ")
    if(len(list_of_attack_types) > 1):
        temp = return_string.rfind(",") + 2
        first_part = return_string[:temp]
        second_part = return_string[temp:]
        return_string = first_part + "and " + second_part
    return return_string

def print_status_string():
    print("")
    print("")
    print(f"The hero {main_player.name} has {main_player.HP} HP")
    print(f"The opponent {opponents[0].name} has {opponents[0].HP} HP")
    print(get_string_of_actions(main_player))
    
def player_attack(attacking_opponent, defending_opponent, attack_name):

    if attack_name in attacking_opponent.attack_types:
        defending_opponent.perform_attack(main_player.attack_types[attack_name])
        print(f"{attacking_opponent.name} performs {attack_name} on {defending_opponent.name} for {main_player.attack_types[attack_name]} HP")
    else:
        print("That attack type isn't available, you miss your turn")

def get_random_attack(player):
    list_of_attack_types = list(player.attack_types.keys())
    return list_of_attack_types[random.randrange(0, len(list_of_attack_types) - 1)]

main_player = get_main_player()
opponents = get_opponents()

while(main_player.is_alive() and all_opponents_alive()):
    
    print_status_string()
    selected_attack = input("What would you like to do: ")
    selected_attack = selected_attack.lower()
    player_attack(main_player, opponents[0], selected_attack)
    if(opponents[0].is_alive()):
        random_attack = get_random_attack(opponents[0])
        player_attack(opponents[0], main_player, random_attack)
        if not main_player.is_alive():
            print(f"{main_player.name} has died")
    else:
        print(f"{opponents[0].name} has died")


        




