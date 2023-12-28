init python:
    logtext = []
    logtextprint = ""
    textcounter = 0
    def logText(text):
        global logtext
        global logtextprint

        logtext.append(text)
        
        if len(logtext) > 30:
            logtext.pop(0)

        logtextprint = f"\n".join(logtext)

        # renpy.get_displayable("dungeon_command", "dglog").scroll = 1

    # Code for Auto-scroll in Log screens
    yadjValue = float("inf")
    yadj = ui.adjustment()

    mapplacement = ""
    

    def blankNewMap():
        # global newdungeon
        blankdungeon = []

        for ny in range(32):
            blankdungeon.append([])
            for nx in range(32):
                blankdungeon[ny].append(1)
            
        return blankdungeon

    def toggleMapTileOLD(tiley, tilex):
        global newdungeon

        if newdungeon[tiley][tilex] != 0:
            newdungeon[tiley][tilex] = 0
        elif newdungeon[tiley][tilex] != 1:
            newdungeon[tiley][tilex] = 1

    def toggleMapTileAlt(tiley, tilex):
        global newdungeon

        if newdungeon[tiley][tilex] != 2:
            newdungeon[tiley][tilex] = 2
        elif newdungeon[tiley][tilex] != C:
            newdungeon[tiley][tilex] = C

    def toggleMapTile(tiley, tilex):
        global newdungeon

        if mapplacement == "Wall":
            newdungeon[tiley][tilex] = 1
        elif mapplacement == "Floor":
            newdungeon[tiley][tilex] = 0
        elif mapplacement == "Door":
            newdungeon[tiley][tilex] = 2
        
        elif mapplacement == "Secret Passage E > W":
            newdungeon[tiley][tilex] = E
        elif mapplacement == "Secret Passage W > E":
            newdungeon[tiley][tilex] = W
        elif mapplacement == "Secret Passage N > S":
            newdungeon[tiley][tilex] = N
        elif mapplacement == "Secret Passage S > N":
            newdungeon[tiley][tilex] = S

        elif mapplacement == "Secret Passage":
            newdungeon[tiley][tilex] = 9
        elif mapplacement == "Secret Passage NS":
            newdungeon[tiley][tilex] = 8
        elif mapplacement == "Stairs Up":
            newdungeon[tiley][tilex] = U
        elif mapplacement == "Stairs Down":
            newdungeon[tiley][tilex] = D

        elif mapplacement == "Chest":
            newdungeon[tiley][tilex] = C
        elif mapplacement == "Merchant":
            newdungeon[tiley][tilex] = M

    def copyMap():
            import pygame.scrap
            import json
            dungeon_str = json.dumps(newdungeon)

            dungeon_bytes = dungeon_str.encode('utf-8')

            pygame.scrap.put(pygame.SCRAP_TEXT, dungeon_bytes)
            renpy.notify(_("Copied the dungeon to the clipboard."))

default playermapzoom = 0.4
default newdungeon = blankNewMap()

screen party:
    zorder 0

    frame:
        xpadding 15
        ypadding 15
        yalign 1.00
        xalign 1.00
        # xfill True
        xsize 1420
        ysize 300
        background None

        hbox:
            xalign 0.5
            yalign 0.4
            spacing 20
            for n in party:
                if n.char_class != "Decoy":
                    frame: #Char 1
                        ypadding 20
                        xpadding 20
                        xsize 300
                        if charinit == n:
                            background "#224"
                        
                        if n.hp <= 0:
                            background "#822"
                        vbox:
                            ymaximum 150
                            spacing 10
                            text "[n.name]":
                                outlines [(3, "#333", 2, 2)]
                                size 30
                            fixed:
                                bar value AnimatedValue(value=n.hp, range=n.maxhp, delay=0.3) xsize 260 ysize 38
                                text f"{int(n.hp)} / {int(n.maxhp)}" size 30 ypos -2 xalign 0.5 outlines [(2, "#333", 1, 1)]
                            fixed:
                                ypos -50
                                bar value AnimatedValue(value=n.tp, range=n.maxtp, delay=0.3) xsize 260 left_bar "#ff0" right_bar "#440" ysize 38
                                text f"{int(n.tp)} / {int(n.maxtp)}" size 30 ypos -2 xalign 0.5 outlines [(2, "#333", 1, 1)]
                            fixed:
                                hbox:
                                    spacing -5
                                    for effect in n.effects:
                                        transform:
                                            rotate -30
                                            xanchor 0.5 yanchor 0.5
                                            text effect.title() + f" {n.effects[effect][1]}":
                                                size 20 outlines [(2, "#333", 1, 1)]


        hbox:
            xalign 0.5
            ypos -100
            spacing 20
            for n in party:
                if n.char_class == "Decoy":
                    frame: #Decoys
                        ypadding 20
                        xpadding 20
                        xsize 300
                        ysize 120
                        vbox:
                            ymaximum 150
                            spacing 10
                            text "[n.name]":
                                outlines [(3, "#333", 2, 2)] size 30
                            fixed:
                                bar value AnimatedValue(value=n.hp, range=n.maxhp, delay=0.3) xsize 260 ysize 30
                                text "[n.hp] / [n.maxhp]" ypos -2 xalign 0.5 outlines [(2, "#333", 1, 1)] size 25

screen time:
    zorder 0
    frame:
        xpadding 25
        ypadding 25
        yalign 0.0
        xalign 1.0
        xsize 400
        background None

        grid 1 3:
            xalign 0.5
            yalign 0.5
            text "Time:":
                xalign 0.5
                size 40
                outlines [(4, "#333", 2, 2)]
            text f"{str(hour).zfill(2)} : {str(steps * 2).zfill(2)}":
                xalign 0.5
                size 40
                outlines [(4, "#333", 2, 2)]
            text hour_name:
                size 40
                if hour >= 3 and hour <= 5:
                    color "#000" outlines [(4, "#0C0", 2, 2)]
                elif hour >= 18 or hour <= 2:
                    color "#00F" outlines [(4, "#FFF", 2, 2)]
                else:
                    color "#FFF" outlines [(4, "#333", 2, 2)]

screen town:
    zorder 1
    tag menus
    frame:
        xpadding 15
        ypadding 15
        yalign 0.00
        xalign 0.00
        yfill True
        # ysize 800
        xsize 500

        text "Welcome to" yalign 0.05 xalign 0.5 size 40
        text "HUNDWICK" yalign 0.1 xalign 0.5 size 70

        vbox:
            
            ypos 0.25
            spacing 25
            frame:
                xfill True
                ypadding 10
                textbutton "Party":
                    text_size 50
                    xalign 0.5
                    yalign 0.5
                    action Call("party_menu_scene")

            frame:
                xfill True    
                ypadding 10
                textbutton "Tavern":
                    text_size 50
                    xalign 0.5
                    yalign 0.5
                    action Jump("tavern_scene")

            frame:
                xfill True    
                ypadding 10
                textbutton "Trainer":
                    text_size 50
                    xalign 0.5
                    yalign 0.5
                    action Jump("trainer_scene")

            frame:
                xfill True    
                ypadding 10
                textbutton "Shop":
                    text_size 50
                    xalign 0.5
                    yalign 0.5
                    action Jump("shop_scene")

            frame:
                xfill True    
                ypadding 10
                textbutton "Dungeon":
                    text_size 50
                    xalign 0.5
                    yalign 0.5
                    action Jump("dungeon_label")

            # frame:
            #     xfill True    
            #     ypadding 10
            #     textbutton "Combat":
            #         text_size 50
            #         xalign 0.5
            #         yalign 0.5
            #         action Call("combat_label")
                
            # frame:
            #     xfill True    
            #     ypadding 10
            #     textbutton "Comb Res":
            #         text_size 50
            #         xalign 0.5
            #         yalign 0.5
            #         action Call("combresults")

            # frame:
            #     xfill True    
            #     ypadding 10
            #     textbutton "EXP+":
            #         text_size 50
            #         xalign 0.5
            #         yalign 0.5
            #         action Call("levelup_label")

            # null height 50
            # frame:
            #     xfill True    
            #     ypadding 10
            #     textbutton "Map Maker":
            #         text_size 50
            #         xalign 0.5
            #         yalign 0.5
            #         action Call("mapmaker_label")

screen tavern:
    zorder 1
    tag menus
    frame:
        xpadding 15
        ypadding 15
        yalign 0.00
        xalign 0.00
        yfill True
        # ysize 800
        xsize 500

        text "ONTAM's" yalign 0.05 xalign 0.5 size 40
        text "Tavern & Inn" yalign 0.1 xalign 0.5 size 70

        showif tavern_command == None:
            vbox: # TAVERN options
                
                ypos 0.25
                spacing 25
                frame:
                    xfill True
                    ypadding 10
                    textbutton "Party":
                        text_size 50
                        xalign 0.5
                        yalign 0.5
                        action Call("party_menu_scene")

                frame:
                    xfill True    
                    ypadding 10
                    textbutton "Rest":
                        text_size 50
                        xalign 0.5
                        yalign 0.5
                        action SetVariable("tavern_command", "Rest")

                frame:
                    xfill True    
                    ypadding 10
                    textbutton "Quests":
                        text_size 50
                        xalign 0.5
                        yalign 0.5
                        # action NullAction()

                frame:
                    xfill True    
                    ypadding 10
                    textbutton "Talk":
                        text_size 50
                        xalign 0.5
                        yalign 0.5
                        # action NullAction()

                frame:
                    xfill True    
                    ypadding 10
                    textbutton "Return":
                        text_size 50
                        xalign 0.5
                        yalign 0.5
                        action Jump("town_scene")

        showif tavern_command == "Rest":
            python:
                price = 0
                for n in party:
                    price += n.level * 10
                price = int(price / len (party))
            
            vbox:
                ypos 0.25
                spacing 25
                xsize 440
                xpos 20

                text f"Accomodations for your group will cost {price} Cr.\n\nRest for 8 hours?" size 30

                null height 50
                text "Party Funds: " + str(party_money) size 30
                frame:
                    xfill True    
                    ypadding 10
                    textbutton "Yes":
                        text_size 50
                        xalign 0.5
                        yalign 0.5
                        action Jump("tavern_scene.rest")

                frame:
                    xfill True    
                    ypadding 10
                    textbutton "No":
                        text_size 50
                        xalign 0.5
                        yalign 0.5
                        action SetVariable("tavern_command", None)


