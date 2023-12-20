# create dice rolling functions
# create a turn based combat system
init 3 python:
    import math
    import time
    import random
    import copy

    cclasses = character_classes

    """ 0: Phys
        1: fire
        2: wind
        3: earth
        4: ice
        5: thunder
        6: toxic
    """

    elem = ["phys","fire","wind","earth","ice","thunder","toxic","decay","chaos","death"]

    atkmod = 0
    d100 = 0
    dmgdice = 0
    damage = 0
    miss = False
    enemytarget = None
    chartarget = None
    charcommand = None
    rounds = 0
    atk_report = ""


    def rollattack(char,target):
        global atk_report
        global atkmod
        global d100
        global miss
        miss = False
        d100 = random.randint(1,100)

        if d100 >= 90 * abs((math.sqrt(int(char.lck))/100)-(math.sqrt(int(char.agi))/100)+1):
            logText(f"Miss!")
            atkmod = 0
            miss = True

        else:
            if d100 <= int(char.lck)/2 + int(char.agi)/4:
                logText(f"Critical Hit! ({round(1.5 + (int(char.lck)/100),1)}x damage)")
                atkmod = 1.5 + (int(char.lck)/100)
            else:
                atkmod = 1

        atk_report += f"atkmod {atkmod}, "
        return atkmod

    def rolldamage(char):
        global atk_report
        rolleddamage = 0
        for _ in range(int(char.str)):
            if char.dmg == 1:
                rolleddamage += random.randint(1,4) # 1d4 / AVG 2,5
            elif char.dmg == 2:
                rolleddamage += random.randint(1,6) # 1d6 / AVG 3,5
            elif char.dmg == 3:
                rolleddamage += random.randint(1,8) # 1d8 / AVG 4,5
            elif char.dmg == 4:
                rolleddamage += random.randint(2,12) # 2d6 / AVG 7
            elif char.dmg == 5:
                rolleddamage += random.randint(2,16) # 2d8 / AVG 9
            elif char.dmg == 6:
                rolleddamage += random.randint(2,20) # 2d10 / AVG 11
            elif char.dmg == 7:
                rolleddamage += random.randint(3,24) # 3d8 / AVG 13,5
            elif char.dmg == 8:
                rolleddamage += random.randint(3,30) # 3d10 / AVG 16,5
            elif char.dmg == 9:
                rolleddamage += random.randint(3,36) # 3d12 / AVG 19,5
            elif char.dmg >= 10:
                rolleddamage += random.randint(4,40) # 4d10 / AVG 22


        rolleddamage = rolleddamage
        atk_report += f"Rolled dmg {rolleddamage}, "
        return rolleddamage

    def attackfunc(attacker,target):
        global opptoremove
        global atk_report
        atk_report = ""
        rollattack(attacker,target)

        atk_report += f"Attacker STR: {attacker.str} (Sqrd. {round(math.sqrt(attacker.str))}), "
        atk_report += f"Defender VIT {target.vit} (Sqrd. {abs(round(math.sqrt(target.vit)/10-1))}), "

        finaldamage = round((((rolldamage(attacker)) * atkmod) * (math.sqrt(attacker.str)/10+1) + attacker.str) * abs(math.sqrt(target.vit)/10-1))
        
        atk_report += f"\nFinal calc'd damaged: {finaldamage} dealt by {attacker.name}."

        if miss == True:
            finaldamage = 0

        if finaldamage > 0:
            if "phys" in target.weak:
                finaldamage = round(finaldamage * 1.5)
                logText (f"{attacker.name} attacks {target.name}, who's weak to Physical attacks for {finaldamage} damage!")

            elif "phys" in target.resist:
                finaldamage = int(finaldamage * 0.5)
                logText (f"{attacker.name} attacks {target.name}, who's resistant to Physical attacks for {finaldamage} damage!")

            elif target.defending == True:
                finaldamage = finaldamage // 2
                logText (f"{attacker.name} attacks {target.name}, but they defended and suffered only {finaldamage} damage.")

            else:
                logText (f"{attacker.name} attacks {target.name} for {finaldamage} damage.")

            if "protect" in target.effects:
                finaldamage = int (finaldamage * ( 1 - target.effects["protect"][0] * 0.05 ) )
                logText (f"But! {target.name} was protected and suffered only {finaldamage} damage.")

            target.hp -= finaldamage
            if target.hp <= 0 and target in party:
                logText (f"{target.name} has been downed!")
                target.hp = 0
        

        elif finaldamage <= 0:
            logText (f"{attacker.name} attacks {target.name}, but causes no damage.")

        if target.hp <= 0 and target in opposition:
            opposition.remove(target)
            opptoremove.append(target)
            logText (f"{attacker.name} defeated {target.name}!")


        # end of function

    def usetp(char,tp):
        if char.tp < tp:
            cancast = False
            logText (f"Insufficient TP for {char.name} to use this skill.")
        else:
            char.tp -= tp
            cancast = True
        return cancast

    def calcspelldamage(char,spelllevel):
        global spelldamage
        spelldamage = 0
        if spelllevel == "weak":
            for _ in range(int(char.tec)):
                spelldamage += random.randint(2,4) # 2d2 / AVG 3
        elif spelllevel == "medium":
            for _ in range(int(char.tec)):
                spelldamage += random.randint(4,8) # 4d2 / AVG 6
        elif spelllevel == "heavy":
            for _ in range(int(char.tec)):
                spelldamage += random.randint(6,12) # 6d2 / AVG 9

    def calcspellheal(char,spelllevel):
        spellheal = 0
        if spelllevel == "weak":
            spellheal = 25 * (math.sqrt(int(char.tec))/10+1)
        elif spelllevel == "medium":
            spellheal = 50 * (math.sqrt(int(char.tec))/10+1)
        elif spelllevel == "heavy":
            spellheal = 100

        return spellheal

    def spellversion(char,spell):
        starget = None
        dmgtype = ""

        if "firo" in spell:
            dmgtype = "fire"
        elif "gelo" in spell:
            dmgtype = "ice"
        elif "gale" in spell:
            dmgtype = "wind"
        elif "tera" in spell:
            dmgtype = "earth"
        elif "volt" in spell:
            dmgtype = "thunder"
        elif "veno" in spell:
            dmgtype = "toxic"
        elif "nuke" in spell:
            dmgtype = chaos

        if "cura" not in spell and "revita" not in spell and any(element in spell for element in ["firo", "gelo", "gale", "tera", "volt", "veno", "nuke"]):

            if "mor" in spell and spell in char.slist:
                if "grun" in spell and spell in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        calcspelldamage(char,"medium")
                        usespell(char,starget,dmgtype,"multi")

                elif spell in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        starget = targetenemy()
                        if starget is not None:
                            calcspelldamage(char,"medium")
                            usespell(char,starget,dmgtype,"single")


            elif "matha" in spell and spell in char.slist:
                if "grun" in spell and "grun" in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        calcspelldamage(char,"heavy")
                        usespell(char,starget,dmgtype,"multi")

                elif spell in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        starget = targetenemy()
                        if starget is not None:
                            calcspelldamage(char,"heavy")
                            usespell(char,starget,dmgtype,"single")

            elif "mor" not in spell and "matha" not in spell and "cura" not in spell:
                if "grun" in spell and spell in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        calcspelldamage(char,"weak")
                        usespell(char,starget,dmgtype,"multi")


                elif spell in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        starget = targetenemy()
                        if starget is not None:
                            calcspelldamage(char,"weak")
                            usespell(char,starget,dmgtype,"single")


        elif "cura" in spell:
            if "cura" in spell and "mor" in spell:
                if "grun" in spell and spell in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        heal = calcspellheal(char,"medium")
                        for n in party:
                            # healally function
                            healally(char,n,heal)


                else:
                    if usetp(char,char.slist[spell][2]) == True:
                        starget = targetally()
                        if starget is not None:
                            heal = calcspellheal(char,"medium")
                            healally(char,starget,heal)
                pass

            elif "cura" in spell and "matha" in spell:
                if "grun" in spell and spell in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        heal = calcspellheal(char,"heavy")
                        for n in party:
                            # healally function
                            healally(char,n,heal)


                else:
                    if usetp(char,char.slist[spell][2]) == True:
                        starget = targetally()
                        if starget is not None:
                            heal = calcspellheal(char,"heavy")
                            healally(char,starget,heal)
                pass

            elif "cura" in spell:
                if "grun" in spell and spell in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        heal = calcspellheal(char,"weak")
                        for n in party:
                            # healally function
                            healally(char,n,heal)


                else:
                    if usetp(char,char.slist[spell][2]) == True:
                        starget = targetally()
                        if starget is not None:
                            heal = calcspellheal(char,"weak")
                            healally(char,starget,heal)


        elif "revita" in spell:
            
            if "revita" in spell and "mor" not in spell and "motha" not in spell:
                if spell in char.slist:
                    
                    if usetp(char,char.slist[spell][2]) == True:
                        starget = targetdeadally()
                        if starget is not None:
                            starget.hp += round((starget.maxhp*30/100))

                            logText (f"{starget.name} has been revived with {round(starget.maxhp*30/100)} HP!")
                            char.acted = True

            elif "revita" in spell and "mor" in spell:
                if spell in char.slist:

                    if usetp(char,char.slist[spell][2]) == True:
                        starget = targetdeadally()
                        if starget is not None:
                            starget.hp += round((starget.maxhp*60/100))

                            logText (f"{starget.name} has been revived with {round(starget.maxhp*60/100)} HP!")
                            char.acted = True

            elif "revita" in spell and "motha" in spell:
                
                if spell in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        starget = targetdeadally()
                        if starget is not None:
                            starget.hp = round((starget.maxhp))

                            logText (f"{starget.name} has been revived with full HP!")
                            char.acted = True




    ## Logic
    cancelterms = ["no","back","cancel","return","quit"]

    def healally(char, n, heal):
        if n.hp > 0:
            n.hp += round((n.maxhp*heal/100))

            logText (f"{n.name} has been healed for {round(n.maxhp*heal/100)}")

            if n.hp > n.maxhp:
                n.hp = n.maxhp
        else:
            logText(f"No effect on {n.name}")

        char.acted = True

    def usespell(char,starget,dmgtype,spelltype):
        global spelldamage
        global opptoremove
        defeatedopp = []
        defeatedparty = []

        if spelltype == "single":
            dealspelldamage(char,starget,dmgtype,spelldamage)
            if starget.hp <= 0:
                if starget in opposition:
                    opposition.remove(starget)
                    opptoremove.append(starget)
                    logText (f"{char.name} defeated {starget.name}!")


        elif spelltype == "multi":
            if char in party:
                for n in opposition:
                    dealspelldamage(char,n,dmgtype,spelldamage)
                    if n.hp <= 0:
                        defeatedopp.append(n)
            elif char in opposition:
                for n in party:
                    dealspelldamage(char,n,dmgtype,spelldamage)
                    if n.hp <= 0:
                        defeatedparty.append(n)
            
            for n in defeatedopp:
                logText (f"{char.name} defeated {n.name}!")
                opposition.remove(n)
                opptoremove.append(n)
                pass
            for n in defeatedparty:
                logText (f"{char.name} defeated {n.name}!")
                pass

        if starget in party:
            if starget.hp <= 0:
                starget.hp = 0
        
        if char in party:
            char.acted = True

    def dealspelldamage(char,starget,dmgtype,spelldamage):

        # Reduce target's TEC from damage
            # (SQRT(TEC) - 1)*-1
        spelldamage = abs(round(spelldamage * (math.sqrt(char.tec)/10+1) * ((math.sqrt(starget.tec)/10-1))))

        # LCK to evade spell
        sd100 = random.randint(1,100)
        
        # spelldamage = round(spelldamage * (math.sqrt(char.tec)/10+1))
        

        if sd100 <= math.sqrt(starget.lck)/100:
            logText (f"{starget.name} managed to avoid the attack!")

        else:
            if dmgtype in starget.weak:
                spelldamage = int (spelldamage * 1.5)
                logText (f"{starget.name} is weak to {dmgtype} and suffered {spelldamage} {dmgtype} damage!")

            elif starget.defending == True:
                spelldamage = spelldamage // 2
                logText (f"{starget.name} was defending and suffered only {spelldamage} {dmgtype} damage.")

            elif dmgtype in starget.resist:
                spelldamage = spelldamage // 1.5
                logText (f"{starget.name} is resistant to {dmgtype} and suffers only {spelldamage} {dmgtype} damage.")

            else:
                logText (f"{starget.name} suffered {spelldamage} {dmgtype} damage.")

            if "protect" in starget.effects:
                spelldamage = int (spelldamage * ( 1 - starget.effects["protect"][0] * 0.05 ) )
                logText (f"But! {starget.name} was protected and suffered only {spelldamage} {dmgtype} damage.")

            if "coating" in starget.effects:
                if dmgtype in ("fire","wind","earth","ice","thunder","toxic","decay","chaos"):
                    spelldamage = int (spelldamage - ( spelldamage * math.sqrt(starget.effects["protect"][0])/10) )
                    logText (f"But! {starget.name} was coated and suffered only {spelldamage} {dmgtype} damage.")

            starget.hp -= spelldamage

        if starget in party and starget.hp <= 0:
            starget.hp = 0

    def gameover(party):
        global isgameover
        isgameover = True
        return all(n.hp == 0 for n in party)

    opptoremove = []
    combat_money = 0
    combat_exp = 0
    

    # Find party level
    def partyLevel():
        plevel = 0
        for n in party:
            plevel += n.level

        plevel = round(plevel / len(party))
        return plevel
        
    def calcenemyexp(enemy):
        global combat_exp
        plevel = partyLevel()

        if "Làidir" in enemy.name:
            combat_exp += round(round(40*enemy.level/plevel) * 10) * enemy.exp
        else:
            combat_exp += round(40*enemy.level/plevel) * enemy.exp

    def endofturncleanup():
        global initiative
        global opptoremove
        global combat_exp
        global combat_money

        for n in opptoremove:
            calcenemyexp(n)
            combat_money += n.money

            if n in initiative:
                initiative.remove(n)

        opptoremove = []

        for char in party:
            if char.char_class == "Decoy" and char.hp <= 0:
                party.remove(char)

    def calcRewards():
        global combat_exp
        global combat_money
        global party_money

        aliveparty = 0
        for n in party:
            if n.hp >0:
                aliveparty += 1

        for n in party:
            if n.hp >0:
                n.exp += combat_exp
        
        party_money += combat_money

        combatCleanup()

    def combatCleanup():
        # Remove Decoys
        for n in party:
            if n.char_class == "Decoy":
                party.remove(n)

            n.effects.clear()

    ## initiative system
    initiative = []
    initnames = []

    def rollinitiative():
        global initiative
        global initnames

        initiative = []
        initdict = {}

        for n in party:
            initroll = random.randint(1,10)+n.agi
            initdict.update({n: initroll})
        for n in opposition:
            initroll = random.randint(1,10)+n.agi
            initdict.update({n: initroll})


        sortedinit = sorted(initdict.items(), key=lambda item: item[1], reverse=True)

        initiative = [item[0] for item in sortedinit]

        renamed_init = renameduplicates(initiative)

        initiative = renamed_init
                    
    def renameduplicates(initlist):
        ids = ["A","B","C","D","E","F"]
        name_counts = {}
        for n in initlist:
            if n not in party:
                name_count = name_counts.get(n.name, 0)
                name_counts[n.name] = name_count + 1
                
                if name_count == 0:
                    n.name = f"{n.name} {ids[name_count]}"
                if name_count > 0:
                    n.name = f"{n.name} {ids[name_count]}"
        
        return initlist

    def randomenemies():
        global opposition
        global bossbattle

        # 10% of boss
        if 'bossbattle' in globals() and bossbattle:
            laidirBattle = 1
        else:
            laidirBattle = random.randint(2,100)

        if laidirBattle > 1:

            # Level adequate enemies
            levelmodifier = random.choice([0.5,1,2,3,4])
            enemygrouplevel = int(partyLevel() * levelmodifier)

            while enemygrouplevel > 0:

                randomenemylevel = partyLevel() + random.randint(-2,2) -1 
                if randomenemylevel < 0:
                    randomenemylevel = 0

                entype = random.choice(["Malla","Sgeu","Diogh","Colt","Adhbah","Grain"])

                enemy_to_add = generateEnemy(entype,randomenemylevel)
                opposition.append(enemy_to_add)
                enemygrouplevel -= enemy_to_add.level

                if len(opposition) >5:
                    break

            if not opposition:
                entype = random.choice(["Malla","Sgeu","Diogh","Colt","Adhbah","Grain"])
                opposition.append(generateEnemy(entype,partyLevel()))
                
        
        else:
            logText("A Làidir has appeared!")
            opposition.append(generateEnemy("Laidir",partyLevel()))

        bossbattle = False

    dioghtarget = None

    def enemyTurn(enemy):
        global enemytarget
        global dioghtarget
        
        choice = None
        enemytarget = None
        dmgtype = None
        
        if "Diogh" in enemy.name:
            if not dioghtarget:

                while enemytarget == None or enemytarget.hp == 0 or dioghtarget.hp == 0:
                    enemytarget = random.choice(party)
                    logText (f"{enemy.name} seems fixated on {enemytarget.name}...")
                    dioghtarget = enemytarget
            else:
                enemytarget = dioghtarget

        # TARGET
        party_targets = []
        party_weights = []
        while enemytarget == None or enemytarget.hp == 0:
            for char in party:
                if char.hp > 0:
                    party_targets.append(char)
                    party_weights.append(char.threat)
            enemytarget = random.choices(party_targets, weights = party_weights, k=1)[0]

        # PHYS OR ELEM?
        physweight = enemy.str
        elemweight = enemy.tec
        enemychoices = ["phys","elem","aoeelem"]

        # THESE will NEVER attack physically
        if "Adhbah" in enemy.name or "Grain" in enemy.name:
            # choice = random.choices(["elem","aoeelem"], weights=[2,1], k=1)[0]
            physweight = 0
        # THESE will NEVER cast spells
        elif "Malla" in enemy.name or "Sgeu" in enemy.name or "Diogh" in enemy.name:
            elemweight = 0
        

        choice = random.choices(enemychoices, weights=[physweight,elemweight,elemweight/2], k=1)[0]

        if choice == "phys":
            attackfunc(enemy,enemytarget)

        elif choice == "elem":
            if enemy.level < 6:
                spelllevel = "weak"
                enemy.tp -= 4
            elif enemy.level < 12 :
                spelllevel = "medium"
                enemy.tp -= 7
            

            if enemy.tp < 0:
                logText(f"{enemy.name} tried to use a technique, but couldn't focus.")
                attackfunc(enemy,enemytarget)
            else:
                if len(enemy.resist) != 0:
                    dmgtype = random.choice(enemy.resist)
                else:
                    while dmgtype in enemy.weak or dmgtype == None:
                        dmgtype = elem[random.randint(1,6)]

                calcspelldamage(enemy,spelllevel)
                usespell(enemy,enemytarget,dmgtype,"single")

        elif choice == "aoeelem":
        
            if enemy.level < 6:
                spelllevel = "weak"
                enemy.tp -= 10
            elif enemy.level < 12 :
                spelllevel = "medium"
                enemy.tp -= 16

            if enemy.tp < 0:
                logText(f"{enemy.name} tried to use a technique, but couldn't focus.")
                attackfunc(enemy,enemytarget)
            else:
                if len(enemy.resist) != 0:
                    dmgtype = random.choice(enemy.resist)
                else:
                    while dmgtype in enemy.weak or dmgtype == None:
                        dmgtype = elem[random.randint(1,6)]
                    

                calcspelldamage(enemy,spelllevel)
                usespell(enemy,enemytarget,dmgtype,"multi")

        
        pass
         

