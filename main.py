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
    print("You have selected "+default_pykemon.name+" as your first pykemon..Lets begin the journey")