screen shop:
    zorder 1
    tag menus
    frame:
        xpadding 15
        ypadding 15
        yalign 0.00
        xalign 0.00
        yfill True
        # ysize 800
        xsize 500

        text "SYLAS'" yalign 0.05 xalign 0.5 size 40
        text "Shop" yalign 0.1 xalign 0.5 size 70

        vbox:
            
            ypos 0.25
            spacing 25
            frame:
                xfill True
                ypadding 10
                textbutton "Party":
                    text_size 50
                    xalign 0.5
                    yalign 0.5
                    action Call("party_menu_scene")

            frame:
                xfill True    
                ypadding 10
                textbutton "Buy":
                    text_size 50
                    xalign 0.5
                    yalign 0.5
                    action SetVariable("shop_command", "Buy") 

            frame:
                xfill True    
                ypadding 10
                textbutton "Sell":
                    text_size 50
                    xalign 0.5
                    yalign 0.5
                    action SetVariable("shop_command", "Sell") 

            frame:
                xfill True    
                ypadding 10
                textbutton "Talk":
                    text_size 50
                    xalign 0.5
                    yalign 0.5
                    # action NullAction()

            frame:
                xfill True    
                ypadding 10
                textbutton "Return":
                    text_size 50
                    xalign 0.5
                    yalign 0.5
                    action Jump("town_scene")

    showif shop_command == "Buy":
        frame:
            # xsize 1420
            xsize 1350
            xpos 535
            ysize 800
            # xpos 485
            yalign 0.05
            hbox:
                vbox:
                    spacing 10
                    xalign 0.5
                    xsize 250
                    xoffset 30

                    null height 20

                    text "BUY" bold True size 30
                    text "Buying what?" size 25
                    
                    null height 100
                    frame:
                        xfill True
                        textbutton "Consumables" action SetVariable("shop_type", "Consumables") text_size 30
                    
                    frame:
                        xfill True
                        textbutton "Weapon" action SetVariable("shop_type", "Weapon") text_size 30

                    frame:
                        xfill True
                        textbutton "Armor" action SetVariable("shop_type", "Armor") text_size 30
                    
                    frame:
                        xfill True
                        textbutton "Accessory" action SetVariable("shop_type", "Accessory") text_size 30

                    frame:
                        xfill True
                        textbutton "Charm" action SetVariable("shop_type", "Charm") text_size 30

                    null height 50
                    text "Inventory: " + str(len(inventory)) + f" / {inventorylimt}" size 20
                    text "Consumables: " + str(len(consumables)) + f" / {consumableslimit}" size 20
                    text "Funds: " + str(party_money) + " Cr" size 25
                            
                frame:
                    xsize 1000
                    ysize 750
                    xoffset 50
                    ypos 30

                    viewport id "shopbuy":
                        mousewheel True

                        vbox:
                            null height 20
                            for item in shop_stock:
                                if item.type == shop_type:
                                    fixed:
                                        ysize 100
                                        text item.name xpos 20 size 25 xsize 200
                                        text item.lore xpos 220 size 20 xsize 580
                                        # text str(item.value) xpos 850 size 25
                                        frame:
                                            xpos 820 
                                            textbutton f"Buy {item.value} Cr" text_size 25:
                                                if party_money >= item.value and len(inventory) < inventorylimt:
                                                    action Function(buyItem,item,"Equip")
                                        if item.type == "Weapon":
                                            text "STR: " + str(item.str) size 25 xpos 220 ypos 60
                                            text "DMG: " + str(item.dmg) size 25 xpos 320 ypos 60
                                            text "TEC: " + str(item.tec) size 25 xpos 420 ypos 60
                                        if item.type == "Armor":
                                            text "VIT: " + str(item.vit) size 25 xpos 220 ypos 60
                                            text "AGI: " + str(item.agi) size 25 xpos 320 ypos 60
                                            text "LCK: " + str(item.lck) size 25 xpos 420 ypos 60
                                        if item.type == "Accessory" or item.type == "Charm":
                                            text "STR: " + str(item.str) size 25 xpos 220 ypos 60
                                            text "DMG: " + str(item.dmg) size 25 xpos 320 ypos 60
                                            text "TEC: " + str(item.tec) size 25 xpos 420 ypos 60
                                            text "VIT: " + str(item.vit) size 25 xpos 520 ypos 60
                                            text "AGI: " + str(item.agi) size 25 xpos 620 ypos 60
                                            text "LCK: " + str(item.lck) size 25 xpos 720 ypos 60
                                            if item.resist != None:
                                                text "RES.: " + " ".join(item.resist).title() size 25 xpos 820 ypos 60

                                if shop_type == "Consumables":
                                    if item.type not in ("Weapon","Armor","Accessory","Charm"):
                                        fixed:
                                            ysize 80
                                            text item.name xpos 20 size 25 xsize 200
                                            text item.lore xpos 220 size 20 xsize 580
                                            # text str(item.value) xpos 850 size 25
                                            frame:
                                                xpos 820 
                                                textbutton f"Buy {item.value} Cr" text_size 25:
                                                    if party_money >= item.value and len(consumables) < consumableslimit:
                                                        action Function(buyItem,item,"Consumable")
                    vbar value YScrollValue("shopbuy") xalign 1.0 xoffset 30


    showif shop_command == "Sell":
        frame:
            # xsize 1420
            xsize 1350
            xpos 535
            ysize 800
            # xpos 485
            yalign 0.05
            hbox:
                vbox:
                    spacing 10
                    xalign 0.5
                    xsize 250
                    xoffset 30

                    null height 20

                    text "SELL" bold True size 30
                    text "Sell what?" size 25
                    
                    null height 100
                    frame:
                        xfill True
                        textbutton "Consumables" action SetVariable("shop_type", "Consumables") text_size 30
                    
                    frame:
                        xfill True
                        textbutton "Weapon" action SetVariable("shop_type", "Weapon") text_size 30

                    frame:
                        xfill True
                        textbutton "Armor" action SetVariable("shop_type", "Armor") text_size 30
                    
                    frame:
                        xfill True
                        textbutton "Accessory" action SetVariable("shop_type", "Accessory") text_size 30

                    frame:
                        xfill True
                        textbutton "Charm" action SetVariable("shop_type", "Charm") text_size 30

                    null height 50
                    text "Inventory: " + str(len(inventory)) + f" / {inventorylimt}" size 20
                    text "Consumables: " + str(len(consumables)) + f" / {consumableslimit}" size 20
                    text "Funds: " + str(party_money) + " Cr" size 25
                            
                frame:
                    xsize 1000
                    ysize 750
                    xoffset 50
                    ypos 30

                    viewport id "shopsell":
                        mousewheel True

                        vbox:
                            null height 20
                            for item in inventory:
                                if item.type == shop_type:
                                    fixed:
                                        ysize 100
                                        text item.name xpos 20 size 25 xsize 200
                                        text item.lore xpos 220 size 20 xsize 580
                                        # text str(item.value) xpos 850 size 25
                                        frame:
                                            xpos 820 
                                            textbutton f"Sell {item.value//2} Cr" text_size 25:
                                                action Function(sellItem,item,"Equip")
                                        if item.type == "Weapon":
                                            text "STR: " + str(item.str) size 25 xpos 220 ypos 60
                                            text "DMG: " + str(item.dmg) size 25 xpos 320 ypos 60
                                            text "TEC: " + str(item.tec) size 25 xpos 420 ypos 60
                                        if item.type == "Armor":
                                            text "VIT: " + str(item.vit) size 25 xpos 220 ypos 60
                                            text "AGI: " + str(item.agi) size 25 xpos 320 ypos 60
                                            text "LCK: " + str(item.lck) size 25 xpos 420 ypos 60
                                        if item.type == "Accessory" or item.type == "Charm":
                                            text "STR: " + str(item.str) size 25 xpos 220 ypos 60
                                            text "DMG: " + str(item.dmg) size 25 xpos 320 ypos 60
                                            text "TEC: " + str(item.tec) size 25 xpos 420 ypos 60
                                            text "VIT: " + str(item.vit) size 25 xpos 520 ypos 60
                                            text "AGI: " + str(item.agi) size 25 xpos 620 ypos 60
                                            text "LCK: " + str(item.lck) size 25 xpos 720 ypos 60
                                            if item.resist != None:
                                                text "RES.: " + " ".join(item.resist).title() size 25 xpos 820 ypos 60
                            for item in consumables:
                                if shop_type == "Consumables":
                                    if item.type not in ("Weapon","Armor","Accessory","Charm"):
                                        fixed:
                                            ysize 80
                                            text item.name xpos 20 size 25 xsize 200
                                            text item.lore xpos 220 size 20 xsize 580
                                            # text str(item.value) xpos 850 size 25
                                            frame:
                                                xpos 820 
                                                textbutton f"Sell {item.value//2} Cr" text_size 25:
                                                    action Function(sellItem,item,"Consumable")
                    vbar value YScrollValue("shopsell") xalign 1.0 xoffset 30

screen merchant:
    zorder 1
    tag menus
    frame:
        xpadding 15
        ypadding 15
        yalign 0.00
        xalign 0.00
        yfill True
        # ysize 800
        xsize 500

        text "MERCHANT's" yalign 0.05 xalign 0.5 size 40
        text "Wares" yalign 0.1 xalign 0.5 size 70

        vbox:
            
            ypos 0.25
            spacing 25
            frame:
                xfill True
                ypadding 10
                textbutton "Party":
                    text_size 50
                    xalign 0.5
                    yalign 0.5
                    action Call("party_menu_scene")

            frame:
                xfill True    
                ypadding 10
                textbutton "Buy":
                    text_size 50
                    xalign 0.5
                    yalign 0.5
                    action SetVariable("shop_command", "Buy") 

            frame:
                xfill True    
                ypadding 10
                textbutton "Sell":
                    text_size 50
                    xalign 0.5
                    yalign 0.5
                    action SetVariable("shop_command", "Sell") 

            frame:
                xfill True    
                ypadding 10
                textbutton "Talk":
                    text_size 50
                    xalign 0.5
                    yalign 0.5
                    # action NullAction()

            frame:
                xfill True    
                ypadding 10
                textbutton "Return":
                    text_size 50
                    xalign 0.5
                    yalign 0.5
                    action Show("dungeon_explore"), Return()

    showif shop_command == "Buy":
        frame:
            # xsize 1420
            xsize 1320
            xpos 535
            ysize 800
            # xpos 485
            yalign 0.05
            hbox:
                vbox:
                    spacing 10
                    xalign 0.5
                    xsize 250
                    xoffset 30

                    null height 20

                    text "BUY" bold True size 30
                    text "Buying what?" size 25
                    
                    null height 100
                    frame:
                        xfill True
                        textbutton "Consumables" action SetVariable("shop_type", "Consumables") text_size 30

                    null height 50
                    text "Inventory: " + str(len(inventory)) + f" / {inventorylimt}" size 20
                    text "Consumables: " + str(len(consumables)) + f" / {consumableslimit}" size 20
                    text "Funds: " + str(party_money) + " Cr" size 25
                            
                frame:
                    xsize 1000
                    ysize 750
                    xoffset 50
                    ypos 30

                    vbox:
                        null height 20
                        for item in shop_stock:
                            if item.type == shop_type:
                                fixed:
                                    ysize 100
                                    text item.name xpos 20 size 25 xsize 200
                                    text item.lore xpos 220 size 20 xsize 580
                                    # text str(item.value) xpos 850 size 25
                                    frame:
                                        xpos 820 
                                        textbutton f"Buy {item.value*5} Cr" text_size 25:
                                            if party_money >= (item.value*5) and len(inventory) < inventorylimt:
                                                action Function(buyItem,item,"Equip")
                                    if item.type == "Weapon":
                                        text "STR: " + str(item.str) size 25 xpos 220 ypos 60
                                        text "DMG: " + str(item.dmg) size 25 xpos 320 ypos 60
                                        text "TEC: " + str(item.tec) size 25 xpos 420 ypos 60
                                    if item.type == "Armor":
                                        text "VIT: " + str(item.vit) size 25 xpos 220 ypos 60
                                        text "AGI: " + str(item.agi) size 25 xpos 320 ypos 60
                                        text "LCK: " + str(item.lck) size 25 xpos 420 ypos 60
                                    if item.type == "Accessory" or item.type == "Charm":
                                        text "STR: " + str(item.str) size 25 xpos 220 ypos 60
                                        text "DMG: " + str(item.dmg) size 25 xpos 320 ypos 60
                                        text "TEC: " + str(item.tec) size 25 xpos 420 ypos 60
                                        text "VIT: " + str(item.vit) size 25 xpos 520 ypos 60
                                        text "AGI: " + str(item.agi) size 25 xpos 620 ypos 60
                                        text "LCK: " + str(item.lck) size 25 xpos 720 ypos 60
                                        if item.resist != None:
                                            text "RES.: " + " ".join(item.resist).title() size 25 xpos 820 ypos 60

                            if shop_type == "Consumables":
                                if item.type not in ("Weapon","Armor","Accessory","Charm"):
                                    fixed:
                                        ysize 80
                                        text item.name xpos 20 size 25 xsize 200
                                        text item.lore xpos 220 size 20 xsize 580
                                        # text str(item.value) xpos 850 size 25
                                        frame:
                                            xpos 820 
                                            textbutton f"Buy {item.value*5} Cr" text_size 25:
                                                if party_money >= item.value*5 and len(consumables) < consumableslimit:
                                                    action Function(buyItemMerch,item,"Consumable")



    showif shop_command == "Sell":
        frame:
            # xsize 1420
            xsize 1320
            xpos 535
            ysize 800
            # xpos 485
            yalign 0.05
            hbox:
                vbox:
                    spacing 10
                    xalign 0.5
                    xsize 250
                    xoffset 30

                    null height 20

                    text "SELL" bold True size 30
                    
                    
                    null height 100

                    null height 50
                    text "Inventory: " + str(len(inventory)) + f" / {inventorylimt}" size 20
                    text "Consumables: " + str(len(consumables)) + f" / {consumableslimit}" size 20
                    text "Funds: " + str(party_money) + " Cr" size 25
                            
                frame:
                    xsize 1000
                    ysize 750
                    xoffset 50
                    ypos 30
                    background None

                    vbox:
                        xsize 800
                        xalign 0.5
                        null height 20
                        text "MERCHANT: Sell? I'm not looking to buy, mate. 'sides, I can just loot yer' corpses when you die in there." size 25


