init python:

    import math
    import os
    import copy

    # LOGIC

    class Equipment():
        def __init__(self,name,type,level,special,str,dmg,vit,tec,agi,lck,weak,resist,value,lore):
            self.name = name
            self.type = type
            self.level = level
            self.special = special
            self.str = str
            self.dmg = dmg
            self.tec = tec
            self.vit = vit
            self.agi = agi
            self.lck = lck
            self.weak = weak
            self.resist = resist
            self.value = value
            self.lore = lore

    class Consumable():
        def __init__(self, name, type, lore, value):
            self.name = name
            self.type = type
            self.lore = lore
            self.value = value

    # Equip types: Armor, Weapon, Accessory

    armor1 = Equipment("Cloth Armor","Armor",1,None,str=0,dmg=0,tec=0,vit=1,agi=1,lck=0,weak=None,resist=None,value=20,
                    lore="Simple armor that provides minimal protection to wearer, but allows good freedom of movement.")
    armor2 = Equipment("Chain Mail","Armor",1,None,str=0,dmg=0,tec=0,vit=2,agi=0,lck=0,weak=None,resist=None,value=80,
                    lore="Simple armor that offers decent protection, but too heavy for the untrained to wear.")
    armor3 = Equipment("Conjurer Robe","Armor",1,None,str=0,dmg=0,tec=1,vit=2,agi=1,lck=0,weak=None,resist=None,value=200,
                    lore="Robes that doesn't restrict movement and eases the use of techniques.")
    armor4 = Equipment("Breastplate","Armor",1,None,str=0,dmg=0,tec=0,vit=5,agi=0,lck=0,weak=None,resist=None,value=300,
                    lore="Protective armor that lessens the impact of stronger blows to vital areas.")
                
    weapon1 = Equipment("Simple Blade","Weapon",1,None,str=1,dmg=0,tec=0,vit=0,agi=0,lck=0,weak=None,resist=None,value=10,
                        lore="Simple weapon that offers basic means of offense and wieldy enough for anyone to use.")
    weapon2 = Equipment("Sturdy Branch","Weapon",1,None,str=0,dmg=0,tec=1,vit=0,agi=0,lck=0,weak=None,resist=None,value=20,
                        lore="An ordinary tree branch inscribed with runes to facilitate the use of techniques in combat.")
    weapon3 = Equipment("Sharpened Blade","Weapon",1,None,str=3,dmg=1,tec=0,vit=0,agi=0,lck=0,weak=None,resist=None,value=100,
                        lore="A weapon made to inflict grievous wounds and shorten the duration of battles.")
    weapon4 = Equipment("Carved Branch","Weapon",1,None,str=1,dmg=0,tec=3,vit=0,agi=0,lck=0,weak=None,resist=None,value=100,
                        lore="A lenght of wood inscribed with powerful runes.")

    acc1 = Equipment("Round Shield","Accessory",1,None,str=0,dmg=0,tec=0,vit=2,agi=0,lck=0,weak=None,resist=None,value=50,
                        lore="A large pot lid repurposed into a shield. Not the sturdiest, but can still deflect some blows.")
    acc2 = Equipment("Grimoire","Accessory",1,None,str=0,dmg=0,tec=2,vit=0,agi=0,lck=0,weak=None,resist=None,value=80,
                        lore="A thick leather-bound book with many incantations written down.")
    acc3 = Equipment("Slick Boots","Accessory",1,None,str=0,dmg=0,tec=0,vit=0,agi=2,lck=0,weak=None,resist=None,value=50,
                        lore="This footwear improves grip in most wild terrain, allowing the user to move more precisely.")
    acc4 = Equipment("Gauntlets","Accessory",1,None,str=1,dmg=0,tec=0,vit=1,agi=0,lck=0,weak=None,resist=None,value=80,
                        lore="Reinforced gloves that improves the grip of weapons and helps wielding them in combat.")

    chr1 = Equipment("Focus Ring","Charm",1,None,str=0,dmg=0,tec=2,vit=0,agi=0,lck=0,weak=None,resist=None,value=100,
                        lore="A ring inscribed with runes that assists the wielder in remembering techniques in combat.")
    chr2 = Equipment("Lucky Charm","Charm",1,None,str=0,dmg=0,tec=0,vit=0,agi=0,lck=2,weak=None,resist=None,value=100,
                        lore="An amulet decorated with symbols of luck, said to work even for non-believers.")
    chr3 = Equipment("Fire Ring","Charm",1,None,str=0,dmg=1,tec=0,vit=0,agi=0,lck=0,weak=None,resist=["fire"],value=100,
                        lore="A charred and blackened ring that increases the user's protection to fire and strenghtens them.")
    chr4 = Equipment("Amulet of Power","Charm",1,None,str=2,dmg=1,tec=2,vit=2,agi=2,lck=2,weak=None,resist=None,value=800,
                        lore="An amulet imbued with mighty power that strengthens the user. Incredibly Valuable.")

    item1 = Consumable("Healing Draught D","Healing","Heals 50 HP",20)
    item11 = Consumable("Healing Draught C","Healing","Heals 100 HP",30)
    item12 = Consumable("Healing Draught B","Healing","Heals 200 HP",50)
    item2 = Consumable("Invigorating Tonic D","Healing","Recovers 15 TP",50)
    item21 = Consumable("Invigorating Tonic C","Healing","Recovers 30 TP",100)
    item22 = Consumable("Invigorating Tonic B","Healing","Recovers 60 TP",200)
    item3 = Consumable("Charged Memento","Reviving","Revives with 25% HP", 80)
    item4 = Consumable("Rations","Rest","Eating these in a safe place will recover half HP and TP to the party.", 50)
    item5 = Consumable("Urn of Ret","Return","Breaking this urn releases the magical powder that returns the party to town.", 100)

    # SHOP STOCK
    shop_stock = [
        armor1, armor2, armor3, armor4,
        weapon1,weapon2,weapon3, weapon4,
        acc1, acc2, acc3, acc4,
        chr1,chr2,chr3,chr4,
        item1,item11, item12, item2, item21, item22,item3,item4,item5]

    # EQUIPMENT
    inventory = [armor1, armor2, weapon1, weapon2]
    inventorylimt = 20

    # CONSUMABLES
    consumables = [item1, item2, item3, item4, item5]
    consumableslimit = 20



