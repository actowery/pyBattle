from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item
import random


#black spells
fire = Spell("Fire", 10, 600, "black")
thunder = Spell("Thunder", 10, 600, "black")
blizzard = Spell("Blizzard", 10, 600, "black")
quake = Spell("Quake", 20, 1200, "black")
meteor = Spell("Meteor", 30, 2050, "black")

#white spells
cure = Spell("Cure", 10, 600, "white")
cura = Spell("Cura", 25, 1500, "white")

#create items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hi_potion = Item("Hi-Potion", "potion", "Heals 150 HP", 150)
super_potion = Item("SuperPotion", "potion", "Heals 250 HP", 250)
elixir = Item("Elixir", "potion", "Heals Max HP/MP to one party member", 9999)
mega_elixir = Item("MegaElixir", "potion", "Heals Max HP/MP to entire party", 9999)

grenade = Item("Grenade", "damage", "Deals 50 HP", 100)

#pc and npc
player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": grenade, "quantity": 10}]

player1 = Person("Valos", 3260, 55, 1000, 34, player_spells, player_items)
player2 = Person("Adert", 4460, 95, 300, 134, player_spells, player_items)
player3 = Person("Robot", 2460, 25, 60, 75, player_spells, player_items)

enemy1 = Person("Whelp ", 130, 560, 350, 55, [], [] )
enemy2 = Person("Dragon", 32000, 755, 315, 25, [], [])
enemy3 = Person("Whelp ", 130, 560, 350, 55, [], [] )
players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]
running = True

print(bcolors.FAIL + bcolors.BOLD +"AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    print("====================")
    print("")
    print("NAME                    HP                                       MP")
    
    for player in players:
        player.get_stats()

    print("\n")
    for enemy in enemies:
        enemy.get_enemy_stats()
    
    for player in players:
        player.choose_action()
        choice = input("Choose action: ")
        index = int(choice) - 1
        
        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)
            enemies[enemy].take_damage(dmg)
            print("You hit " + enemies[enemy].name + " for", dmg)
            
            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + " has been destroyed!")
                del enemies[enemy]
            
        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose a spell or '0' to return: ")) - 1
            
            if magic_choice == -1:
                continue
            
            spell = player.mag[magic_choice]
            magic_dmg = spell.generate_spell_damage()
            if spell.cost > player.get_mp():
                print(bcolors.FAIL + "\nNot enough MP!\n" + bcolors.ENDC)
                continue
            
            player.reduce_mp(spell.cost)        
            if spell.element == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + "You heal for", magic_dmg, "with", spell.name, "!" + bcolors.ENDC)
                
            elif spell.element == "black":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(magic_dmg)

                print(bcolors.OKBLUE + "\n" + "You hit " + enemies[enemy].name + " for", magic_dmg, "with", spell.name, "!" + bcolors.ENDC)
                if enemies[enemy].get_hp == 0:
                    print(enemies[enemy].name + " has been destroyed!")
                    del enemies[enemy]
        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose an Item or '0' to return: ")) - 1
            
            if item_choice == -1:
                continue
            
            item = player.items[item_choice]["item"]
    
            
            if player.items[item_choice]["quantity"] <= 0:
                print(bcolors.FAIL + "\n" + "None left.." + bcolors.ENDC)
                continue
    
            player.items[item_choice]["quantity"] -= 1
            
            if item.category == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\nYou used " + item.name + " and healed ", item.prop, "HP!")
        
            elif item.category == "elixir":
                if item.name == "MegaElixir":
                    for i in players:
                        i.hp = player.maxhp
                        i.mp = player.maxmp
                    else:
                        player.hp = player.maxhp
                        player.mp = player.maxmp

                print(bcolors.OKGREEN + "\nYou used " + item.name + " and HP/MP healed fully!")

            elif item.category == "damage":
                enemy = player.choose_target(enemies)
                enemies[enemy].take_damage(item.prop)

                print(bcolors.FAIL + "\nYou used " + item.name +" on " +enemies[enemy].name + " and dealt", item.prop, "damage!")
                if enemies[enemy].get_hp == 0:
                    print(enemies[enemy].name + " has been destroyed!")
                    del enemies[enemy]
    enemy_choice = 1
    target = random.randrange(0, 3)
    enemy_dmg = enemies[0].generate_damage()
    
    players[target].take_damage(enemy_dmg)
    print("Enemy hits " + players[target].name + " for", enemy_dmg)
    defeated_enemies = 0
    defeated_players = 0
    for enemy in enemies:
        if enemy.get_hp() <= 0: 
            defeated_enemies += 1
    for player in players:
        if player.get_hp() <= 0: 
            defeated_players += 1

    if defeated_enemies == 2:
        print(bcolors.OKGREEN + "YOU WIN!!" + bcolors.ENDC)
        running = False
    elif defeated_players == 2:
        print(bcolors.FAIL + "YOU LOSE..." + bcolors.ENDC)
        running = False