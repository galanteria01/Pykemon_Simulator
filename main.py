import random
from modules.classes import *
from modules.spells import *

# Initialise the spells
fire_cinder = spells("Cinder",20)
fire_burn = spells("Burn",32)

water_splash = spells("Splash",18)
water_rain = spells("Rain",30)

rock_hit = spells("Hit",16)
rock_eruption = spells("Eruption",28)

grass_earthquake = spells("Earthquake",14)
grass_whip = spells("Whip",26)

common_heal = spells("Heal",20)

fire = [fire_cinder,fire_burn,common_heal]
water = [water_splash,water_rain,common_heal]
rock = [rock_hit,rock_eruption,common_heal]
grass = [grass_earthquake,grass_whip,common_heal]

# Initialising the characters
charizard = pokemon("Charizard",90,"FIRE",fire)
blastoise = pokemon("Blastoise",80,"WATER",water)
onix = pokemon("Onix",70,"ROCK",rock)
venusaur = pokemon("Venusaur",60,"GRASS",grass)

pykemons = [charizard, blastoise, onix, venusaur]

print("Welcome to pykemon!")
print("Can you become greatest pykemon training? \n")
print("Don't worry,Prof harry is here to give you your first pykemon: ")
print("Here are the three choices:")
choice = input("Press ENTER to choose from list")
if choice == "":
    for i in range(0,4):
        print("Pokemon no "+str(i+1))
        pykemons[i].about_me()
    choose = int(input("Enter your choosed pykemon: "))
    if choose == 1:
        default_pykemon = charizard
    elif choose == 2:
        default_pykemon = blastoise
    elif choose == 3:
        default_pykemon = onix
    elif choose == 4:
        default_pykemon = venusaur
    print("You have selected "+ default_pykemon.name+" as your first pykemon..Lets begin the journey")
    player_collect = [default_pykemon]
    running = True

    while running:
        n = random.randrange(0,4)
        enemy = pykemons[n]

        print("On way you encountered with "+enemy.name)
        print("If you wish to fight enter 'yes' or else if you want to run enter 'no'.")
        battle_choice = input().lower()
        if battle_choice == 'yes':
            battle = True
            while battle:
                # Stats of both player & enemy
                print(default_pykemon.name+" has health stats of "+str(default_pykemon.hp)+"/"+str(default_pykemon.maxhp))
                print(enemy.name+" has health stats of "+str(enemy.hp)+"/"+str(enemy.maxhp))

                # Player attacks
                for i in range(0,3):
                    print("_____________________")
                    print(str(i+1),default_pykemon.powers[i].name)
                player_choice = int(input()) - 1
                if player_choice == 0 or player_choice ==1:
                    enemy_damage = default_pykemon.powers[player_choice].atk
                    enemy.take_dmg(enemy_damage)
                    print("The "+default_pykemon.name+" has dealth damage of "+str(enemy_damage)+" to "+enemy.name)
                elif player_choice == 2:
                    player_heal = default_pykemon.powers[player_choice].atk
                    default_pykemon.heal(player_heal)
                    print("The " + default_pykemon.name + " has  healed for " + str(player_heal) + " hp ")


                # Enemy attacks
                print("___________________________")
                enemy_choice = random.randrange(1,4)
                if enemy_choice == 1 or enemy_choice == 2:
                    player_damage = enemy.powers[enemy_choice-1].atk
                    default_pykemon.take_dmg(player_damage)
                    print("The " + enemy.name + " has dealth damage of " + str(player_damage) + " to " + default_pykemon.name)
                elif player_choice == 3:
                    enemy_heal = enemy.powers[enemy_choice-1].atk
                    enemy.heal(enemy_heal)
                    print("The " + enemy.name + " has  healed for " + str(enemy_heal) + " hp ")


                # Checking whether player and enemy had died or alive
                if default_pykemon.hp == 0:
                    print("Enemy has won!")
                    battle = False
                elif enemy.hp == 0:
                    print("Player has won!")
                    battle = False
                else:
                    continue