screen trainer:
    zorder 1
    tag menus
    frame: # LEFT MENUS
        xpadding 15
        ypadding 15
        yalign 0.00
        xalign 0.00
        yfill True
        # ysize 800
        xsize 500

        text "CHROMDUR's" yalign 0.05 xalign 0.5 size 40
        text "Arena" yalign 0.1 xalign 0.5 size 70

        showif trainer_command == None: # Main Screen
            vbox:
                ypos 0.25
                spacing 25
                frame:
                    xfill True
                    ypadding 10
                    textbutton "Party":
                        text_size 50
                        xalign 0.5
                        yalign 0.5
                        action Call("party_menu_scene")

                frame:
                    xfill True    
                    ypadding 10
                    textbutton "Recruit":
                        text_size 50
                        xalign 0.5
                        yalign 0.5
                        action SetVariable("trainer_command", "Recruit")

                frame:
                    xfill True    
                    ypadding 10
                    textbutton "Manage":
                        text_size 50
                        xalign 0.5
                        yalign 0.5
                        action SetVariable("trainer_command", "Manage")

                frame:
                    xfill True    
                    ypadding 10
                    textbutton "Talk":
                        text_size 50
                        xalign 0.5
                        yalign 0.5
                        # action NullAction()

            fixed:
                ypos 900
                frame:
                    xfill True    
                    ypadding 10
                    textbutton "Return":
                        text_size 50
                        xalign 0.5
                        yalign 0.5
                        action Jump("town_scene")

        showif trainer_command == "Recruit":

            fixed:
                xpos 20
                xsize 440
                ypos 0.25
                spacing 20
                text "Recruiting a new Vagranteer costs 10 Cr." size 30 ypos 0
                text "As part of the taxes for finding someone who fits your specific needs." size 25 ypos 100
                text "They also bring their own equipment, which while shody and cheap, still has a cost." size 20 ypos 200
                text "Furthermore, we're doing all the job for you, 10 Crowns is a more than fair price." size 15 ypos 300

                null height 200
                
                text "Party funds: " + str(party_money) ypos 850
            
            fixed:
                ypos 900
                frame:
                    xfill True    
                    ypadding 10
                    textbutton "Return":
                        text_size 50
                        xalign 0.5
                        yalign 0.5
                        action SetVariable("trainer_command", None), SetVariable("newchar_name", ""), SetVariable("newchar_race", None), SetVariable("newchar_class", None), SetVariable("newchar_element", None), SetVariable("newchar_ready", False)


            showif newchar_ready == False:            
                frame:
                    # xsize 1420
                    xsize 1320
                    xpos 535
                    ysize 800
                    # xpos 485
                    yalign 0
                    # background None
                    vbox:
                        spacing 10
                        xalign 0.5
                        xsize 1000

                        null height 20

                        text "RACE" bold True size 30
                        hbox:
                            spacing 10
                            for race in character_races:
                                textbutton race.name action SetVariable("newchar_race", race) text_size 30
                        
                        text "Race Profile" bold True size 30
                        if newchar_race != None:
                            text newchar_race.lore size 25
                        else:
                            text "Choose a Race" size 25
                        text "Racial Bonus" bold True size 30
                        if newchar_race != None:
                            text newchar_race.bonus size 30
                        else:
                            text "Choose a Race" size 25

                        null height 20
                        text "CLASS" bold True size 30
                        hbox:
                            spacing 10
                            for cclass in character_classes:
                                textbutton cclass.name action SetVariable("newchar_class", cclass) text_size 30

                        text "Class Profile" bold True size 30
                        if newchar_class != None:
                            text newchar_class.lore size 25
                        else:
                            text "Choose a class" size 25
                        text "Class Stats" bold True
                        if newchar_class != None:                       
                            hbox:
                                spacing 20
                                text "STR: " + str(newchar_class.str) size 30
                                text "DMG: " + str(newchar_class.dmg) size 30
                                text "TEC: " + str(newchar_class.tec) size 30
                                text "VIT: " + str(newchar_class.vit) size 30
                                text "AGI: " + str(newchar_class.agi) size 30
                                text "LCK: " + str(newchar_class.lck) size 30
                        else:
                            hbox:
                                spacing 20
                                text "STR: 0" size 30
                                text "DMG: 0" size 30
                                text "TEC: 0" size 30
                                text "VIT: 0" size 30
                                text "AGI: 0" size 30
                                text "LCK: 0" size 30

                    frame:
                        xalign 0.95
                        yalign 0.95
                        textbutton "Accept":
                            text_size 30
                            if newchar_class != None and newchar_race != None and party_money >= 10:
                                action SetVariable("newchar_ready", True)

            showif newchar_ready == True:
                frame:
                    xsize 750
                    ysize 400
                    xpos 800
                    yalign 0.5
                    padding (20,20)
                    vbox:
                        xsize 700
                        spacing 20
                        text "What is the new Vagranteer's name?" size 30
                        input length 12:
                            value VariableInputValue("newchar_name")

                        if newchar_class == arcanist:
                            text "What element is this Arcanist attuned to?" size 30
                            hbox:
                                spacing 10
                                for element in ("fire", "ice", "wind", "earth", "thunder", "toxic"):
                                    textbutton element.title() action SetVariable("newchar_element", element) text_size 30
                        if newchar_class == thaumaturge:
                            text "What element is this Thaumaturge attuned to?" size 30
                            hbox:
                                spacing 10
                                for element in ("wind", "earth", "thunder"):
                                    textbutton element.title() action SetVariable("newchar_element", element) text_size 30
                        if newchar_class == herald:
                            text "What element is this Herald attuned to?" size 30
                            hbox:
                                spacing 10
                                for element in ("fire", "ice", "wind", "thunder"):
                                    textbutton element.title() action SetVariable("newchar_element", element) text_size 30
                        frame:
                            xalign 0.95
                            padding (10,10)
                            textbutton "Hire (10 Cr)" text_size 30 action Function(createCharacterRpy, newchar_name, newchar_race, newchar_class, newchar_element), SetVariable("newchar_ready", False), SetVariable("newchar_class", None), SetVariable("newchar_element", None), SetVariable("newchar_name", ""), SetVariable("newchar_race", None),  SetVariable("trainer_command", None)


        showif trainer_command == "Manage":
            fixed:
                xpos 20
                xsize 440
                ypos 0.25
                spacing 20
                
                text "Manage Characters between the roster and the current group." size 30 ypos 20
                
                text "A party must have at least one character, and at most four." size 25 ypos 550

            fixed: # Return button
                ypos 900
                frame:
                    xfill True    
                    ypadding 10
                    textbutton "Return":
                        text_size 50
                        xalign 0.5
                        yalign 0.5
                        if len(party) > 0 and len(party) <= 4:
                            action SetVariable("trainer_command", None)
            
            frame:
                xsize 1420
                ysize 700
                xpos 485
                ypos 120
                background None
                vbox:
                    spacing 10
                    xalign 0.5
                    frame:
                        xsize 1200
                        ysize 350
                        padding (20,20)
                        text "ROSTER" size 30
                        frame:
                            ysize 280
                            ypos 40
                            background None
                            viewport id "roster":
                                draggable True
                                mousewheel True
                                vbox:
                                    null height 10
                                    grid 1 len(character_roster):
                                        spacing 5
                                        for char in character_roster:
                                            fixed:
                                                ysize 50
                                                text char.name size 30 xpos 10
                                                text "Level " + str(char.level) size 30 xpos 280
                                                text char.race.name size 30 xpos 450
                                                text char.char_class.name size 30 xpos 650
                                                textbutton "Add to Party" action Function(addToParty, char) text_size 30 xanchor 1.0 xpos 1120
                            vbar value YScrollValue("roster") xalign 1.0 xoffset 10

                    frame:
                        xsize 1200
                        ysize 300
                        padding (20,20)
                        vbox:
                            text "PARTY" size 30
                            null height 10
                            grid 1 len(party):
                                spacing 5
                                for char in party:
                                    fixed:
                                        ysize 50
                                        text char.name size 30 xpos 10
                                        text "Level " + str(char.level) size 30 xpos 280
                                        text char.race.name size 30 xpos 450
                                        text char.char_class.name size 30 xpos 650
                                        textbutton "Remove" action Function(removeFromParty,char) text_size 30 xanchor 1.0 xpos 1150



screen partymenu:
    zorder 1    
    frame:
        xpadding 15
        ypadding 15
        yalign 0.00
        xalign 1.00
        xfill True
        ysize 780

        vbox: # Menus
            xpos 50
            ypos 0
            xsize 350
            fixed:
                text "VAGRANTEERS" size 50 xalign 0.5 ypos 50
                frame:
                    xfill True
                    ypos 150
                    textbutton "Inventory":
                        action Call("manage_inventory_label")
                        text_size 40

                frame:
                    xfill True
                    ypos 250
                    textbutton "Equipment":
                        action Call("manage_equip_label")
                        text_size 40
                
                frame:
                    xfill True
                    ypos 350
                    textbutton "Skills":
                        action Call("manage_skills_label")
                        text_size 40



        fixed: # Return button and Money
            ypos 600
            xsize 350
            xpos 50
            frame:
                xfill True
                textbutton "Return":
                    text_size 40
                    action Return(value=None)

            fixed:
                xsize 350
                ypos 80
                text "Funds:" size 30 xpos 0
                text "[party_money]" size 25 xanchor 1.0 xpos 250 ypos 2
                text "Crowns" size 25 xpos 260 ypos 2

        grid 4 1: # Show party Statblock
            xpos 565
            ypos 50
            xspacing 20
            transpose True
            for n in party:
                use party_menu_char