# RENPY FUNCTIONS

    def useItem(item, char):
        global testing_equip
        global useitem_returnmessage
        global ipower
        global exploring
        global checkExploring
        global selected_item

        if item.type == "Healing":
            iname, ipower, ieffect = item.lore.split()
            ipower = int(ipower)
            
            if ieffect == "HP":

                if char.hp <= 0:
                    useitem_returnmessage = "Can't be used on dead character."
                    logText("Can't be used on dead character.")
                    return

                char.hp += ipower
                if char.hp > char.maxhp:
                    char.hp = char.maxhp
                consumables.remove(item)
                useitem_returnmessage = f"[selected_character.name] recovered [ipower] HP."
                logText(f"{char.name} recovered {ipower} HP.")
                if in_combat:
                    selected_item = True

                return True

            elif ieffect == "TP":
                
                char.tp += ipower
                if char.tp > char.maxtp:
                    char.tp = char.maxtp
                consumables.remove(item)
                useitem_returnmessage = (f"[selected_character.name] recovered [ipower] TP.")
                logText(f"{char.name} recovered {ipower} TP.")
                if in_combat:
                    selected_item = True
                return True

        if item.type == "Reviving":
            ieffect, i1, ipower, i2 = item.lore.split()

            if char.hp > 0:
                useitem_returnmessage = "Can't be used on a living character."
                logText("Can't be used on a living character.")

                return

            if ipower == "50%":
                char.hp += round(char.maxhp//2)
            elif ipower == "25%":
                char.hp += round(char.maxhp//4)

            consumables.remove(item)
            useitem_returnmessage = f"[selected_character.name] was revived with [ipower] HP."
            logText(f"{char.name} was revived with {ipower} HP.")
            if in_combat:
                    selected_item = True
            return True

        if item.type == "Rest":
            
            if exploring == True:
                if restAreaCheck() == True:
                    for char in party:
                        if char.hp > 0:
                            char.hp += int(char.maxhp * 0.25)
                            if char.hp > char.maxhp:
                                char.hp = char.maxhp
                            char.tp += int(char.maxtp * 0.25)
                            if char.tp > char.maxtp:
                                char.tp = char.maxtp

                    checkHour(1)

                    useitem_returnmessage = ("Time has passed and party has restored some HP and TP.")
                    consumables.remove(item)
                    return True
                else:
                    useitem_returnmessage = ("Can't use this outside of a safe area.")
                    return False
            else:
                useitem_returnmessage = ("Can't use this while in town.")
            pass

        if item.type == "Return":
            if exploring == True:

                useitem_returnmessage = "Returning to town."
                consumables.remove(item)
                # testing_equip = False
                # checkExploring(False)
                # runTown()
                exploring = False
                renpy.hide_screen("dungeon_danger")
                renpy.hide_screen("dungeon_explore")
                renpy.jump("town_scene")

            else:
                useitem_returnmessage = "You can only use this item while exploring."

    def changeEquip(item, char):
        item_rem = None

        if item == "Weapon":
            slot = "Weapon"
            item = None
        elif item == "Armor":
            slot = "Armor"
            item = None
        elif item == "Accessory":
            slot = "Accessory"
            item = None
        elif item == "Charm":
            slot = "Charm"
            item = None
        else:
            slot = item.type

        if item == None:
            if char.equip[slot] == None:
                pass
            else:
                item_rem = char.equip[slot]

                char.str -= item_rem.str
                char.dmg -= item_rem.dmg
                char.tec -= item_rem.tec
                char.vit -= item_rem.vit
                char.agi -= item_rem.agi
                char.lck -= item_rem.lck
                if item_rem.weak is not None:
                    for n in item_rem.weak:
                        if n in char.weak:
                            char.weak.remove(n)
                if item_rem.resist is not None:
                    for n in item_rem.resist:
                        if n in char.resist:
                            char.resist.remove(n)
                # Remove item
                inventory.append(char.equip[slot])
                char.equip[slot] = None

        else:
            if char.equip[slot] == None:
                char.str += item.str
                char.dmg += item.dmg
                char.tec += item.tec
                char.vit += item.vit
                char.agi += item.agi
                char.lck += item.lck
                if item.weak is not None:
                    for n in item.weak:
                        char.weak.append(n)
                if item.resist is not None:
                    for n in item.resist:
                        char.resist.append(n)

                char.equip[slot] = item
                inventory.remove(item)

            else:
                item_rem = char.equip[slot]

                char.str -= item_rem.str
                char.dmg -= item_rem.dmg
                char.tec -= item_rem.tec
                char.vit -= item_rem.vit
                char.agi -= item_rem.agi
                char.lck -= item_rem.lck
                if item_rem.weak is not None:
                    for n in item_rem.weak:
                        if n in char.weak:
                            char.weak.remove(n)
                if item_rem.resist is not None:
                    for n in item_rem.resist:
                        if n in char.resist:
                            char.resist.remove(n)
                # Remove item
                inventory.append(char.equip[slot])

                # Equip new item
                char.str += item.str
                char.dmg += item.dmg
                char.tec += item.tec
                char.vit += item.vit
                char.agi += item.agi
                char.lck += item.lck
                if item.weak is not None:
                    for n in item.weak:
                        char.weak.append(n)
                if item.resist is not None:
                    for n in item.resist:
                        char.resist.append(n)

                char.equip[slot] = item
                inventory.remove(item)


        fetchEquip(slot)
        pass

    def fetchEquip(type):
        global equiplist
        equiplist = []

        if type == "Weapon":
        
            equiplist = []
            for n in inventory:
                if n.type == "Weapon":
                    equiplist.append(n)

        
        elif type == "Armor":

            equiplist = []
            for n in inventory:
                if n.type == "Armor":
                    equiplist.append(n)

        elif type == "Accessory":

            equiplist = []
            for n in inventory:
                if n.type == "Accessory":
                    equiplist.append(n)

        elif type == "Charm":

            equiplist = []
            for n in inventory:
                if n.type == "Charm":
                    equiplist.append(n)

        return equiplist

# RENPY DEFAULTS

# SHOP STOCK
default shop_stock = [
        armor1, armor2, armor3, armor4,
        weapon1,weapon2,weapon3, weapon4,
        acc1, acc2, acc3, acc4,
        chr1,chr2,chr3,chr4,
        item1,item11, item12, item2, item21, item22,item3,item4,item5]

# EQUIPMENT
default inventory = []
default inventorylimt = 20

# CONSUMABLES
default consumables = []
default consumableslimit = 20