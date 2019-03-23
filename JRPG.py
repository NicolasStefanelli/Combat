import random

class Chracter:
    def __init__(self,name = None,alignment = None,health = 0,speed = 0,phys_defense = 0,mag_defense = 0,attack_low = 0,attack_high = 0,chrs = None):
        """name = str; alignment = bool; health = int; speed = int; phys_defense = int; mag_defense = int"""
        if chrs == None:
            self.name = name
            self.level = 1
            self.xp = 0
            self.alignment = alignment
            self.health = health
            self.speed = speed
            self.pdef = phys_defense
            self.mdef = mag_defense
            self.attack_low = attack_low
            self.attack_high = attack_high
            self.dmg_mod = 0
            self.inventory = []
        else:
            self.name = chrs.name
            self.level = chrs.level
            self.xp = chrs.xp
            self.alignment = chrs.alignment
            self.health = chrs.health
            self.speed = chrs.speed
            self.pdef = chrs.pdef
            self.mdef = chrs.mdef
            self.attack_low = chrs.attack_low
            self.attack_high = chrs.attack_high
            self.dmg_mod = chrs.dmg_mod
            self.inventory = chrs.inventory

    def add_item(self,item):
        self.inventory.append(item)

    def remove_item(self,item):
        self.inventory.remove(item)

    def use_item(self,item):
        if item in self.inventory:
            item.use_item()
    
    def str(self):
        return self.name

class party:
    def __init__(self):
        self.party_list = []

    def add_to_party(self,character):
        self.party_list.append(character)

    def remove_from_party(self,character):
        self.party_list.remove(character)
    def len(self):
        return len(self.party_list)

class item:
    def __init__(self,name,usage_code,dmg_mod = 0,mshield = 0,pshield=0,mp=0,hp=0):
        self.name = name
        self.usage_code = usage_code
        self.dmg_mod = dmg_mod
        self.mshield = mshield
        self.pshield = pshield
        self.mp = mp
        self.hp = hp

    def use_item(self,character,item):
        """ 0 = health; 1 = magic; 2 = dmg; 3 = magic shield; 4 = physical shield"""
        if item.usage_code == 0:
            character.health = character.health + item.hp
        elif item.usage_code == 1:
            character.magic = character.magic + item.mp
        elif item.usage_code == 2:
            character.dmg_mod = character.dmg_mod + item.dmg_mod
        elif item.usage_code == 3:
            pass # add later
        else:
            pass # add later

def Battle(good_guys,bad_guys):
    battle_order = create_battle_order(good_guys,bad_guys)
    flee = False
    while len(good_guys) != 0 and len(bad_guys) != 0 and flee == False:
        for character in battle_order:
            if character.alignment == True:
                choice = input("What do you want to do?")
                if choice == "ATTACK":
                    character_to_attack = input("Who would you like to attack?:")
                    attacked_character = bad_guys[character_to_attack]
                    damage_dealt = attack_damage(character.attack_low,character.attack_high) + character.dmg_mod
                    attacked_character.health = attacked_character.health - damage_dealt
                    if attacked_character.health == 0 or attacked_character < 0:
                        bad_guys.remove_from_party(attacked_character)
                        print("%s died!" % (str(attacked_character)))
                elif choice == "BUFF":
                    buff_selected = input("Which buff would you like to use?:")
                    buff_use(character,buff_selected)
                elif choice == "FLEE":
                    flee = True
            else:
                choice = random.randint(1,3)
                


                    
                    