screen party_menu_char:
    frame:
        xsize 300
        ysize 600
        fixed:
            xsize 270
            xoffset 15
            yoffset 15
            if CurrentScreenName() == "select_character":        
                textbutton n.name:
                    action SetVariable("selected_character", n), Return(value=n)
                    text_size 40 xpos -7 ypos -6
            else:
                text "[n.name]" size 40

            text "[n.race.name] [n.char_class.name]" size 20 ypos 50
            text "Level [n.level]" size 25 ypos 70
            text "EXP {0} / {1}".format(n.exp, n.level * exptolevel) size 20 ypos 100
            
            text f"HP  {int(n.hp)} / {int(n.maxhp)}" size 30 ypos 130
            text f"TP  {int(n.tp)} / {int(n.maxtp)}" size 30 ypos 160
            
            text "STATS" size 35 ypos 220
            fixed:
                ypos 260
                # xspacing 10
                # transpose True
                text "STR:" size 25 ypos 0 xpos 10
                text "DMG:" size 25 ypos 30 xpos 10
                text "TEC:" size 25 ypos 60 xpos 10
                text f"{int(n.str)}" size 25 ypos 0 xpos 90
                text f"{int(n.dmg)}" size 25 ypos 30 xpos 90
                text f"{int(n.tec)}" size 25 ypos 60 xpos 90
                
                text "VIT:" size 25 ypos 0 xpos 140
                text "AGI:" size 25 ypos 30 xpos 140
                text "LCK:" size 25 ypos 60 xpos 140
                text f"{int(n.vit)}" size 25 ypos 0 xpos 220
                text f"{int(n.agi)}" size 25 ypos 30 xpos 220
                text f"{int(n.lck)}" size 25 ypos 60 xpos 220

            
            text "EQUIPMENT" size 35 ypos 380

            fixed:
                ypos 420
                text  "Wpn.:" size 25 ypos 0
                text  "Arm.:" size 25 ypos 30
                text  "Acc.:" size 25 ypos 60
                text  "Chr.:" size 25 ypos 90

                if n.equip["Weapon"] != None:
                    text "[n.equip[Weapon].name]" size 20 ypos 6 xpos 80
                else:
                    text "[n.equip[Weapon]]" size 25 ypos 2 xpos 80

                if n.equip["Armor"] != None:
                    text "[n.equip[Armor].name]" size 20 ypos 36 xpos 80
                else:
                    text "[n.equip[Armor]]" size 25 ypos 32 xpos 80

                if n.equip["Accessory"] != None:
                    text "[n.equip[Accessory].name]" size 20 ypos 66 xpos 80
                else:
                    text "[n.equip[Accessory]]" size 25 ypos 62 xpos 80

                if n.equip["Charm"] != None:
                    text "[n.equip[Charm].name]" size 20 ypos 96 xpos 80
                else:
                    text "[n.equip[Charm]]" size 25 ypos 92 xpos 80

screen select_character:
    
    frame:
        xpadding 15
        ypadding 15
        yalign 0.00
        xalign 1.00
        xfill True
        ysize 780

        # vbox:
        #     xalign 0.025
        #     yalign 0.5
        #     xsize 350
        #     spacing 25
        #     vbox:
        #         spacing 25
        #         text "VAGRANTEERS" size 50 xalign 0.5

        #         text "Select a character:":
        #             size 40
        #             outlines [(2, "#333", 1, 1)]
                
        #         null height 300

        #         frame:
        #             xfill True
        #             textbutton "Return":
        #                 text_size 40
        #                 action Return(None)

        vbox: # Menus
            xpos 50
            ypos 0
            xsize 350
            fixed:
                text "VAGRANTEERS" size 50 xalign 0.5 ypos 50

                text "Select a character:" size 30 ypos 120
                # frame:
                #     xfill True
                #     ypos 150
                #     textbutton "Inventory":
                #         action Call("manage_inventory_label")
                #         text_size 40

                # frame:
                #     xfill True
                #     ypos 250
                #     textbutton "Equipment":
                #         action Call("manage_equip_label")
                #         text_size 40
                
                # frame:
                #     xfill True
                #     ypos 350
                #     textbutton "Skills":
                #         action Call("manage_skills_label")
                #         text_size 40



        fixed: # Return button and Money
            ypos 600
            xsize 350
            xpos 50
            frame:
                xfill True
                textbutton "Return":
                    text_size 40
                    action Return(value=None)

            # fixed:
            #     xsize 350
            #     ypos -50
            #     text "Funds:" size 30 xpos 0
            #     text "[party_money]" size 25 xanchor 1.0 xpos 250 ypos 2
            #     text "Crowns" size 25 xpos 260 ypos 2



        grid 4 1: # Show party Statblock
                    xpos 565
                    ypos 50
                    xspacing 20
                    transpose True
                    for n in party:
                        use party_menu_char

screen manageEquip:
    frame:
        xpadding 15
        ypadding 15
        yalign 0.00
        xalign 1.00
        xfill True
        ysize 780
        $ charname = selected_character.name.upper()

        vbox:
            xalign 0.025
            yalign 0.5
            xsize 350
            spacing 25
            vbox:
                spacing 25
                


        vbox: # Menus
            xpos 50
            ypos 0
            xsize 350
            fixed:
                # text "VAGRANTEERS" size 50 xalign 0.5 ypos 50
                text f"[charname]'s" size 50 xalign 0.0 ypos 50
                text "Equipment" size 40 xalign 0.0 ypos 100

                text "Select a slot:" size 40 ypos 150

                frame:
                    xfill True
                    ypos 200
                    textbutton "Weapon":
                        text_size 40
                        action [SetVariable("selected_slot", "Weapon"),
                        Jump("manage_equip_slot_label")]

                frame:
                    xfill True
                    ypos 280
                    textbutton "Armor":
                        text_size 40
                        action [SetVariable("selected_slot", "Armor"),
                        Jump("manage_equip_slot_label")]
                    
                frame:
                    xfill True
                    ypos 360
                    textbutton "Accessory":
                        text_size 40
                        action [SetVariable("selected_slot", "Accessory"),
                        Jump("manage_equip_slot_label")]

                frame:
                    xfill True
                    ypos 440
                    textbutton "Charm":
                        text_size 40
                        action [SetVariable("selected_slot", "Charm"),
                        Jump("manage_equip_slot_label")]



        fixed: # Return button and Money
            ypos 600
            xsize 350
            xpos 50
            frame:
                xfill True
                textbutton "Return":
                    text_size 40
                    action Return(value=None)

            # fixed:
            #     xsize 350
            #     ypos 80
            #     text "Funds:" size 30 xpos 0
            #     text "[party_money]" size 25 xanchor 1.0 xpos 250 ypos 2
            #     text "Crowns" size 25 xpos 260 ypos 2



        grid 1 1: # Show selected character's Statblock
            xpos 565
            ypos 50
            xspacing 20
            transpose True
            $ n = selected_character
            use party_menu_char

        if selected_slot == "Weapon":
            use party_equipment_wpn
        elif selected_slot == "Armor":
            use party_equipment_arm
        elif selected_slot == "Accessory":
            use party_equipment_acc
        elif selected_slot == "Charm":
            use party_equipment_charm



screen party_equipment_wpn:
    frame: # Show Party's Inventory
        xsize 900
        ysize 600
        xpos 900 
        ypos 50
        xpadding 20
        ypadding 20

        fixed:
            text "Party's Weapons:" size 30
                        
            text "Name" size 25 ypos 40 xpos 20
            
            text "STR" size 25 ypos 40 xpos 320
            text "DMG" size 25 ypos 40 xpos 400
            text "TEC" size 25 ypos 40 xpos 480

            frame:
                ysize 480
                ypos 80
                background None
                viewport id "wpnlist":
                    draggable True
                    mousewheel True
                    hbox:
                        grid 1 len(equiplist)+1:
                            spacing 5
                            frame:
                                xsize 820
                                textbutton "Remove Weapon": 
                                    action Function(changeEquip, "Weapon", selected_character) text_size 30

                            for n in equiplist:
                                frame:
                                    xsize 820
                                    textbutton "[n.name]":
                                        action Function(changeEquip, n, selected_character)
                                        text_size 30

                        grid 3 len(equiplist):
                            ypos 80
                            xpos -500
                            spacing 29
                            xspacing 70

                            for n in equiplist:
                                text "[n.str]" size 30:
                                    if selected_character.equip["Weapon"] != None:
                                        if n.str < selected_character.equip["Weapon"].str:
                                            color "#F44"
                                        elif n.str > selected_character.equip["Weapon"].str:
                                            color "#1F1"
                                    elif selected_character.equip["Weapon"] == None and n.str > 0:
                                        color "#1F1"

                                text "[n.dmg]" size 30:
                                    if selected_character.equip["Weapon"] != None:
                                        if n.dmg < selected_character.equip["Weapon"].dmg:
                                            color "#F44"
                                        elif n.dmg > selected_character.equip["Weapon"].dmg:
                                            color "#1F1"
                                    elif selected_character.equip["Weapon"] == None and n.dmg > 0:
                                        color "#1F1"

                                text "[n.tec]" size 30:
                                    if selected_character.equip["Weapon"] != None:
                                        if n.tec < selected_character.equip["Weapon"].tec:
                                            color "#F44"
                                        elif n.tec > selected_character.equip["Weapon"].tec:
                                            color "#1F1"
                                    elif selected_character.equip["Weapon"] == None and n.tec > 0:
                                        color "#1F1"

                vbar value YScrollValue("wpnlist") xalign 1.0 xoffset 10

screen party_equipment_arm:
    frame: # Show Party's Inventory
        xsize 900
        ysize 600
        xpos 900 
        ypos 50
        xpadding 20
        ypadding 20

        fixed:
            text "Party's Armors:" size 30
            
            text "Name" size 25 ypos 40 xpos 20

            text "VIT" size 25 ypos 40 xpos 320
            text "AGI" size 25 ypos 40 xpos 400
            text "LCK" size 25 ypos 40 xpos 480
            text "Resist" size 25 ypos 40 xpos 560

            frame:
                ysize 480
                ypos 80
                background None
                viewport id "armlist":
                    draggable True
                    mousewheel True
                    hbox:

                        grid 1 len(equiplist)+1:
                            spacing 5
                            
                            frame:
                                xsize 820
                                textbutton "Remove Armor":
                                    action Function(changeEquip, "Armor", selected_character) text_size 30

                            for n in equiplist:
                                frame:
                                    xsize 820

                                    fixed:
                                        ysize 48
                                        textbutton "[n.name]":
                                            action Function(changeEquip, n, selected_character)
                                            text_size 30

                                        text "[n.vit]" size 30 xpos 320 ypos 5:
                                            if selected_character.equip["Armor"] != None:
                                                if n.vit < selected_character.equip["Armor"].vit:
                                                    color "#F44"
                                                elif n.vit > selected_character.equip["Armor"].vit:
                                                    color "#1F1"
                                            elif selected_character.equip["Armor"] == None and n.vit > 0:
                                                color "#1F1"

                                        text "[n.agi]" size 30 xpos 400 ypos 5:
                                            if selected_character.equip["Armor"] != None:
                                                if n.agi < selected_character.equip["Armor"].agi:
                                                    color "#F44"
                                                elif n.agi > selected_character.equip["Armor"].agi:
                                                    color "#1F1"
                                            elif selected_character.equip["Armor"] == None and n.agi > 0:
                                                color "#1F1"

                                        text "[n.lck]" size 30 xpos 480 ypos 5:
                                            if selected_character.equip["Armor"] != None:
                                                if n.lck < selected_character.equip["Armor"].lck:
                                                    color "#F44"
                                                elif n.lck > selected_character.equip["Armor"].lck:
                                                    color "#1F1"
                                            elif selected_character.equip["Armor"] == None and n.lck > 0:
                                                color "#1F1"

                                        if n.resist != None:
                                            text " ".join(n.resist).title() size 30 xpos 540 ypos 5
                                        else:
                                            text "None" size 30 xpos 560 ypos 5

                vbar value YScrollValue("armlist") xalign 1.0 xoffset 10

