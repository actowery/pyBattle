from classes.game import Person, bcolors
from classes.magic import Spell

#black spells
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
quake = Spell("Quake", 20, 200, "black")
meteor = Spell("Meteor", 12, 150, "black")

#white spells
cure = Spell("Cure", 10, 100, "white")
cura = Spell("Cura", 20, 200, "white")


#pc and npc         
player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

running = True

print(bcolors.FAIL + bcolors.BOLD +"AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    print("====================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1
    
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You hit for", dmg)
        
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose spell: ")) - 1
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