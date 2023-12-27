define config.rollback_enabled = False # No rollback in game

label start:
    show screen party
    show screen time
    jump town_scene
    
    return

label town_scene:
    $ party_screen_shown = False
    $ logtext = []
    $ logtextprint = ""

    if hour >= 18 or hour <=5:
        scene bg Town at scenerydark with dissolve
    else:
        scene bg Town at scenery with dissolve
    

    label .screen:
    
    call screen town with dissolve

    jump town_scene.screen

label tavern_scene:
    $ tavern_command = None
    scene bg Tavern at scenery with dissolve

    label .screen:
    call screen tavern with dissolve
    jump tavern_scene.screen

    label .rest:
    if tavernRest() == True:
        scene black with dissolve
        $ renpy.say("Ontam", "Then please, come this way to the bedrooms.")
        $ renpy.say(None,"Time passed and all characters in party have fully rested!")
        $ renpy.say("Ontam","Thanks for your patronage. Hope to see you soon!")
    else:
        $ renpy.say("Ontam","Ah, sorry, you don't have enough money to pay for lodgings here. Maybe sell something at the shop or hunt a few more shades?")

    jump tavern_scene
    


label shop_scene:

    $ shop_command = None
    $ shop_type = None
    scene bg Shop at scenery with dissolve

    label .screen:
    call screen shop with dissolve
    jump shop_scene.screen

label merchant_label:

    $ shop_command = None
    $ shop_type = None

    hide screen dungeon_explore
    call screen merchant with dissolve
    show screen dungeon_explore
    return


label trainer_scene:
    $ trainer_command = None

    $ newchar_name = ""
    $ newchar_ready = False
    $ newchar_race = None
    $ newchar_class = None
    $ newchar_element = None


    if hour >= 18 or hour <=5:
        scene bg Arena at scenerydark with dissolve
    else:
        scene bg Arena at scenery with dissolve
    

    label .screen:
    call screen trainer with dissolve

    jump trainer_scene.screen


label party_menu_scene:

    # call screen partymenu with dissolve
    call screen partymenu
    return
    
label manage_equip_label:

    $ selected_character = None
    $ selected_slot = None
    call screen select_character

    if selected_character == None:
        jump party_menu_scene

    call screen manageEquip

    jump manage_equip_label
    return

label manage_skills_label:

    $ selected_character = None
    $ selected_skill = None
    $ selected_target = None
    call screen select_character

    if selected_character == None:
        jump party_menu_scene

    call screen manageSkills


    jump manage_skills_label
    return

label manage_inventory_label:

    $ selected_character = None
    $ selected_item = None
    $ ipower = 0
    $ useitem_returnmessage = ""
    call screen manageInventory

    jump party_menu_scene

    label .useitemonchar:
    call screen select_character
    
    if selected_character == None:
        jump manage_inventory_label
    
    label .useitem_nochar:
    $ useItem(selected_item, selected_character)

    $ renpy.say(None, useitem_returnmessage)

    jump manage_inventory_label

    return

$ selected_slot = ""
label manage_equip_slot_label:

    $ equiplist = []
    $ fetchEquip(selected_slot)

    call screen manageEquip

    jump manage_equip_label
    return


label dgplayermap_label:

    call screen dungeon_playermap

    return

label dungeon_label:
    
    $ party_coord = [1, 1]
    $ party_facing = 2
    $ exploring = True
    $ danger = 0

    if hour >= 18 or hour <=5:
        scene bg Dungeon at scenerydark with dissolve
    else:
        scene bg Dungeon at scenery with dissolve


    label .screen:
    show screen dungeon_danger
    show screen dungeon_explore
    $ getMap()
    call screen dungeon_command

    jump dungeon_label.screen

default charinit = None
default in_combat = False
label combat_label:

    # scene transition for battle
    $ battlecommand = None
    $ charinit = None
    $ randomenemies()
    $ rollinitiative()
    $ in_combat = True
    $ selected_item = None
    $ selected_character = None
    $ selected_skill = None

    show bg at blur

    hide screen dungeon_danger
    hide screen dungeon_explore
    show screen initiative_screen
    show screen combat_log
    show screen combat_screen
    # call screen combat_command

    $ logText("\nEnemies have appeared!")
    pause(1.0)

    $ rounds = 0
    while in_combat:
        $ rounds += 1

        python: # Rounds code
            if not opposition: # Combat is Won
                in_combat = False

            for n in initiative: # Combat Turns
                if n.hp > 0 and opposition:
                    logText(f"\nIt's {n.name}'s turn!")

                if n in opposition and n.hp > 0: # Enemy's Turn

                    if len(n.effects) > 0:
                        for effect in n.effects:
                            tickEffect(n)

                    enemyTurn(n)
                    renpy.pause(1.0)

                    if gameover(party):
                        renpy.pause(1.0)
                        in_combat = False
                        renpy.jump("gameover_label")

                
                elif n in party: # Player Character's Turn
                    n.acted = False
                    n.defending = False
                    charinit = n
                    battlecommand = None
                    if not opposition:
                        pass
                    elif n.hp <= 0:
                        pass
                    else:

                        if len(n.effects) > 0:
                            effect_keys = list(n.effects.keys())
                            for effect in effect_keys:
                                tickEffect(n)

                        while n.acted == False:
                            
                            if len(n.effects) > 0:
                                logText("Active Effects:")
                                effect_keys = list(n.effects.keys())
                                for effect in effect_keys:
                                    logText(f"{effect.upper()}: turns left: {n.effects[effect][1]}")

                            renpy.call_screen("combat_command")
                            renpy.pause(0.5)

                # endofturncleanup()

            if gameover(party):
                in_combat = False
                renpy.jump("gameover_label")

            endofturncleanup()
        
        $ steps += 1

    hide screen initiative_screen
    hide screen combat_log
    hide screen combat_screen
    $ charinit = None

    if hour >= 18 or hour <=5:
        show bg at unblurdark
    else:
        show bg at unblur

    $ combatCleanup()

    call combresults from _call_combresults

    return # Returns to previous label/scene


label combresults:

    $ resultstext = ""
    # $ calcRewards()
    $ resultstext = f"You won the combat in {rounds} rounds!\nThe party gains {combat_money} Cr and each living party member receives {int(combat_exp)} experience."

    call screen combat_results with dissolve
    # call screen combat_results with dissolve
    
    $ rounds = 0
    $ combat_money = 0
    $ combat_exp = 0
    python:
        for n in party:
            # class_choice = pickClass(char.char_class)
            chartolevel = n
            checkLevel(n)
    
    return

label levelup_label:
    python:
        for char in party:
            # class_choice = char.char_class
            chartolevel = char
            char.exp += 1500
            checkLevel(char)
    return

label gameover_label:

    "The whole party has perished."

    hide screen initiative_screen
    hide screen combat_log
    hide screen combat_screen
    hide screen combat_command

    "Game Over."

    scene black with dissolve
    $ renpy.block_rollback()
    call screen main_menu with dissolve


label mapmaker_label:

    screen black

    call screen mapmaker_screen

    jump town_scene
##    