screen party_equipment_acc:
    frame: # Show Party's Inventory
        xsize 900
        ysize 600
        xpos 900 
        ypos 50
        xpadding 20
        ypadding 20

        fixed:
            text "Party's Accessories:" size 30
            text "Name" size 25 ypos 40 xpos 20
            text "STR" size 25 ypos 40 xpos 320
            text "DMG" size 25 ypos 40 xpos 380
            text "TEC" size 25 ypos 40 xpos 450
            text "VIT" size 25 ypos 40 xpos 510
            text "AGI" size 25 ypos 40 xpos 560
            text "LCK" size 25 ypos 40 xpos 620
            text "Resist" size 25 ypos 40 xpos 680


            frame:
                ysize 480
                ypos 80
                background None
                viewport id "acclist":
                    draggable True
                    mousewheel True
                    hbox:

                        grid 1 len(equiplist)+2:
                            spacing 5

                            frame:
                                xsize 820
                                textbutton "Remove Accessory":
                                    action Function(changeEquip, "Accessory", selected_character) text_size 30

                            for n in equiplist:
                                frame:
                                    xsize 820

                                    fixed:
                                        ysize 48
                                        textbutton "[n.name]":
                                            action Function(changeEquip, n, selected_character)
                                            text_size 30

                                        text "[n.str]" size 25 xpos 320 ypos 7:
                                            if selected_character.equip["Accessory"] != None:
                                                if n.str < selected_character.equip["Accessory"].str:
                                                    color "#F44"
                                                elif n.str > selected_character.equip["Accessory"].str:
                                                    color "#1F1"
                                            elif selected_character.equip["Accessory"] == None and n.str > 0:
                                                color "#1F1"
                                            elif selected_character.equip["Accessory"] == None and n.str < 0:
                                                color "#F44"

                                        text "[n.dmg]" size 25 xpos 380 ypos 7:
                                            if selected_character.equip["Accessory"] != None:
                                                if n.dmg < selected_character.equip["Accessory"].dmg:
                                                    color "#F44"
                                                elif n.dmg > selected_character.equip["Accessory"].dmg:
                                                    color "#1F1"
                                            elif selected_character.equip["Accessory"] == None and n.dmg > 0:
                                                color "#1F1"
                                            elif selected_character.equip["Accessory"] == None and n.dmg < 0:
                                                color "#F44"

                                        text "[n.tec]" size 25 xpos 450 ypos 7:
                                            if selected_character.equip["Accessory"] != None:
                                                if n.tec < selected_character.equip["Accessory"].tec:
                                                    color "#F44"
                                                elif n.tec > selected_character.equip["Accessory"].tec:
                                                    color "#1F1"
                                            elif selected_character.equip["Accessory"] == None and n.tec > 0:
                                                color "#1F1"
                                            elif selected_character.equip["Accessory"] == None and n.tec < 0:
                                                color "#F44"

                                        text "[n.vit]" size 25 xpos 510 ypos 7:
                                            if selected_character.equip["Accessory"] != None:
                                                if n.vit < selected_character.equip["Accessory"].vit:
                                                    color "#F44"
                                                elif n.vit > selected_character.equip["Accessory"].vit:
                                                    color "#1F1"
                                            elif selected_character.equip["Accessory"] == None and n.vit > 0:
                                                color "#1F1"
                                            elif selected_character.equip["Accessory"] == None and n.vit < 0:
                                                color "#F44"

                                        text "[n.agi]" size 25 xpos 560 ypos 7:
                                            if selected_character.equip["Accessory"] != None:
                                                if n.agi < selected_character.equip["Accessory"].agi:
                                                    color "#F44"
                                                elif n.agi > selected_character.equip["Accessory"].agi:
                                                    color "#1F1"
                                            elif selected_character.equip["Accessory"] == None and n.agi > 0:
                                                color "#1F1"
                                            elif selected_character.equip["Accessory"] == None and n.agi < 0:
                                                color "#F44"

                                        text "[n.lck]" size 25 xpos 620 ypos 7:
                                            if selected_character.equip["Accessory"] != None:
                                                if n.lck < selected_character.equip["Accessory"].lck:
                                                    color "#F44"
                                                elif n.lck > selected_character.equip["Accessory"].lck:
                                                    color "#1F1"
                                            elif selected_character.equip["Accessory"] == None and n.lck > 0:
                                                color "#1F1"
                                            elif selected_character.equip["Accessory"] == None and n.lck < 0:
                                                color "#F44"

                                        if n.resist != None:
                                            text " ".join(n.resist).title() size 25 xpos 680 ypos 7
                                        else:
                                            text "None" size 25 xpos 680 ypos 7

                
                vbar value YScrollValue("acclist") xalign 1.0 xoffset 10


screen party_equipment_charm:
    frame: # Show Party's Charms
        xsize 900
        ysize 600
        xpos 900 
        ypos 50
        xpadding 20
        ypadding 20

        fixed:
            text "Party's Charms:" size 30
            text "Name" size 25 ypos 40 xpos 20
            text "STR" size 25 ypos 40 xpos 320
            text "DMG" size 25 ypos 40 xpos 380
            text "TEC" size 25 ypos 40 xpos 450
            text "VIT" size 25 ypos 40 xpos 510
            text "AGI" size 25 ypos 40 xpos 560
            text "LCK" size 25 ypos 40 xpos 620
            text "Resist" size 25 ypos 40 xpos 680


            frame:
                ysize 480
                ypos 80
                background None
                viewport id "chrlist":
                    draggable True
                    mousewheel True
                    hbox:

                        grid 1 len(equiplist)+2:
                            spacing 5

                            frame:
                                xsize 820
                                textbutton "Remove Charm":
                                    action Function(changeEquip, "Charm", selected_character) text_size 30

                            for n in equiplist:
                                frame:
                                    xsize 820

                                    fixed:
                                        ysize 48
                                        textbutton "[n.name]":
                                            action Function(changeEquip, n, selected_character)
                                            text_size 30

                                        text "[n.str]" size 25 xpos 320 ypos 7:
                                            if selected_character.equip["Charm"] != None:
                                                if n.str < selected_character.equip["Charm"].str:
                                                    color "#F44"
                                                elif n.str > selected_character.equip["Charm"].str:
                                                    color "#1F1"
                                            elif selected_character.equip["Charm"] == None and n.str > 0:
                                                color "#1F1"
                                            elif selected_character.equip["Charm"] == None and n.str < 0:
                                                color "#F44"

                                        text "[n.dmg]" size 25 xpos 380 ypos 7:
                                            if selected_character.equip["Charm"] != None:
                                                if n.dmg < selected_character.equip["Charm"].dmg:
                                                    color "#F44"
                                                elif n.dmg > selected_character.equip["Charm"].dmg:
                                                    color "#1F1"
                                            elif selected_character.equip["Charm"] == None and n.dmg > 0:
                                                color "#1F1"
                                            elif selected_character.equip["Charm"] == None and n.dmg < 0:
                                                color "#F44"

                                        text "[n.tec]" size 25 xpos 450 ypos 7:
                                            if selected_character.equip["Charm"] != None:
                                                if n.tec < selected_character.equip["Charm"].tec:
                                                    color "#F44"
                                                elif n.tec > selected_character.equip["Charm"].tec:
                                                    color "#1F1"
                                            elif selected_character.equip["Charm"] == None and n.tec > 0:
                                                color "#1F1"
                                            elif selected_character.equip["Charm"] == None and n.tec < 0:
                                                color "#F44"

                                        text "[n.vit]" size 25 xpos 510 ypos 7:
                                            if selected_character.equip["Charm"] != None:
                                                if n.vit < selected_character.equip["Charm"].vit:
                                                    color "#F44"
                                                elif n.vit > selected_character.equip["Charm"].vit:
                                                    color "#1F1"
                                            elif selected_character.equip["Charm"] == None and n.vit > 0:
                                                color "#1F1"
                                            elif selected_character.equip["Charm"] == None and n.vit < 0:
                                                color "#F44"

                                        text "[n.agi]" size 25 xpos 560 ypos 7:
                                            if selected_character.equip["Charm"] != None:
                                                if n.agi < selected_character.equip["Charm"].agi:
                                                    color "#F44"
                                                elif n.agi > selected_character.equip["Charm"].agi:
                                                    color "#1F1"
                                            elif selected_character.equip["Charm"] == None and n.agi > 0:
                                                color "#1F1"
                                            elif selected_character.equip["Charm"] == None and n.agi < 0:
                                                color "#F44"

                                        text "[n.lck]" size 25 xpos 620 ypos 7:
                                            if selected_character.equip["Charm"] != None:
                                                if n.lck < selected_character.equip["Charm"].lck:
                                                    color "#F44"
                                                elif n.lck > selected_character.equip["Charm"].lck:
                                                    color "#1F1"
                                            elif selected_character.equip["Charm"] == None and n.lck > 0:
                                                color "#1F1"
                                            elif selected_character.equip["Charm"] == None and n.lck < 0:
                                                color "#F44"

                                        if n.resist != None:
                                            text " ".join(n.resist).title() size 25 xpos 680 ypos 7
                                        else:
                                            text "None" size 25 xpos 680 ypos 7

                
                vbar value YScrollValue("chrlist") xalign 1.0 xoffset 10



screen manageInventory:
    frame: # Left Side Menu
        xpadding 15
        ypadding 15
        yalign 0.00
        xalign 1.00
        xfill True
        ysize 780

        vbox: # Left menu
            xpos 50
            ypos 0
            xsize 350
            fixed:
                text f"Party's Inventory" size 50 xalign 0.0 ypos 50
                text f"Inventory space:\n{len(consumables)} / {inventorylimt}" size 30 ypos 180

        fixed: # Return button and Money
            ypos 600
            xsize 350
            xpos 50
            frame:
                xfill True
                textbutton "Return":
                    text_size 40
                    action Return(value=None)

            fixed:
                xsize 350
                ypos 80
                text "Funds:" size 30 xpos 0
                text "[party_money]" size 25 xanchor 1.0 xpos 250 ypos 2
                text "Crowns" size 25 xpos 260 ypos 2

    frame: # Show Party's Inventory
        xsize 1200
        ysize 650
        xpos 600
        ypos 50
        xpadding 20
        ypadding 20

        text "Consumables:" size 30

        text "Name" size 30 ypos 50
        text "Effect" size 30 xpos 260 ypos 50
        text "Value" size 30 xpos 1000 ypos 50

        viewport id "consum":
            draggable True
            mousewheel True
            ysize 500
            ypos 100
            
            vbox:
                spacing 5
                for n in consumables:
                    frame:
                        xsize 1150
                        ysize 70
                        textbutton "[n.name]":
                            if n.type == "Healing" or n.type == "Reviving":
                                action SetVariable("selected_item", n), Jump("manage_inventory_label.useitemonchar")
                            elif n.type == "Rest" or n.type == "Return":
                                action SetVariable("selected_item", n), Jump("manage_inventory_label.useitem_nochar")
                            text_size 25 ypos 5

                        text n.lore:
                            size 25 xpos 260 xsize 650

                        text "[n.value] Cr" size 25 xpos 1000 ypos 15
        vbar value YScrollValue("consum") xalign 1.0 xoffset 10


