init python:

# RENPY Commands

    def tavernRest():
        global hour

        price = 0
        for n in party:
            price += n.level * 10
        price = int(price / len (party))

        global party_money
        if party_money >= price:
            party_money -= price
            for n in party:
                n.hp = n.maxhp
                n.tp = n.maxtp
            hour += 2

            if hour == 8:
                hour = 0
            elif hour == 9:
                hour = 1
            elif hour == 10:
                hour = 2

            return True
        else:
            return False

    def buyItem(item, type):
        global party_money
        global consumables
        global inventory

        if type == "Equip":
            inventory.append(item)
        elif type == "Consumable":
            consumables.append(item)
        party_money -= item.value

    def buyItemMerch(item, type):
        global party_money
        global consumables
        global inventory

        if type == "Equip":
            inventory.append(item)
        elif type == "Consumable":
            consumables.append(item)
        party_money -= item.value*5

    def sellItem(item, type):
        global party_money
        global consumables
        global inventory

        if type == "Equip":
            inventory.remove(item)
        elif type == "Consumable":
            consumables.remove(item)
        party_money += item.value//2

##