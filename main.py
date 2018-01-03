from classes.game import Person, bcolors


magic = [{"name": "Fire", "cost": 10, "dmg": 130},
         {"name": "Thunder", "cost": 10, "dmg": 190},
         {"name": "Blizzard", "cost": 10, "dmg": 160}]
         
player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

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
        magic_dmg = player.generate_spell_damage(magic_choice)
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_cost(magic_choice)
        
        if cost > player.get_mp():
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue
        
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + "You hit for", magic_dmg, "with", spell, "!" + bcolors.ENDC)
    
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