screen manageSkills:
    frame:
        xpadding 15
        ypadding 15
        yalign 0.00
        xalign 1.00
        xfill True
        ysize 780
        $ charname = selected_character.name.upper()
        $ n = selected_character
        $ char = selected_character

        vbox: # Left Menu
            xpos 50
            ypos 0
            xsize 350
            fixed:

                text f"[charname]'s" size 50 xalign 0.0 ypos 50
                text f"Skills" size 40 xalign 0.0 ypos 100
                
                
                text "Select a Skill to use or Level Up:": 
                    size 30
                    ypos 160
                

                text f"Skill Points: [char.skillpts]" size 30 ypos 540
                
        fixed: # Return button and Money
            ypos 600
            xsize 350
            xpos 50
            frame:
                xfill True
                textbutton "Return":
                    text_size 40
                    action Return(value=None)

        grid 1 1: # Show selected character's Statblock
            xpos 565
            ypos 50
            xspacing 20
            transpose True
            
            use party_menu_char

        frame: # SKILL Menus
            xsize 965
            ysize 600
            xpos 885
            ypos 50
            padding [20,20]


            showif selected_skill == None: # Select Skill
                fixed:
                    ysize 50
                    text "Skill" size 30
                    text "Level" size 30 xpos 150
                    text "Effect" size 30 xpos 280
                    text "Cost" size 30 xpos 740
            
                viewport id "vpskills":
                    draggable True
                    mousewheel True
                    ypos 60
                    ysize 500
                    vbox:
                        grid 1 len(char.slist):
                            for sk in char.slist:

                                fixed:
                                    xsize 900
                                    ysize 80
                                    if any(substring in sk for substring in ["grun", "mor", "matha", "enhavi", "enhagi", "enhalk", "enfest","enfevi","enfegi","enfelk"]):
                                        if "cura" in sk or "revita" in sk:
                                            textbutton sk.upper():
                                                text_size 25
                                                action SetVariable("selected_skill", sk), Function(levelUpSkill_Check, selected_character, sk, False)
                                        else:    
                                            textbutton sk.upper():
                                                text_size 25 action NullAction()
                                    else:
                                        textbutton sk.upper():
                                            text_size 25
                                            action SetVariable("selected_skill", sk), Function(levelUpSkill_Check, selected_character, sk, False)

                                    if any(substring in sk for substring in ["grun", "mor", "matha", "enhavi", "enhagi", "enhalk", "enfest","enfevi","enfegi","enfelk"]):
                                        text str(char.slist[sk][0]) size 25 xpos 220
                                    else:
                                        text f"Level " + str(char.slist[sk][0]) size 25 xpos 150

                                    # Effect
                                    text char.slist[sk][1] size 25 xpos 280 xsize 450

                                    # HP/TP Costs
                                    if char.slist[sk][2] > 0:
                                        text  str(char.slist[sk][2]) + f" TP" size 25 xpos 740

                                    if len(char.slist[sk]) > 3 and char.slist[sk][3] != "S" and char.slist[sk][3] > 0:
                                        text  str(char.slist[sk][3]) + f" HP" size 25 xpos 800

                vbar value YScrollValue("vpskills") xalign 1.0 xoffset 10

            showif selected_skill != None and selected_target != "choosing": # Use or Level Skill
                frame: # Descriptor
                    background None
                    ysize 480
                    viewport id "skilldescriptor":
                        draggable True
                        mousewheel True
                        vbox:
                            # fixed:
                            text descriptor size 25 xsize 850 line_leading 15
                    vbar value YScrollValue("skilldescriptor") xalign 1.0 xoffset 10

                fixed: # Use skill button
                    ypos 500
                    xpos 10
                    if selected_skill != None:
                        showif char.hp > 0 and any(substring in selected_skill for substring in ["cura", "revita"]):
                            frame:
                                textbutton f"Use Skill ({str(char.slist[selected_skill][2])} TP)":
                                    text_size 30
                                    if "grun" not in selected_skill:
                                        action SetVariable("selected_target", "choosing")
                                    else:
                                        action Function(skillCommand, char, selected_skill, None)


                fixed: # Level up skill buttons
                    ypos 500
                    xpos 450
                    spacing 20
                    text "Level this skill up?" size 25 ypos 10
                    frame:
                        xpos 300
                        xanchor 0.5
                        if selected_skill != None:
                            if selected_character.skillpts >0 and selected_character.slist[selected_skill][0] < 10 and not any(substring in selected_skill for substring in ["grun", "mor", "matha"]):
                                textbutton "Yes":
                                    action Function(levelUpSkill_Check, selected_character, selected_skill, True), SetVariable("selected_skill", None)
                                    text_size 30
                            elif selected_character.slist[selected_skill][0] >= 10:
                                textbutton "Maxed" text_size 30
                            else:
                                textbutton "---" text_size 30
                    frame:
                        xpos 400
                        xanchor 0.5
                        textbutton "No":
                            action SetVariable("selected_skill", None)
                            text_size 30

            showif selected_target == "choosing": # Use Skill on Character
                fixed:
                    xpos 10
                    xsize 600
                    if selected_skill != None:
                        text f"Use {selected_skill.upper()} on who?" size 30 xsize 850 line_leading 15
                        text f"This will cost {str(char.slist[selected_skill][2])} TP" size 30 ypos 50
                        text f"{str(char.slist[selected_skill][1])}" size 25 ypos 80

                        if char.tp < char.slist[selected_skill][2]:
                            text f"Not enough TP" size 30 xpos 100 ypos 150 color "#F44"

                fixed:
                    ypos 200
                    xpos 100
                    grid 1 len(party) + 1:
                        spacing 5
                        for person in party:
                            frame:
                                xsize 400
                                ysize 60
                                textbutton person.name text_size 30 action Function(skillCommand, char, selected_skill, person)
                                text f"{int(person.hp)} / {int(person.maxhp)}" size 25 xanchor 1.0 xpos 380 ypos 10
                        frame:
                            xsize 400
                            textbutton "Cancel" text_size 30 action SetVariable("selected_target", None)

screen dungeon_danger:
    zorder -1
    frame:
        xsize 400
        ysize 200
        xalign 1.0
        yalign 0.2
        xpadding 25
        ypadding 25
        background None

        grid 1 2:
            xalign 0.5
            yalign 0.5
            text "DANGER":
                xalign 0.5
                size 40
                bold True
                # outlines [(4, "#333", 2, 2)]
                if danger > 85:
                    color "#F33" outlines [(4, "#FFF", 2, 2)]
                elif danger >50:
                    color "#CC3" outlines [(4, "#333", 2, 2)]
                elif danger > 25:
                    color "#3F3" outlines [(4, "#333", 2, 2)]
                else:
                    color "#FFF" outlines [(4, "#333", 2, 2)]
            if restAreaCheck() == True:
                text "Safe Area":
                    xalign 0.5
                    size 40
                    bold True
                    color "#3F3" outlines [(4, "#333", 2, 2)]
            
screen dungeon_explore:
    zorder -1
    frame:
        xsize 1420
        ysize 780
        xalign 1.0
        background None

        frame:
            xalign 0.5
            yalign 0.5
            padding [20,20]
            grid view_distance*2+1 view_distance*2+1:
                xspacing 5
                yspacing 5
                xalign 0.5
                yalign 0.5

                for ty in range(len(localmap)):
                    for n in localmap[ty]:
                        if n == ' ':
                            add "dgfloor"
                        elif n == '■':
                            add "dgwall"
                        elif n == "X":
                            add "dgdark"
                        elif n == '□':
                            add "dgdoor"
                        elif n == '♠':
                            add "dgstairsd"
                        elif n == '♦':
                            add "dgstairsu"
                        elif n == "●":
                            add "dgchestc"
                        elif n == "○":
                            add "dgchesto"
                        elif n == "▲":
                            add "partyN"
                        elif n == "▼":
                            add "partyS"
                        elif n == "◄":
                            add "partyW"
                        elif n == "►":
                            add "partyE"
                        elif n == "↔":
                            add "dgpasswe"
                        elif n == "↕":
                            add "dgpassns"
                        elif n == "☺":
                            add "dgmerch"
                        elif n == "↑":
                            add "dgpassn"
                        elif n == "↓":
                            add "dgpasss"
                        elif n == "→":
                            add "dgpasse"
                        elif n == "←":
                            add "dgpassw"
                        else:
                            add "dgfloor"


screen dungeon_playermap:
    zorder +2

    python:
        if party_facing is not None: # Print Party Facing to middle of @localmap
            if party_facing == 8:
                dungeon_playermap[party_coord[0]][party_coord[1]] = "▲"

            elif party_facing == 2:
                dungeon_playermap[party_coord[0]][party_coord[1]] = "▼"

            elif party_facing == 4:
                dungeon_playermap[party_coord[0]][party_coord[1]] = "◄"
            
            elif party_facing == 6:
                dungeon_playermap[party_coord[0]][party_coord[1]] = "►"

    frame:
        # xsize 1420
        xfill True
        ysize 780
        xalign 1.0
        # background None

        key "K_TAB" action Return()

        fixed: # Left menu
            ypos 0
            xsize 350
            xpos 50

            text f"Dungeon Map" size 50 xalign 0.0 ypos 50
            text f"Floor: {dungeon_level}" size 30 ypos 180
            text f"{mapcompletion}% mapped" size 30 ypos 230



        fixed: # Return button
                ypos 600
                xsize 350
                xpos 50
                frame:
                    xfill True
                    textbutton "Return":
                        text_size 40
                        action Return(value=None)

        frame:
            xsize 1420
            xalign 1.0
            yalign 0.5

            

            viewport id "dgplayermap":
                draggable True
                mousewheel True
                
                grid len(dungeon_playermap) len(dungeon_playermap):
                    xspacing 3
                    yspacing 3
                    xalign 0.5
                    yalign 0.5

                    for ty in range(len(dungeon_playermap)):
                        for n in dungeon_playermap[ty]:
                            if n == 0:
                                add "dgfloor" zoom playermapzoom
                            elif n == 1 or n == 9 or n == N or n == S or n == W or n == E:
                                add "dgwall" zoom playermapzoom
                            elif n == None or n == "out":
                                add "dgdark" zoom playermapzoom
                            elif n == 2 or n == 3:
                                add "dgdoor" zoom playermapzoom
                            elif n == D:
                                add "dgstairsd" zoom playermapzoom
                            elif n == U:
                                add "dgstairsu" zoom playermapzoom
                            elif n == C:
                                add "dgchestc" zoom playermapzoom
                            elif n == O:
                                add "dgchesto" zoom playermapzoom
                            elif n == "▲":
                                add "partyN" zoom playermapzoom
                            elif n == "▼":
                                add "partyS" zoom playermapzoom
                            elif n == "◄":
                                add "partyW" zoom playermapzoom
                            elif n == "►":
                                add "partyE" zoom playermapzoom

                            elif n == 6:
                                add "dgpasswe" zoom playermapzoom
                            elif n == 8:
                                add "dgpassns" zoom playermapzoom
                            elif n == M:
                                add "dgmerch" zoom playermapzoom
                            elif n == SO:
                                add "dgpassn" zoom playermapzoom
                            elif n == NO:
                                add "dgpasss" zoom playermapzoom
                            elif n == WO:
                                add "dgpasse" zoom playermapzoom
                            elif n == EO:
                                add "dgpassw" zoom playermapzoom
                            else:
                                add "dgdark" zoom playermapzoom
            
            # bar value XScrollValue("dgplayermap") yalign 1.0 yoffset 10
            vbar value YScrollValue("dgplayermap") xalign 1.0 xoffset 10

    python:
        dungeon_playermap[party_coord[0]][party_coord[1]] = 0