# RENPY COMMANDS

    def escapeCommand(char):
        chance = 30 + char.agi
        escaped100 = random.randint(1,100)

        if escaped100 <= chance:
            opposition.clear()
            
            logText (f"The group escapes!")
            char.acted = True

        else:
            logText (f"Failed to escape.")
            char.acted = True
            pass


    def skillCommand(char, spell, target):
        dmgtype = ""

        if "firo" in spell:
            dmgtype = "fire"
        elif "gelo" in spell:
            dmgtype = "ice"
        elif "gale" in spell:
            dmgtype = "wind"
        elif "tera" in spell:
            dmgtype = "earth"
        elif "volt" in spell:
            dmgtype = "thunder"
        elif "veno" in spell:
            dmgtype = "toxic"
        elif "nuke" in spell:
            dmgtype = chaos

        if "cura" not in spell and "revita" not in spell and any(element in spell for element in ["firo", "gelo", "gale", "tera", "volt", "veno", "nuke"]):

            if "mor" in spell and spell in char.slist:
                if "grun" in spell and spell in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        calcspelldamage(char,"medium")
                        usespell(char,target,dmgtype,"multi")

                        char.acted = True


                elif spell in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        if target is not None:
                            calcspelldamage(char,"medium")
                            usespell(char,target,dmgtype,"single")

                            char.acted = True


                pass

            elif "matha" in spell and spell in char.slist:
                if "grun" in spell and "grun" in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        calcspelldamage(char,"heavy")
                        usespell(char,target,dmgtype,"multi")

                        char.acted = True



                elif spell in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        if target is not None:
                            calcspelldamage(char,"heavy")
                            usespell(char,target,dmgtype,"single")

                            char.acted = True

            elif "mor" not in spell and "matha" not in spell and "cura" not in spell:
                if "grun" in spell and spell in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        calcspelldamage(char,"weak")
                        usespell(char,target,dmgtype,"multi")

                        char.acted = True


                elif spell in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        if target is not None:
                            calcspelldamage(char,"weak")
                            usespell(char,target,dmgtype,"single")

                            char.acted = True

        elif "cura" in spell:
            if "cura" in spell and "mor" in spell:
                if "grun" in spell and spell in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        heal = calcspellheal(char,"medium")
                        for n in party:
                            # healally function
                            healally(char,n,heal)
                        
                        char.acted = True


                else:
                    if target is not None and target.hp < target.maxhp:
                        if usetp(char,char.slist[spell][2]) == True:
                            heal = calcspellheal(char,"medium")
                            healally(char,target,heal)

                            char.acted = True


            elif "cura" in spell and "matha" in spell:
                if "grun" in spell and spell in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        heal = calcspellheal(char,"heavy")
                        for n in party:
                            # healally function
                            healally(char,n,heal)

                        char.acted = True

                else:
                    if target is not None and target.hp < target.maxhp:
                        if usetp(char,char.slist[spell][2]) == True:
                            heal = calcspellheal(char,"heavy")
                            healally(char,target,heal)

                            char.acted = True
                pass

            elif "cura" in spell:
                if "grun" in spell and spell in char.slist:
                    if usetp(char,char.slist[spell][2]) == True:
                        heal = calcspellheal(char,"weak")
                        for n in party:
                            # healally function
                            healally(char,n,heal)
                        
                        char.acted = True


                else:
                    if target is not None and target.hp < target.maxhp:
                        if usetp(char,char.slist[spell][2]) == True:
                            heal = calcspellheal(char,"weak")
                            healally(char,target,heal)

                            char.acted = True

        elif "revita" in spell:
            
            if "revita" in spell and "mor" not in spell and "motha" not in spell:
                if spell in char.slist:
                    
                    if target is not None and target.hp <= 0:
                        if usetp(char,char.slist[spell][2]) == True:
                            target.hp += round((target.maxhp*30/100))

                            logText (f"{target.name} has been revived with {round(target.maxhp*30/100)} HP!")
                            char.acted = True

            elif "revita" in spell and "mor" in spell:
                if spell in char.slist:

                    if target is not None and target.hp <= 0:
                        if usetp(char,char.slist[spell][2]) == True:
                            target.hp += round((target.maxhp*60/100))

                            logText (f"{target.name} has been revived with {round(target.maxhp*60/100)} HP!")
                            char.acted = True

            elif "revita" in spell and "motha" in spell:
                
                if spell in char.slist:
                    if target is not None and target.hp <= 0:
                        if usetp(char,char.slist[spell][2]) == True:
                            target.hp = round((target.maxhp))

                            logText (f"{target.name} has been revived with full HP!")
                            char.acted = True

    def skillCommandPhys(char, charcommand, target):

        if "charge" in charcommand:
            if char.hp > round(char.maxhp*0.15):

                if target is not None:

                    char.hp -= round(char.maxhp*0.15)
                    attacktimes = random.randint(1,3)

                    for _ in range (1,attacktimes+1):

                        attackfunc(char,target)

                        if target.hp <= 0:
                            break

                    char.acted = True

        elif "cleave" in charcommand:
            # if char.hp > round(char.maxhp*0.20) and usetp(char,char.slist[charcommand][2]) == True:
            if usetp(char,char.slist[charcommand][2]) == True:
                
                atkmin = math.ceil(char.slist["cleave"][0]/2)
                atkmax = math.floor(char.slist["cleave"][0]/2) + 3
                attacktimes = random.randint(atkmin, atkmax)
                # char.hp -= round(char.maxhp*0.20) # No more HP cost
                # char.tp -= 3

                for _ in range(attacktimes):
                    if opposition:
                        target = random.choice(opposition)
                        attackfunc(char,target)


                        char.acted = True

        elif "hunt" in charcommand:
            if usetp(char,char.slist[charcommand][2]) == True:

                if target is not None:

                    # char.tp -= 5

                    strbonus = (((math.sqrt(target.hp)/10+1) * char.str) - char.str ) * ( 0.7 + 0.3 * math.ceil(char.slist["sneak"][0]//2)) # + 30% every odd level

                    char.str += strbonus
                    attackfunc(char,target)
                    char.str -= strbonus

                    char.acted = True

        elif "sneak" in charcommand:
            if usetp(char,char.slist[charcommand][2]) == True:

                if target is not None:

                    
                    
                    char.str += char.slist["sneak"][0] # STR + Skill level
                    char.dmg += int(math.ceil(char.slist["sneak"][0]/4)) # DMG + 1 / 4 lvls
                    char.lck += 15 + (char.slist["sneak"][0] * 5) # LCK + 15 + 5/lvl
                    
                    attackfunc(char,target)

                    char.str -= char.slist["sneak"][0] # STR - Skill level
                    char.dmg -= int(math.ceil(char.slist["sneak"][0]/4)) # DMG - 1 / 4 lvls
                    char.lck -= 15 + (char.slist["sneak"][0] * 5) # LCK - 15 + 5/lvl

                    char.acted = True
            
        elif "bomb" in charcommand:

            if usetp(char,char.slist["bomb"][2]) == True:
                global opptoremove
                defeatedopp = []
                bombdamage = int( char.slist["bomb"][0] * (math.sqrt(char.lck)/10+1) * 15 ) # Bomb power = 15

                for enemy in opposition:
                    enemy.hp -= bombdamage
                    logText (f"{enemy.name} suffered {bombdamage} explosion damage.")
                    if enemy.hp <= 0:
                            defeatedopp.append(enemy)

                for n in defeatedopp:
                    logText (f"{char.name} defeated {enemy.name}!")
                    opposition.remove(enemy)
                    opptoremove.append(enemy)

                char.acted = True
        
    def skillCommandSupp(char, charcommand, target):
        
        if "protect" in charcommand:

            if usetp(char,char.slist[charcommand][2]) == True:
                for n in party:
                    applyEffect(char,charcommand,n)
                char.acted = True

        elif "taunt" in charcommand:

            if usetp(char,char.slist[charcommand][2]) == True:
                applyEffect(char,charcommand,char)
                char.acted = True

        elif "decoy" in charcommand:

            if usetp(char,char.slist[charcommand][2]) == True:
                
                decoy = Character(
                    name=f"{char.name}'s Decoy", char_class="Decoy", race = None,
                    level=1, maxhp=(25*char.slist["decoy"][0]), hp=(25*char.slist["decoy"][0]), maxtp=0, tp=0,
                    str=0, dmg=0, tec=(2*char.slist["decoy"][0]), vit=(3*char.slist["decoy"][0]), agi=(2*char.slist["decoy"][0]), lck=0,
                    acted=False, defending=False, weak=[], resist=[], exp=0, init=0, skillpts=0, perkpts=0, effects={}, threat=12+(2*char.slist["decoy"][0]),
                    equip={
                    "Weapon":None,
                    "Armor":None,
                    "Accessory 1":None,
                    "Accessory 2":None},
                    slist={}
                    )
                
                for n in party:
                    if n.name == f"{char.name}'s Decoy":
                        party.remove(n)
                party.append(copy.deepcopy(decoy))
                
                char.acted = True

        elif "enha" in charcommand:
            
            if "grun" in charcommand:
                if usetp(char,char.slist[charcommand][2]) == True:
                    for n in party:
                        applyEffect(char, charcommand, n)
                    char.acted = True
            
            else: # Single Ally
                if usetp(char,char.slist[charcommand][2]) == True:
                    applyEffect(char, charcommand, target)
                    char.acted = True

        elif "enfe" in charcommand:
            
            if "grun" in charcommand:
                if usetp(char,char.slist[charcommand][2]) == True:
                    for enemy in opposition:
                        applyEffect(char, charcommand, enemy)
                    char.acted = True

            else: # Single Enemy
                if usetp(char,char.slist[charcommand][2]) == True:
                    applyEffect(char, charcommand, target)
                    char.acted = True

        elif "coating" in charcommand:

            if usetp(char,char.slist[charcommand][2]) == True:
                for n in party:
                    applyEffect(char,charcommand,n)

                char.acted = True

        elif "appraise" in charcommand:

            if usetp(char,char.slist[charcommand][2]) == True:

                target.exp += 0.25 * char.slist["appraise"][0]

                char.acted = True


# RENPY DEFAULTS

default opposition = []
##