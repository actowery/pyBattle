from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item


#black spells
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
quake = Spell("Quake", 20, 200, "black")
meteor = Spell("Meteor", 12, 150, "black")

#white spells
cure = Spell("Cure", 10, 100, "white")
cura = Spell("Cura", 20, 200, "white")

#create items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hi_potion = Item("Hi-Potion", "potion", "Heals 150 HP", 150)
super_potion = Item("Super Potion", "potion", "Heals 250 HP", 250)
elixir = Item("Elixir", "potion", "Heals Max HP/MP to one party member", 9999)
mega_elixir = Item("Mega Elixir", "potion", "Heals Max HP/MP to entire party", 9999)

grenade = Item("Grenade", "damage", "Deals 50 HP", 100)

#pc and npc
player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 15}, {"item": grenade, "quantity": 10}]

player1 = Person("Valos", 3260, 65, 60, 34, player_spells, player_items)
player2 = Person("Adert", 4460, 65, 60, 34, player_spells, player_items)
player3 = Person("Robot", 2460, 65, 60, 34, player_spells, player_items)
enemy = Person("Dragon", 3200, 65, 45, 25, [], [])

players = [player1, player2, player3]

running = True

print(bcolors.FAIL + bcolors.BOLD +"AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    print("====================")
    print("\n\n")
    print("NAME                    HP                                       MP")
    
    for player in players:
        player.get_stats()

    print("\n")
    
    for player in players:
        player.choose_action()
        choice = input("Choose action: ")
        index = int(choice) - 1
        
        if index == 0:
            dmg = player.generate_damage()
            enemy.take_damage(dmg)
            print("You hit for", dmg)
            
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
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + "You hit for", magic_dmg, "with", spell.name, "!" + bcolors.ENDC)
        
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
                player.hp = player.maxhp
                player.mp = player.maxmp
                print(bcolors.OKGREEN + "\nYou used " + item.name + " and HP/MP healed fully!")
            elif item.category == "damage":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\nYou used " + item.name + " and dealt", item.prop, "damage!")
            
    enemy_choice = 1
    
    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy hits for", enemy_dmg)
    
    print("====================")
    print("Enemy is at ", bcolors.FAIL + str(int(((enemy.get_hp() / enemy.get_max_hp())*100))) + "%" + bcolors.ENDC + "\n")
    print("You are at ", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + "hp" + bcolors.ENDC)
    print("You are at ", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + "mp" + bcolors.ENDC)
    
    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "YOU WIN!!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "YOU LOSE..." + bcolors.ENDC)
        running = False