screen mapmaker_screen:
    zorder +2

    

    frame:
        # xsize 1420
        xfill True
        # ysize 780
        yfill True
        xalign 1.0
        # background None

        # key "K_TAB" action Return()

        fixed: # Left menu
            ypos 0
            xsize 350
            xpos 50

            text f"Dungeon Map" size 50 xalign 0.0 ypos 50
            text f"Creating a new Floor" size 30 ypos 180
            text f"Placement Mode:\n{mapplacement}" size 30 ypos 250

        fixed: 
            ypos 350
            xpos 50
            xsize 350
            
            transform: # TILE BUTTONS
                zoom 0.8
                grid 4 4:
                    spacing 10

                    imagebutton idle "dgwall" action SetVariable("mapplacement", "Wall")
                    imagebutton idle "dgfloor" action SetVariable("mapplacement", "Floor")
                    imagebutton idle "dgdoor" action SetVariable("mapplacement", "Door")
                    text ""

                    imagebutton idle "dgpassw" action SetVariable("mapplacement", "Secret Passage E > W")
                    imagebutton idle "dgpassn" action SetVariable("mapplacement", "Secret Passage S > N")
                    imagebutton idle "dgpasss" action SetVariable("mapplacement", "Secret Passage N > S")
                    imagebutton idle "dgpasse" action SetVariable("mapplacement", "Secret Passage W > E")

                    imagebutton idle "dgpasssecret" action SetVariable("mapplacement", "Secret Passage")
                    text ""
                    # imagebutton idle "dgpassns" action SetVariable("mapplacement", "Secret Passage NS")
                    imagebutton idle "dgstairsu" action SetVariable("mapplacement", "Stairs Up")
                    imagebutton idle "dgstairsd" action SetVariable("mapplacement", "Stairs Down")

                    imagebutton idle "dgchestc" action SetVariable("mapplacement", "Chest")
                    imagebutton idle "dgmerch" action SetVariable("mapplacement", "Merchant")
                    text ""
                    text ""

            frame:
                xfill True
                ypos 400
                textbutton "Clear" text_size 40 action SetVariable("newdungeon", blankNewMap())

            frame:
                xfill True
                ypos 500
                textbutton "Copy" text_size 40 action Function(copyMap)


        fixed: # Return button
                ypos 950
                xsize 350
                xpos 50
                frame:
                    xfill True
                    textbutton "Return":
                        text_size 40
                        # action Return()
                        action Hide("mapmaker_screen")

        frame: # Map Tiles
            xsize 1420
            xalign 1.0
            yalign 0.5

            viewport id "mapmakerscren":
                # draggable True
                mousewheel True
                
                grid len(newdungeon) len(newdungeon):
                    xspacing 3
                    yspacing 3
                    xalign 0.5
                    yalign 0.5

                    for ty in range(len(newdungeon)):

                        for tx in range(len(newdungeon[ty])):
                            transform:
                                zoom 0.4
                                if newdungeon[ty][tx] == 0:
                                    imagebutton idle "dgfloor" action Function(toggleMapTile, ty, tx)
                                elif newdungeon[ty][tx] == 1:
                                    imagebutton idle "dgwall" action Function(toggleMapTile, ty, tx)
                                elif newdungeon[ty][tx] == 2:
                                    imagebutton idle "dgdoor" action Function(toggleMapTile, ty, tx)

                                elif newdungeon[ty][tx] == E:
                                    imagebutton idle "dgpassw" action Function(toggleMapTile, ty, tx)
                                elif newdungeon[ty][tx] == W:
                                    imagebutton idle "dgpasse" action Function(toggleMapTile, ty, tx)
                                elif newdungeon[ty][tx] == N:
                                    imagebutton idle "dgpasss" action Function(toggleMapTile, ty, tx)
                                elif newdungeon[ty][tx] == S:
                                    imagebutton idle "dgpassn" action Function(toggleMapTile, ty, tx)

                                elif newdungeon[ty][tx] == 9:
                                    imagebutton idle "dgpasssecret" action Function(toggleMapTile, ty, tx)
                                elif newdungeon[ty][tx] == U:
                                    imagebutton idle "dgstairsu" action Function(toggleMapTile, ty, tx)
                                elif newdungeon[ty][tx] == D:
                                    imagebutton idle "dgstairsd" action Function(toggleMapTile, ty, tx)

                                elif newdungeon[ty][tx] == C:
                                    imagebutton idle "dgchestc" action Function(toggleMapTile, ty, tx)
                                elif newdungeon[ty][tx] == M:
                                    imagebutton idle "dgmerch" action Function(toggleMapTile, ty, tx)

            # bar value XScrollValue("mapmakerscren") yalign 1.0 yoffset 10
            vbar value YScrollValue("mapmakerscren") xalign 1.0 xoffset 10

    python:
        dungeon_playermap[party_coord[0]][party_coord[1]] = 0



$ logoffset = 0
screen dungeon_command:

    python:
        if yadj.value == yadj.range:
            yadj.value = float('inf')

    

    zorder 1
    frame:
        yfill True
        xsize 500

        vbox:
            xalign 0.5
            # spacing 20
            # null height 20
            frame: # Activity Log
                xsize 500
                ysize 650
                viewport id "dglog" yadjustment yadj:
                    draggable True
                    mousewheel True
                    vbox:
                        null height 20
                        text "  Activity Log" yalign 0.1
                        null height 20

                        text "[logtextprint]" yalign 1.0 line_leading 20 size 20 xpos 20
                        null height 20

                vbar value YScrollValue("dglog") xalign 1.0 xoffset 10


            grid 3 2:
                xalign 0.5
                yalign 0.5
                spacing 10

                imagebutton idle "buttonturnccwidle" hover "buttonturnccwhover"  action Function(turnLeft)
                imagebutton idle "buttonforwidle" hover "buttonforwhover" action Function(moveForwards)
                imagebutton idle "buttonturncwidle" hover "buttonturncwhover" action Function(turnRight)
                
                # imagebutton idle "buttonleftidle" hover "buttonlefthover"  action NullAction()
                # imagebutton idle "buttonbackidle" hover "buttonbackhover" action NullAction()
                # imagebutton idle "buttonrightidle" hover "buttonrighthover" action NullAction()

                # imagebutton idle "buttonhandidle" hover "buttonlefthover"  action NullAction()
                imagebutton idle "buttonmapidle" hover "buttonmaphover" action Call("dgplayermap_label")
                imagebutton idle "buttonhandidle" hover "buttonhandhover" action Function(interactKey)
                imagebutton idle "buttonpartyidle" hover "buttonpartyhover" action Call("party_menu_scene")

            fixed:
                ypos -280
                xpos -10
                
                
                text "Q" size 30 xpos 50 outlines [(3, "#333", 2, 2)]
                text "W" size 30 xpos 200 outlines [(3, "#333", 2, 2)]
                text "E" size 30 xpos 350 outlines [(3, "#333", 2, 2)]
                text "TAB" size 30 xpos 50 ypos 150 outlines [(3, "#333", 2, 2)]
                text "F" size 30 xpos 200 ypos 150 outlines [(3, "#333", 2, 2)]
                text "R" size 30 xpos 350 ypos 150 outlines [(3, "#333", 2, 2)]

            key "q" action Function(turnLeft)
            key "w" action Function(moveForwards)
            key "e" action Function(turnRight)
            # key "a" action Function
            # key "s" action Function
            key "K_TAB" action Call("dgplayermap_label")
            key "f" action Function(interactKey)
            key "r" action Call("party_menu_scene")

screen initiative_screen:
    zorder 2
    frame:
        xsize 1000
        ysize 200
        xalign 0.6
        yalign 0.05
        xpadding 25
        ypadding 25
        # background None

        vbox:
            xsize 950
            text "INITIATIVE:" size 30
            hbox:
                box_wrap True
                for char in initiative:
                    if char not in party:
                        if char.hp > 0:
                            text char.name + ", " color "#FA0" size 25
                    else:
                        if char == charinit:
                            text char.name + ", " color "#7070b9" size 25
                        elif char.hp <= 0:
                            text char.name + ", " color "#F55" size 25
                        else:
                            text char.name + ", " size 25

screen combat_screen:
    zorder -1
    frame:
        xsize 1420
        ysize 780
        xalign 1.0
        background None

        hbox:
            yalign 0.7
            xalign 0.5
            spacing 30
            for enemy in opposition:
                vbox id enemy.name:
                    spacing 5
                    add "dgmerch" xanchor 0.5 
                    text enemy.name size 30 xanchor 0.5
                    bar value AnimatedValue(value=enemy.hp, range=enemy.maxhp,delay=0.5) xsize 250 ysize 30 xanchor 0.5
                    text f"Level {enemy.level}" size 30 xanchor 0.5

screen combat_log:
    
    python:
        if yadj.value == yadj.range:
            yadj.value = float('inf')
    
    zorder 1
    frame:
        ysize 650
        xsize 500
                    
        viewport id "comblog" yadjustment yadj:
            draggable True
            mousewheel True
            vbox:
                null height 20
                text "  Activity Log" yalign 0.1
                null height 20

                text "[logtextprint]" yalign 1.0 line_leading 20 size 20 xpos 20 xsize 460
                null height 20
        vbar value YScrollValue("comblog") xalign 1.0 xoffset 10

screen combat_command: # Command for @charinit
    zorder 1
    frame:
        ysize 430
        xsize 500
        ypos 650

        viewport id "combcomm":
            draggable True
            mousewheel True
            vbox:
                xalign 0.5
                spacing 20
                null height 20

                showif battlecommand == None:
                    vbox:
                        # xalign 0.2
                        # yalign 0.5
                        ypos -20
                        xpos 20
                        spacing 10
                        

                        text "Command:" size 30
                        frame:
                            xsize 400
                            textbutton "Attack" action SetVariable("battlecommand", "Attack") text_size 30
                        frame:
                            xsize 400
                            textbutton "Skills" action SetVariable("battlecommand", "Skill") text_size 30
                        frame:
                            xsize 400
                            textbutton "Defend" action SetVariable("battlecommand", "Defend") text_size 30
                        frame:
                            xsize 400
                            textbutton "Item" action SetVariable("battlecommand", "Item") text_size 30
                        frame:
                            xsize 400
                            textbutton "Escape" action SetVariable("battlecommand", "Escape") text_size 30

                showif battlecommand == "Attack":
                    vbox:
                        ypos -20
                        xpos 20
                        spacing 10
                        
                        text "Who?" size 30
                        frame:
                            xsize 400
                            textbutton "Return" action SetVariable("battlecommand", None) text_size 30
                        for enemy in opposition:
                            frame:
                                xsize 400
                                textbutton enemy.name text_size 30 action Function(attackfunc, charinit, enemy), SetVariable("charinit.acted", True), Return()

                showif battlecommand == "Skill":
                    vbox:
                        ypos -20
                        xpos 20
                        spacing 10
                        
                        text "Which?" size 30
                        frame:
                            xsize 400
                            textbutton "Return" action SetVariable("battlecommand", None) text_size 30
                        for skill in charinit.slist:
                            frame:
                                xsize 400
                                fixed: # SKill list
                                    ysize 50
                                    textbutton skill.title() action SetVariable("selected_skill", skill), SetVariable("battlecommand", "skillchoosen") text_size 30 xpos 0

                                    # HP/TP Costs
                                    if charinit.slist[skill][2] > 0:
                                        text  str(charinit.slist[skill][2]) + f" TP" size 25 ypos 10  xpos 380 xanchor 1.0 

                                    if len(charinit.slist[skill]) > 3 and charinit.slist[skill][3] != "S" and charinit.slist[skill][3] > 0:
                                        text  str(charinit.slist[skill][3]) + f" HP" size 25 ypos 10 xpos 300 xanchor 1.0

                showif battlecommand == "skillchoosen":
                    vbox:
                        ypos -20
                        xpos 20
                        spacing 10
                        
                        text "Confirm?" size 30
                        if selected_skill != None:
                            text selected_skill.upper() + ": " + charinit.slist[selected_skill][1] size 25 xsize 400
                            # text charinit.slist[selected_skill][1] size 25

                        frame:
                            xsize 400
                            textbutton "Return" action SetVariable("selected_skill", None), SetVariable("battlecommand", "Skill") text_size 30
                        
                        if selected_skill != None:
                            
                            # ELEM SKILL Target ONE Enemy
                            if "cura" not in selected_skill and "revita" not in selected_skill and "grun" not in selected_skill and any(element in selected_skill for element in ["firo", "gelo", "gale", "tera", "volt", "veno", "nuke"]): # Target one enemy
                                for enemy in opposition:
                                    frame:
                                        xsize 400
                                        textbutton enemy.name text_size 30 action Function(skillCommand,charinit,selected_skill, enemy) 

                            # ELEM SKILL Target ALL enemies
                            elif "cura" not in selected_skill and "revita" not in selected_skill and "grun" in selected_skill and any(element in selected_skill for element in ["firo", "gelo", "gale", "tera", "volt", "veno", "nuke"]): # Target all enemies
                                frame:
                                    xsize 400
                                    textbutton "Confirm" text_size 30 action Function(skillCommand,charinit,selected_skill, None)#, SetVariable("charinit.acted", True), SetVariable("selected_skill", None), Return()

                            # PHYSical skills ONE Enemy: SNEAK / HUNT
                            elif selected_skill in ("sneak","charge","hunt"): # Physical Skills
                                for enemy in opposition:
                                    frame:
                                        xsize 400
                                        textbutton enemy.name text_size 30 action Function(skillCommandPhys,charinit,selected_skill, enemy)#, SetVariable("charinit.acted", True), SetVariable("selected_skill", None), Return()

                            # PHYSical Skills GROUP: CLEAVE / BOMB
                            elif "cleave" in selected_skill or "bomb" in selected_skill: # Physical Skills
                                frame:
                                    xsize 400
                                    textbutton "Confirm" text_size 30 action Function(skillCommandPhys,charinit,selected_skill, None)#, SetVariable("charinit.acted", True), SetVariable("selected_skill", None), Return()

                            # CURA
                            elif "cura" in selected_skill and "grun" not in selected_skill: # Target one ally
                                for char in party:
                                    if char.hp >0:
                                        frame:
                                            xsize 400
                                            textbutton char.name text_size 30 action Function(skillCommand,charinit,selected_skill, char)#, SetVariable("charinit.acted", True), SetVariable("selected_skill", None), Return()

                            # REVITA
                            elif "revita" in selected_skill:
                                for char in party:
                                    if char.hp <= 0:
                                        frame:
                                            xsize 400
                                            textbutton char.name text_size 30 action Function(skillCommand,charinit,selected_skill, char)#, SetVariable("charinit.acted", True), SetVariable("selected_skill", None), Return()

                            # GRUN CURA 
                            elif "cura" in selected_skill and "grun" in selected_skill: # Target all allies
                                frame:
                                    xsize 400
                                    textbutton "Confirm" text_size 30 action Function(skillCommand,charinit,selected_skill, None)#, SetVariable("charinit.acted", True), SetVariable("selected_skill", None), Return()

                            # DECOY
                            elif selected_skill in "decoy":
                                frame:
                                    xsize 400
                                    textbutton "Confirm" text_size 30 action Function(skillCommandSupp,charinit,selected_skill, None), SetVariable("selected_skill", None)

                            # ENHA skills / single
                            elif "enha" in selected_skill and "grun" not in selected_skill:
                                for char in party:
                                    frame:
                                        xsize 400
                                        textbutton char.name text_size 30 action Function(skillCommandSupp,charinit,selected_skill, char), SetVariable("selected_skill", None)

                            # ENHA skills / group / PROTECT / TAUNT / COATING
                            elif "enha" in selected_skill and "grun" in selected_skill or "protect" in selected_skill or "taunt" in selected_skill or "coating" in selected_skill:
                                frame:
                                    xsize 400
                                    textbutton "Confirm" text_size 30 action Function(skillCommandSupp,charinit,selected_skill, None), SetVariable("selected_skill", None)

                            # ENFE skills / single / APPRAISE
                            elif "enfe" in selected_skill and "grun" not in selected_skill or "appraise" in selected_skill:
                                for enemy in opposition:
                                    frame:
                                        xsize 400
                                        textbutton enemy.name text_size 30 action Function(skillCommandSupp,charinit,selected_skill, enemy), SetVariable("selected_skill", None)

                            # ENFE skills / GROUP
                            elif "enfe" in selected_skill and "grun" in selected_skill:
                                frame:
                                    xsize 400
                                    textbutton "Confirm" text_size 30 action Function(skillCommandSupp,charinit,selected_skill, None), SetVariable("selected_skill", None)

                showif battlecommand == "Defend":
                    vbox:
                        ypos -20
                        xpos 20
                        spacing 10
                        
                        text "You sure?" size 30
                        frame:
                            xsize 400
                            textbutton "Return" action SetVariable("battlecommand", None) text_size 30
                        frame:
                            xsize 400
                            textbutton "Confirm" text_size 30 action SetVariable("charinit.defending", True), SetVariable("charinit.acted",True), Function(logText,f"{charinit.name} is defending."), Return()

                showif battlecommand == "Item":
                    vbox:
                        ypos -20
                        xpos 20
                        spacing 10
                        
                        text "What Item?" size 30
                        frame:
                            xsize 400
                            textbutton "Return" text_size 30 action SetVariable("battlecommand", None) 
                        
                        for item in consumables:
                            if item.type in ("Healing","Reviving","Combat"):
                                frame:
                                    xsize 400
                                    textbutton item.name text_size 30 action SetVariable("selected_item", item), SetVariable("battlecommand", "Itemchoosen")

                showif battlecommand == "Itemchoosen":
                    vbox:
                        ypos -20
                        xpos 20
                        spacing 10
                        
                        text "You Sure?" size 30
                        if selected_item != None and selected_item != True:
                            text selected_item.name size 25
                            text selected_item.lore size 25
                        frame:
                            xsize 400
                            textbutton "Return" text_size 30 action SetVariable("battlecommand", None)
                        
                        if selected_item != None and selected_item != True:
                            if selected_item.type in ("Healing","Reviving"): # Healing items
                                for char in party:
                                    frame:
                                        xsize 400
                                        textbutton char.name text_size 30 action Function(useItem, selected_item, char)
                                    
                        if selected_item == True:
                            timer 0.001 action SetVariable("charinit.acted", True), SetVariable("selected_item", None), Return()

                showif battlecommand == "Escape":
                    vbox:
                        ypos -20
                        xpos 20
                        spacing 10
                        
                        text "You sure?" size 30
                        frame:
                            xsize 400
                            textbutton "Return" text_size 30 action SetVariable("battlecommand", None)
                        frame:
                            xsize 400
                            textbutton "Confirm" text_size 30 action Function(escapeCommand, charinit),  Return()

        vbar value YScrollValue("combcomm") xalign 1.0 xoffset 10

    if charinit.acted == True:
        timer 0.001 action SetVariable("selected_skill", None), Return()
        

screen combat_results:
    zorder 3

    timer 0.5 action Function(calcRewards)
        
    frame:
        xalign 0.5
        yalign 0.3
        xsize 900
        ysize 650
        padding [40,40]

        vbox:
            text resultstext size 30

            null height 30
            for char in party:
                vbox:
                    grid 3 1:
                        spacing 20
                        fixed:
                            ysize 40
                            text char.name.upper() size 30
                            text "Level " + str(char.level) + " / Experience:" size 30 xanchor 0.5 xpos 400
                            text str(char.exp) + " / " + str(char.level * exptolevel) xanchor 1.0 size 30 xpos 800
                if char.level > 1:
                    bar value AnimatedValue(value=(char.exp - (char.level -1)  * exptolevel), range=(char.level -1) *exptolevel, delay=2) xsize 800 ysize 20
                else:
                    bar value AnimatedValue(value=(char.exp - (char.level -1)  * exptolevel), range=(char.level) *exptolevel, delay=2) xsize 800 ysize 20
                null height 20
            
            null height 50
        frame:
            # padding (20,20)
            yalign 0.975
            xalign 0.95
            textbutton "Continue" text_size 30 action Return() 
                
screen levelUpScreen:

    # chartolevel = char
    # charstattolevel = None

    frame:
        xsize 1000
        ysize 750
        xalign 0.5
        yalign 0.1
        if chartolevel != None:
            vbox:
                xpos 150
                xsize 700
                null height 50
                
                text f"{chartolevel.name}, {chartolevel.race.name} {chartolevel.char_class.name}"
                text "has leveled up!"

                text "Choose one stat to increase." size 30

                null height 20
                fixed: # Level
                    ysize 60
                    xpos 50
                    text "Level" xpos 0
                    text f"{chartolevel.level}" + "  >  " + f"{chartolevel.level+1}" xpos 200
                    
                fixed: # HP
                    ysize 60
                    xpos 50
                    text "Max HP:" xpos 0
                    text f"{math.floor(chartolevel.maxhp)}" + "  >  " + f"{math.floor(chartolevel.maxhp+(chartolevel.char_class.improv[0]*chartolevel.char_class.hp))}" xpos 200
                    frame:
                        xpos 420
                        ypos -5
                        ysize 50
                        textbutton f"+ {math.floor(chartolevel.char_class.hp)}" text_size 28 yalign 0.5 action SetVariable("charstattolevel", "hp"), Return()
                    text f">  {math.floor(chartolevel.maxhp+(chartolevel.char_class.improv[0]*chartolevel.char_class.hp)+(chartolevel.char_class.hp))}" xpos 520
                    
                
                fixed: # TP
                    ysize 60
                    xpos 50
                    text "Max TP:" xpos 0
                    text f"{math.floor(chartolevel.maxtp)}" + "  >  " + f"{math.floor(chartolevel.maxtp+(chartolevel.char_class.improv[1]*chartolevel.char_class.tp))}" xpos 200
                    frame:
                        xpos 420
                        ypos -5
                        ysize 50
                        textbutton f"+ {math.floor(chartolevel.char_class.tp)}" text_size 28 yalign 0.5 action SetVariable("charstattolevel", "tp"), Return()
                    text f">  {math.floor(chartolevel.maxtp+(chartolevel.char_class.improv[1]*chartolevel.char_class.tp)+(chartolevel.char_class.tp))}" xpos 520

                fixed: # STR
                    ysize 60
                    xpos 50
                    text "STR:" xpos 0
                    text f"{math.floor(chartolevel.str)}" + "  >  " + f"{math.floor(chartolevel.str+chartolevel.char_class.improv[2])}" xpos 200
                    frame:
                        xpos 420
                        ypos -5
                        ysize 50
                        textbutton "+ 1" text_size 28 yalign 0.5 action SetVariable("charstattolevel", "str"), Return()
                    text f">  {math.floor(chartolevel.str+chartolevel.char_class.improv[2]+1)}" xpos 520

                fixed: # DMG
                    ysize 60
                    xpos 50
                    text "DMG:" xpos 0
                    text f"{math.floor(chartolevel.tec)}" + "  >  " + f"{math.floor(chartolevel.tec+chartolevel.char_class.improv[7])}" xpos 200
                    # frame:
                    #     xpos 500
                    #     ypos -5
                    #     ysize 50
                    #     textbutton "+ 1" text_size 28 yalign 0.5 action NullAction()

                fixed: # TEC
                    ysize 60
                    xpos 50
                    text "TEC:" xpos 0
                    text f"{math.floor(chartolevel.tec)}" + "  >  " + f"{math.floor(chartolevel.tec+chartolevel.char_class.improv[3])}" xpos 200
                    frame:
                        xpos 420
                        ypos -5
                        ysize 50
                        textbutton "+ 1" text_size 28 yalign 0.5 action SetVariable("charstattolevel", "tec"), Return()
                    text f">  {math.floor(chartolevel.tec+chartolevel.char_class.improv[3]+1)}" xpos 520

                fixed: # VIT
                    ysize 60
                    xpos 50
                    text "VIT:" xpos 0
                    text f"{math.floor(chartolevel.vit)}" + "  >  " + f"{math.floor(chartolevel.vit+chartolevel.char_class.improv[4])}" xpos 200
                    frame:
                        xpos 420
                        ypos -5
                        ysize 50
                        textbutton "+ 1" text_size 28 yalign 0.5 action SetVariable("charstattolevel", "vit"), Return()
                    text f">  {math.floor(chartolevel.vit+chartolevel.char_class.improv[4]+1)}" xpos 520

                fixed: # AGI
                    ysize 60
                    xpos 50
                    text "AGI:" xpos 0
                    text f"{math.floor(chartolevel.agi)}" + "  >  " + f"{math.floor(chartolevel.agi+chartolevel.char_class.improv[5])}" xpos 200
                    frame:
                        xpos 420
                        ypos -5
                        ysize 50
                        textbutton "+ 1" text_size 28 yalign 0.5 action SetVariable("charstattolevel", "agi"), Return()
                    text f">  {math.floor(chartolevel.agi+chartolevel.char_class.improv[5]+1)}" xpos 520

                fixed: # LCK
                    ysize 60
                    xpos 50
                    text "LCK:" xpos 0
                    text f"{math.floor(chartolevel.lck)}" + "  >  " + f"{math.floor(chartolevel.lck+chartolevel.char_class.improv[6])}" xpos 200
                    frame:
                        xpos 420
                        ypos -5
                        ysize 50
                        textbutton "+ 1" text_size 28 yalign 0.5 action SetVariable("charstattolevel", "lck"), Return()
                    text f">  {math.floor(chartolevel.lck+chartolevel.char_class.improv[6]+1)}" xpos 520


##