init 2 python:

    import math
    import copy
    import random

    ## SKILLS
    global_skill_list = {
        "firo": [1, "Causes weak fire damage to one enemy.", 4],
        "grunfiro": [1, "Causes weak fire damage to all enemies.", 10],
        "firomor": [1, "Causes moderate fire damage to one enemy.", 8],
        "grunfiromor": [1, "Causes moderate fire damage to all enemies.", 16],
        "firomatha": [1, "Causes heavy fire damage to one enemy.", 12],
        "grunfiromatha": [1, "Causes heavy fire damage to all enemies.", 22],
        
        "gelo": [1, "Causes weak ice damage to one enemy.", 4],
        "grungelo": [1, "Causes weak ice damage to all enemies.", 10],
        "gelomor": [1, "Causes moderate ice damage to one enemy.", 8],
        "grungelomor": [1, "Causes moderate ice damage to all enemies.", 16],
        "gelomatha": [1, "Causes heavy ice damage to one enemy.", 12],
        "grungelomatha": [1, "Causes heavy ice damage to all enemies.", 22],

        "gale": [1, "Causes weak wind damage to one enemy.", 4],
        "grungale": [1, "Causes weak wind damage to all enemies.", 10],
        "galemor": [1, "Causes moderate wind damage to one enemy.", 8],
        "grungalemor": [1, "Causes moderate wind damage to all enemies.", 16],
        "galematha": [1, "Causes heavy wind damage to one enemy.", 12],
        "grungalematha": [1, "Causes heavy wind damage to all enemies.", 22],

        "tera": [1, "Causes weak earth damage to one enemy.", 4],
        "gruntera": [1, "Causes weak earth damage to all enemies.", 10],
        "teramor": [1, "Causes moderate earth damage to one enemy.", 8],
        "grunteramor": [1, "Causes moderate earth damage to all enemies.", 16],
        "teramatha": [1, "Causes heavy earth damage to one enemy.", 12],
        "grunteramatha": [1, "Causes heavy earth damage to all enemies.", 22],


        "volt": [1, "Causes weak thunder damage to one enemy.", 4],
        "grunvolt": [1, "Causes weak thunder damage to all enemies.", 10],
        "voltmor": [1, "Causes moderate thunder damage to one enemy.", 8],
        "grunvoltmor": [1, "Causes moderate thunder damage to all enemies.", 16],
        "voltmatha": [1, "Causes heavy thunder damage to one enemy.", 12],
        "grunvoltmatha": [1, "Causes heavy thunder damage to all enemies.", 22],

        "veno": [1, "Causes weak toxic damage to one enemy.", 4],
        "grunveno": [1, "Causes weak toxic damage to all enemies.", 10],
        "venomor": [1, "Causes moderate toxic damage to one enemy.", 8],
        "grunvenomor": [1, "Causes moderate toxic damage to all enemies.", 16],
        "venomatha": [1, "Causes heavy toxic damage to one enemy.", 12],
        "grunvenomatha": [1, "Causes heavy toxic damage to all enemies.", 22],
        
        "cura": [1, "Restores small amount of health to one ally.", 3, "S"],
        "gruncura": [1, "Restores small amount of health to all allies.", 7, "S"],
        "curamor": [1, "Restores moderate amount of health to one ally.", 7, "S"],
        "gruncuramor": [1, "Restores moderate amount of health to all allies.", 12, "S"],
        "curamatha": [1, "Restores full health to one ally.", 18, "S"],
        "gruncuramatha": [1, "Restores full health to all allies.", 30, "S"],
        
        "revita": [1, f"Revives one fallen ally with 30% of HP.", 10, "S"],
        "revitamor": [1, f"Revives one fallen ally with 60% of HP.", 18, "S"],
        "revitamatha": [1, f"Revives one fallen ally with full HP.", 30, "S"],
        
        "enhast": [1, "Enhances STR for one ally.", 6, "S"],
        "grunenhast": [1, "Enhances STR for all allies.", 15, "S"],
        "enhate": [1, "Enhances TEC for one ally.", 6, "S"],
        "grunenhate": [1, "Enhances TEC for all allies.", 15, "S"],
        "enhavi": [1, "Enhances VIT for one ally.", 6, "S"],
        "grunenhavi": [1, "Enhances VIT for all allies.", 15, "S"],
        "enhagi": [1, "Enhances AGI for one ally.", 6, "S"],
        "grunenhagi": [1, "Enhances AGI for all allies.", 15, "S"],
        "enhalk": [1, "Enhances LCK for one ally.", 6, "S"],
        "grunenhalk": [1, "Enhances LCK for all allies.", 15, "S"],

        "enfest": [1, "Enfeebles STR for one enemy.", 8, "S"],
        "grunenfest": [1, "Enfeebles STR for all enemies.", 20, "S"],
        "enfete": [1, "Enfeebles TEC for one enemy.", 8, "S"],
        "grunenfete": [1, "Enfeebles TEC for all enemies.", 20, "S"],
        "enfevi": [1, "Enfeebles VIT for one enemy.", 8, "S"],
        "grunenfevi": [1, "Enfeebles VIT for all enemies.", 20, "S"],
        "enfegi": [1, "Enfeebles AGI for one enemy.", 8, "S"],
        "grunenfegi": [1, "Enfeebles AGI for all enemies.", 20, "S"],
        "enfelk": [1, "Enfeebles LCK for one enemy.", 8, "S"],
        "grunenfelk": [1, "Enfeebles LCK for all enemies.", 20, "S"],

        "appraise": [1, "Increases EXP gain for slain enemies.", 20,"S"],
        "bomb": [1, "Causes nuke damage to all enemies.", 10],
        "coating": [1, "Grants elemental resistance to allies.", 10, "S"],

        "protect": [1, "Protects party from incoming damage.", 5, "S"],
        "decoy": [1, "Creates a decoy to divert attacks from party.", 15, "S"],
        "taunt": [1, "Draw enemy attacks and increases own defense.", 8, "S"],

        ### PHYS SKILLS

        # "charge": [1, "Attacks one enemy up to three times.", 0, 15],
        "cleave": [1, "Attacks random enemies multiple (1-3) times.", 5, 0],
        
        "sneak": [1, "Attacks one enemy with increased damage and crit rate.", 6, 0],
        "hunt": [1, "Attacks one enemy with increased damage the more HP it has.", 15, 0],
    }


    # Characters

    class Character:
        def __init__(self,name,char_class,race,level,maxhp,hp,maxtp,tp,str,dmg,tec,vit,agi,lck,slist,acted,defending,weak,resist,equip,exp,init,skillpts,perkpts, effects, threat):
            self.name = name
            self.char_class = char_class
            self.race = race
            self.level = level
            self.maxhp = maxhp
            self.hp = hp
            self.maxtp = maxtp
            self.tp = tp
            self.str = str
            self.dmg = dmg
            self.tec = tec
            self.vit = vit
            self.agi = agi
            self.lck = lck
            self.slist = slist
            self.acted = acted
            self.defending = defending
            self.weak = weak
            self.resist = resist
            self.equip = equip
            self.exp = exp
            self.skillpts = skillpts
            self.perkpts = perkpts
            self.init = init
            self.effects = effects
            self.threat = threat

    # Class Enemy:

    class CharacterClass:
        def __init__(self,name,hp,tp,str,dmg,tec,vit,agi,lck,special,improv,lore):
            self.name = name
            self.hp = hp
            self.tp = tp
            self.str = str
            self.dmg = dmg
            self.tec = tec
            self.vit = vit
            self.agi = agi
            self.lck = lck
            self.special = special
            self.improv = improv
            self.lore = lore

    class CharacterRace:
        def __init__(self, name, bonus, hiddenbonus, lore):
            self.name = name
            self.bonus = bonus
            self.hiddenbonus = hiddenbonus
            self.lore = lore

    # CHARACTER CLASSES
    knight = CharacterClass(
        name = "Knight",
        hp = 10,
        tp = 2,
        str = 6,
        dmg = 2,
        tec = 2,
        vit = 5,
        agi = 2,
        lck = 3,
        improv = [4/3, 1/2, 1, 1/3, 1, 3/5, 1/3, 1/6],
        special = None,
        lore = "A capable fighter with high attack and defense, know a few combat tactics, but doesn't excels in special techniques.")
    thaumaturge = CharacterClass(
        "Thaumaturge",
        hp = 6,
        tp = 5,
        str = 4,
        dmg = 1,
        tec = 6,
        vit = 2,
        agi = 2,
        lck = 4,
        improv = [2/3, 1, 2/3, 1, 2/3, 2/5, 2/3, 1/10],
        special = None,
        lore = "A capable combatant who's reliable in physical combat, but really excells at support and healing.")
    arcanist = CharacterClass(
        "Arcanist",
        hp = 4,
        tp = 7,
        str = 2,
        dmg = 1,
        tec = 8,
        vit = 1,
        agi = 4,
        lck = 2,
        improv = [1/3, 3/2, 1/4, 3/2, 1/3, 2/3, 1/2, 1/15],
        special = None,
        lore = "A specialist combatant, really weak and fragile, but can use devastating special techniques and elemental attacks.")
    scout = CharacterClass(
        "Scout",
        hp = 6,
        tp = 2,
        str = 5,
        dmg = 2,
        tec = 2,
        vit = 2,
        agi = 6,
        lck = 6,
        improv = [1/2, 1/3, 1/2, 1/2, 1/2, 3/2, 4/3, 1/8],
        special = None,
        lore = "A stealthy combatant, somewhat weak and fragile, but capable of landing powerful critical attacks more frequently than others.")
    herald = CharacterClass(
        "Herald",
        hp = 6,
        tp = 3,
        str = 4,
        dmg = 1,
        tec = 4,
        vit = 3,
        agi = 4,
        lck = 4,
        improv = [3/4, 2/3, 1, 3/4, 2/3, 2/3, 2/3, 1/8],
        special = None,
        lore = "A well-rounded combatant and explorer, able to use offensive and support abilities, but doesn't really excels in any.")
    quartermaster = CharacterClass(
        "Quartermaster",
        hp = 6,
        tp = 3,
        str = 4,
        dmg = 1,
        tec = 1,
        vit = 4,
        agi = 5,
        lck = 5,
        improv = [1, 1/4, 1, 1/3, 1, 1/2, 1, 1/6],
        special = None,
        lore = "A supportive combatant, not very powerful in combat, but able to make exploration easier with many support skills.")

    character_classes = [knight,thaumaturge,arcanist,scout,herald,quartermaster]

    # CHARACTER RACES
    r_human = CharacterRace(
        name = "Human", bonus = "+1 AGI, +1 LCK", hiddenbonus = "+1 to Random stat every even level",
        lore = "The most varied species in the kingdoms. They can do almost literaly everything, but it's hard to pinpoint any one human's talents.")
    r_dwarf = CharacterRace(
        name = "Dwarf", bonus = "+10 Max HP", hiddenbonus = "+3 Max HP / Level",
        lore = "Short and Stout, Dwarves are very resilient and won't go down easily, which is why despite their short stature, they're usually found in the frontlines.")
    r_orc = CharacterRace(
        name = "Orc", bonus = "+1 DMG", hiddenbonus = "+1 DMG every 5 levels.",
        lore = "Orcs can channel a mighty strenght from their naturaly strong bodies, which allows them to hit harder and cause more physical damge.")
    r_faefolk = CharacterRace(
        name = "Faefolk", bonus = "+10 TP", hiddenbonus = "+1 Max TP / Level",
        lore = "Elves, Centaurs, Satyrs, Duendes, and other such creatures constitues the Faefolk, they have a natural penchant for magic, which comes easily for them.")
    r_dragonkin = CharacterRace(
        name = "Dragonkin", bonus = "+2 STR", hiddenbonus = "+1 STR or TEC every even level",
        lore = "Tall and imposing, Dragonkin are naturaly strong and resilient to magic, which is why they really shine in the frontlines of combat.")
    r_beastfolk = CharacterRace(
        name = "Beastfolk", bonus = "+1 VIT, +1 AGI", hiddenbonus = "+1 AGI or LCK every even level",
        lore = "Animal folk are many and varied, but their animalistic features makes them more resilient and faster than most other races.") 
    r_tiefling = CharacterRace(
        name = "Tiefling", bonus = "+2 TEC", hiddenbonus = "+1 TEC or +1 Max TP every even level",
        lore = "These humanoids with an infernal heritage have demonic features, but also higher magical resistence and a natural inclination for magical studies.")
    r_lizardfolk = CharacterRace(
        name = "Lizardfolk", bonus = "+1 STR, +1 TEC", hiddenbonus = "+1 TEC or +1 STR every even level",
        lore = "These reptilian humanoids have are imposing and intimidating due to their physique, and also naturally atuned to the elements.")

    character_races = [r_human,r_dwarf,r_orc,r_faefolk,r_dragonkin,r_beastfolk,r_tiefling,r_lizardfolk]

    # previously defined characters

    charTemplate = Character(
        name="Name", char_class="Class", race = None,
        level=1, maxhp=10, hp=10, maxtp=10, tp=10,
        str=1, dmg=1, tec=1, vit=1, agi=1, lck=1,
        acted=False, defending=False, weak=[], resist=[], exp=0, init=0, skillpts=0, perkpts=0,effects={},
        equip={
        "Weapon":None,
        "Armor":None,
        "Accessory":None,
        "Charm":None},
        slist={}, threat=10)


    # previously defined character roster

    elem = ["phys","fire","wind","earth","ice","thunder","toxic","decay","chaos","death"]

    # previously defined Party and Party_money

    cancelterms = ["no","back","cancel","return","quit"]

    character_roster = []
    party = []
    party_money = 100



# RENPY FUNCITONS

    exptolevel = 1000 # EXP TO LEVEL UP
    def checkLevel(char):

        while char.exp >= char.level * exptolevel: # *1.5
            levelUpChar(char)

    def pickClass(cname):
        for n in character_classes:
            if n == cname:
                return n

    def removeFromParty(char):
        character_roster.append(char)
        party.remove(char)

    def addToParty(char):
        if len(party) < 4:
            party.append(char)
            character_roster.remove(char)

    def createCharacterRpy(newname, newrace, newclass, newelement):
        global party_money
        party_money -= 10

        if newname == "":
            if newclass == arcanist:
                newname = random.choice(["Sage","Weaver","Mage","Runesmith", "Arcanist"])
            elif newclass == thaumaturge:
                newname = random.choice(["Nomad","Attune","Seer","Whisper", "Thaumaturge"])
            elif newclass == herald:
                newname = random.choice(["Beacon","Singer","Bard","Crier", "Herald"])
            elif newclass == knight:
                newname = random.choice(["Sentinel","Guardian","Tower","Paladin", "Knight"])
            elif newclass == scout:
                newname = random.choice(["Ranger","Stalker","Fleetfoot","Rogue", "Scout"])
            elif newclass == quartermaster:
                newname = random.choice(["Steward","Supplier","Provisioner","Packmule", "Quartermaster"])



        newchar = None
        newchar = Character(
            name = newname, char_class = newclass, race = newrace,
            maxhp = newclass.hp * 10, hp = newclass.hp * 10 , maxtp = newclass.tp * 10, tp = newclass.tp * 10,
            str = newclass.str, dmg = newclass.dmg, tec = newclass.tec, vit = newclass.vit, agi = newclass.agi, lck = newclass.lck,
            acted = False, defending = False, weak = [], resist= [], level = 1, exp = 0, init = 0, skillpts=0, perkpts=0, threat=10,
            equip = {
                "Weapon":weapon1,
                "Armor":armor1,
                "Accessory":None,
                "Charm":None},
            slist = {}, effects = {})
        
        if newchar is not None: # Extra Stats per Race
            if newchar.race == r_human:
                newchar.lck += 1
                newchar.agi += 1

            elif newchar.race == r_dwarf:
                newchar.maxhp += 10
                newchar.hp += 10

            elif newchar.race == r_orc:
                newchar.dmg += 1
            
            elif newchar.race == r_faefolk:
                newchar.maxtp += 10
                newchar.tp += 10

            elif newchar.race == r_dragonkin:
                newchar.str += 2

            elif newchar.race == r_beastfolk:
                newchar.vit += 1
                newchar.agi += 1
            
            elif newchar.race == r_tiefling:
                newchar.tec += 2

            elif newchar.race == r_lizardfolk:
                newchar.str += 1
                newchar.tec += 1
                
        if newchar is not None: # Extra Skills per Class

            if newchar.char_class == arcanist:

                if newelement == "fire":
                    newchar.slist["firo"] = global_skill_list["firo"].copy()

                if newelement == "ice":
                    newchar.slist["gelo"] = global_skill_list["gelo"].copy()

                if newelement == "wind":
                    newchar.slist["gale"] = global_skill_list["gale"].copy()

                if newelement == "earth":
                    newchar.slist["tera"] = global_skill_list["tera"].copy()

                if newelement == "thunder":
                    newchar.slist["volt"] = global_skill_list["volt"].copy()

                if newelement == "toxic":
                    newchar.slist["veno"] = global_skill_list["veno"].copy()

                newchar.slist["enhate"] = global_skill_list["enhate"].copy()
                newchar.slist["enfete"] = global_skill_list["enfete"].copy()
                
            if newchar.char_class == thaumaturge:
                
                if newelement == "wind":
                    newchar.slist["gale"] = global_skill_list["gale"].copy()

                if newelement == "earth":
                    newchar.slist["tera"] = global_skill_list["tera"].copy()

                if newelement == "thunder":
                    newchar.slist["volt"] = global_skill_list["volt"].copy()

                newchar.slist["cura"] = global_skill_list["cura"].copy()
                newchar.slist["revita"] = global_skill_list["revita"].copy()
                
            if newchar.char_class == herald:

                if newelement == "fire":
                    newchar.slist["firo"] = global_skill_list["firo"].copy()

                if newelement == "ice":
                    newchar.slist["gelo"] = global_skill_list["gelo"].copy()

                if newelement == "wind":
                    newchar.slist["gale"] = global_skill_list["gale"].copy()

                if newelement == "earth":
                    newchar.slist["tera"] = global_skill_list["tera"].copy()

                if newelement == "thunder":
                    newchar.slist["volt"] = global_skill_list["volt"].copy()

                newchar.slist["cura"] = global_skill_list["cura"].copy()
                newchar.slist["enhast"] = global_skill_list["enhast"].copy()

            if newchar.char_class == knight:

                newchar.slist["taunt"] = global_skill_list["taunt"].copy()
                newchar.slist["cleave"] = global_skill_list["cleave"].copy()
                newchar.slist["protect"] = global_skill_list["protect"].copy()

            if newchar.char_class == scout:
                newchar.slist["sneak"] = global_skill_list["sneak"].copy()
                newchar.slist["hunt"] = global_skill_list["hunt"].copy()
                newchar.slist["decoy"] = global_skill_list["decoy"].copy()

            if newchar.char_class == quartermaster:
                newchar.slist["appraise"] = global_skill_list["appraise"].copy()
                newchar.slist["bomb"] = global_skill_list["bomb"].copy()
                newchar.slist["coating"] = global_skill_list["coating"].copy()

            pass

        # Equip bonus
        newchar.str += 1
        newchar.vit += 1
        newchar.agi += 1

        character_roster.append(copy.deepcopy(newchar))
        return newchar

    descriptor = ""
    def levelUpSkill_Check(char, skill, choice_final):
        global descriptor
        descriptor = ""
        skill_level = char.slist[skill][0]
        if skill in ("firo","tera","gelo","gale","veno","volt","nuke"):
            
            descriptor = (f"{skill.upper()} (Level: {skill_level}) is a skill that causes weak elemental damage.\n")
            if char.char_class == arcanist or char.char_class.name == "Arcanist":
                if char.slist[skill][0] <2:
                    descriptor += (f" At Level 2 you learn GRUN{skill.upper()}, which affects all enemies.\n")
                if char.slist[skill][0] <3:
                    descriptor += (f" At Level 3 you learn {skill.upper()}MOR, which causes medium elemental damage.\n")
                if char.slist[skill][0] <4:
                    descriptor += (f" At Level 4 you learn GRUN{skill.upper()}MOR, which causes medium elemental damage to all enemies.\n")
                if char.slist[skill][0] <5:
                    descriptor += (f" At Level 5 you learn {skill.upper()}MATHA, which causes heavy elemental damage.\n")
                if char.slist[skill][0] <6:
                    descriptor += (f" At Level 6 you learn GRUN{skill.upper()}MATHA, which causes heavy elemental damage to all enemies.")
            elif char.char_class == herald or char.char_class == thaumaturge or char.char_class.name == "Herald" or char.char_class.name == "Thaumaturge":
                if char.slist[skill][0] <3:
                    descriptor += (f" At Level 3 you learn GRUN{skill.upper()}, which affects all enemies.\n")
                if char.slist[skill][0] <4:
                    descriptor += (f" At Level 4 you learn {skill.upper()}MOR, which causes medium elemental damage.\n")
                if char.slist[skill][0] <6:
                    descriptor += (f" At Level 6 you learn GRUN{skill.upper()}MOR, which causes medium elemental damage to all enemies.\n")
                if char.slist[skill][0] <7:
                    descriptor += (f" At Level 7 you learn {skill.upper()}MATHA, which causes heavy elemental damage.\n")
                if char.slist[skill][0] <9:
                    descriptor += (f" At Level 9 you learn GRUN{skill.upper()}MATHA, which causes heavy elemental damage to all enemies.")
            
            
            if choice_final == True:
                if char.skillpts >0:
                    char.slist[skill][0] += 1
                    char.skillpts -= 1

                    if char.char_class == arcanist or char.char_class.name == "Arcanist":
                        if char.slist[skill][0] >= 2:
                            char.slist[f"grun{skill.lower()}"] = global_skill_list[f"grun{skill}"].copy()
                            char.slist[f"grun{skill.lower()}"][0] = char.slist[skill][0]-1
                        if char.slist[skill][0] >= 3:
                            char.slist[f"{skill.lower()}mor"] = global_skill_list[f"{skill}mor"].copy()
                            char.slist[f"{skill.lower()}mor"][0] = char.slist[skill][0]
                        if char.slist[skill][0] >= 4:
                            char.slist[f"grun{skill.lower()}mor"] = global_skill_list[f"grun{skill}mor"].copy()
                            char.slist[f"grun{skill.lower()}mor"][0] = char.slist[skill][0]-1
                        if char.slist[skill][0] >= 5:
                            char.slist[f"{skill.lower()}matha"] = global_skill_list[f"{skill}matha"].copy()
                            char.slist[f"{skill.lower()}matha"][0] = char.slist[skill][0]
                        if char.slist[skill][0] >= 6:
                            char.slist[f"grun{skill.lower()}matha"] = global_skill_list[f"grun{skill}matha"].copy()
                            char.slist[f"grun{skill.lower()}matha"][0] = char.slist[skill][0]-2

                    if char.char_class == herald or char.char_class == thaumaturge or char.char_class.name == "Herald" or char.char_class.name == "Thaumaturge":
                        if char.slist[skill][0] >= 3:
                            char.slist[f"grunfiro"] = global_skill_list[f"grunfiro"].copy()
                            char.slist[f"grun{skill.lower()}"][0] = char.slist[skill][0]-2
                        if char.slist[skill][0] >= 4:
                            char.slist[f"{skill.lower()}mor"] = global_skill_list[f"{skill}mor"].copy()
                            char.slist[f"{skill.lower()}mor"][0] = char.slist[skill][0]
                        if char.slist[skill][0] >= 6:
                            char.slist[f"grun{skill.lower()}mor"] = global_skill_list[f"grun{skill}mor"].copy()
                            char.slist[f"grun{skill.lower()}mor"][0] = char.slist[skill][0]-2
                        if char.slist[skill][0] >= 7:
                            char.slist[f"{skill.lower()}matha"] = global_skill_list[f"{skill}matha"].copy()
                            char.slist[f"{skill.lower()}matha"][0] = char.slist[skill][0]
                        if char.slist[skill][0] >= 9:
                            char.slist[f"grun{skill.lower()}matha"] = global_skill_list[f"grun{skill}matha"].copy()
                            char.slist[f"grun{skill.lower()}matha"][0] = char.slist[skill][0]-2
                    pass


        elif skill in ("cura"):
            
            descriptor = (f"{skill.upper()} (Level: {skill_level}) is a skill that {global_skill_list[skill][1]}\n")
            
            if char.char_class == thaumaturge or char.char_class.name == "Thaumaturge":
                if char.slist[skill][0] <2:
                    descriptor += (f" At Level 2 you learn GRUN{skill.upper()}, which affects all allies.\n")
                if char.slist[skill][0] <3:
                    descriptor += (f" At Level 3 you learn {skill.upper()}MOR, which heals a medium amount of damage.\n")
                if char.slist[skill][0] <4:
                    descriptor += (f" At Level 4 you learn GRUN{skill.upper()}MOR, which heals a medium amount of damage to all allies.\n")
                if char.slist[skill][0] <5:
                    descriptor += (f" At Level 5 you learn {skill.upper()}MATHA, which heals a heavy amount of damage.\n")
                if char.slist[skill][0] <6:
                    descriptor += (f" At Level 6 you learn GRUN{skill.upper()}MATHA, which heals a heavy amount of damage to all allies.")
            elif char.char_class == herald or char.char_class.name == "Herald":
                if char.slist[skill][0] <3:
                    descriptor += (f" At Level 3 you learn GRUN{skill.upper()}, which affects all allies.\n")
                if char.slist[skill][0] <4:
                    descriptor += (f" At Level 4 you learn {skill.upper()}MOR, which heals a medium amount of damage.\n")
                if char.slist[skill][0] <6:
                    descriptor += (f" At Level 6 you learn GRUN{skill.upper()}MOR, which heals a medium amount of damage to all allies.\n")
                if char.slist[skill][0] <7:
                    descriptor += (f" At Level 7 you learn {skill.upper()}MATHA, which heals a heavy amount of damage.\n")
                if char.slist[skill][0] <9:
                    descriptor += (f" At Level 9 you learn GRUN{skill.upper()}MATHA, which heals a heavy amount of damage to all allies.")
            
            
            if choice_final == True:
                if char.skillpts >0:

                    char.slist[skill][0] += 1
                    char.skillpts -= 1

                    if char.char_class == thaumaturge or char.char_class.name == "Thaumaturge":
                        if char.slist[skill][0] >= 2:
                            char.slist[f"grun{skill.lower()}"] = global_skill_list[f"grun{skill}"].copy()
                        if char.slist[skill][0] >= 3:
                            char.slist[f"{skill.lower()}mor"] = global_skill_list[f"{skill}mor"].copy()
                        if char.slist[skill][0] >= 4:
                            char.slist[f"grun{skill.lower()}mor"] = global_skill_list[f"grun{skill}mor"].copy()
                        if char.slist[skill][0] >= 5:
                            char.slist[f"{skill.lower()}matha"] = global_skill_list[f"{skill}matha"].copy()
                        if char.slist[skill][0] >= 6:
                            char.slist[f"grun{skill.lower()}matha"] = global_skill_list[f"grun{skill}matha"].copy()

                    elif char.char_class == herald or char.char_class.name == "Herald":
                        if char.slist[skill][0] >= 3:
                            char.slist[f"grun{skill.lower()}"] = global_skill_list[f"grun{skill}"].copy()
                        if char.slist[skill][0] >= 4:
                            char.slist[f"{skill.lower()}mor"] = global_skill_list[f"{skill}mor"].copy()
                        if char.slist[skill][0] >= 6:
                            char.slist[f"grun{skill.lower()}mor"] = global_skill_list[f"grun{skill}mor"].copy()
                        if char.slist[skill][0] >= 7:
                            char.slist[f"{skill.lower()}matha"] = global_skill_list[f"{skill}matha"].copy()
                        if char.slist[skill][0] >= 9:
                            char.slist[f"grun{skill.lower()}matha"] = global_skill_list[f"grun{skill}matha"].copy()
                    pass


        elif skill in ("revita"):
            
            descriptor = (f"{skill.upper()} (Level: {skill_level}) is a skill that revives one fallen ally with 30% of HP.\n")
            
            if char.char_class == thaumaturge or char.char_class.name == "Thaumaturge":
                if char.slist[skill][0] <2:
                    descriptor += (f" At Level 2 the TP cost of REVITA is reduced.\n")
                if char.slist[skill][0] <3:
                    descriptor += (f" At Level 3 you learn {skill.upper()}MOR, which revives one fallen ally with 60% of HP.\n")
                if char.slist[skill][0] <4:
                    descriptor += (f" At Level 4 the TP cost of REVITA and REVITAMOR is reduced.\n")
                if char.slist[skill][0] <5:
                    descriptor += (f" At Level 5 you learn {skill.upper()}MATHA, which revives one fallen ally with full HP.\n")
                if char.slist[skill][0] <10:
                    descriptor += (f" At every Level past 5 the TP cost of all REVITA skills is reduced.\n")

            
            if choice_final == True:
                if char.skillpts >0:
                    char.slist[skill][0] += 1
                    char.skillpts -= 1

                    if char.char_class == thaumaturge or char.char_class.name == "Thaumaturge":
                        if char.slist[skill][0] >= 2:
                            char.slist[f"revita"][2] = 9
                        if char.slist[skill][0] >= 3:
                            char.slist[f"{skill.lower()}mor"] = global_skill_list[f"{skill}mor"].copy()
                        if char.slist[skill][0] >= 4:
                            char.slist[f"revita"][2] = 8
                            char.slist[f"revitamor"][2] = 16
                        if char.slist[skill][0] >= 5:
                            char.slist[f"{skill.lower()}matha"] = global_skill_list[f"{skill}matha"].copy()
                        if char.slist[skill][0] >= 6:
                            char.slist[f"revita"][2] = 7
                            char.slist[f"revitamor"][2] = 15
                            char.slist[f"revitamatha"][2] = 27
                        if char.slist[skill][0] >= 7:
                            char.slist[f"revita"][2] = 6
                            char.slist[f"revitamor"][2] = 13
                            char.slist[f"revitamatha"][2] = 24
                        if char.slist[skill][0] >= 8:
                            char.slist[f"revita"][2] = 5
                            char.slist[f"revitamor"][2] = 12
                            char.slist[f"revitamatha"][2] = 21
                        if char.slist[skill][0] >= 9:
                            char.slist[f"revita"][2] = 4
                            char.slist[f"revitamor"][2] = 10
                            char.slist[f"revitamatha"][2] = 18
                        if char.slist[skill][0] >= 10:
                            char.slist[f"revita"][2] = 3
                            char.slist[f"revitamor"][2] = 9
                            char.slist[f"revitamatha"][2] = 15
                    pass


        elif "enha" in skill:
            
            descriptor = (f"{skill.upper()} (Level: {skill_level}) is a skill that {global_skill_list[skill][1]}\n")
            
            if char.char_class == herald or char.char_class.name == "Herald":
                if skill_level <2:
                    descriptor += (f" At Level 2 you learn GRUN{skill.upper()}, which {global_skill_list[f'grun{skill}'][1]}\n")
                if skill_level <3:
                    descriptor += (f" At Level 3 you learn ENHAVI, which {global_skill_list['enhavi'][1]}\n")
                if skill_level <4:
                    descriptor += (f" At Level 4 you learn GRUNENHAVI, which {global_skill_list['grunenhavi'][1]}\n")
                if skill_level <5:
                    descriptor += (f" At Level 5 you learn ENHAGI, which {global_skill_list['enhagi'][1]}\n")
                if skill_level <6:
                    descriptor += (f" At Level 6 you learn GRUNENHAGI, which {global_skill_list['grunenhagi'][1]}\n")
                if skill_level <7:
                    descriptor += (f" At Level 7 you learn ENHALK, which {global_skill_list['enhalk'][1]}\n")
                if skill_level <8:
                    descriptor += (f" At Level 8 you learn GRUNENHALK, which {global_skill_list['grunenhalk'][1]}\n")
                if skill_level <9:
                    descriptor += (f" At Level 9, the TP cost of all ENHA skills is lowered.\n")
                if skill_level <10:
                    descriptor += (f" At Level 10, the TP cost of all ENHA skills is lowered further.")

            elif char.char_class == arcanist or char.char_class.name == "Arcanist":
                if skill_level <2:
                    descriptor += (f" At Level 2 you learn GRUN{skill.upper()}, which {global_skill_list[f'grun{skill}'][1]}\n")
                if skill_level <3:
                    descriptor += (f" At Level 3 you learn ENHALK, which {global_skill_list['enhalk'][1]}\n")
                if skill_level <4:
                    descriptor += (f" At Level 4 you learn GRUNENHALK, which {global_skill_list['grunenhalk'][1]}\n")
                if skill_level <5:
                    descriptor += (f" At Level 5 you learn ENHAGI, which {global_skill_list['enhagi'][1]}\n")
                if skill_level <6:
                    descriptor += (f" At Level 6 you learn GRUNENHAGI, which {global_skill_list['grunenhagi'][1]}\n")
                if skill_level <7:
                    descriptor += (f" At Level 7 you learn ENHAVI, which {global_skill_list['enhavi'][1]}\n")
                if skill_level <8:
                    descriptor += (f" At Level 8 you learn GRUNENHAVI, which {global_skill_list['grunenhavi'][1]}\n")
                if skill_level <9:
                    descriptor += (f" At Level 9, the TP cost of all ENHA skills is lowered.\n")
                if skill_level <10:
                    descriptor += (f" At Level 10, the TP cost of all ENHA skills is lowered further.")
            

            
            if choice_final == True:
                if char.skillpts >0:
                    char.slist[skill][0] += 1
                    char.skillpts -= 1

                    if char.char_class == arcanist or char.char_class.name == "Arcanist":
                        if char.slist[skill][0] >= 2:
                            char.slist[f"grun{skill.lower()}"] = global_skill_list[f"grun{skill}"].copy()
                        if char.slist[skill][0] >= 3:
                            char.slist[f"enhalk"] = global_skill_list[f"enhalk"].copy()
                        if char.slist[skill][0] >= 4:
                            char.slist[f"grunenhalk"] = global_skill_list[f"grunenhalk"].copy()
                        if char.slist[skill][0] >= 5:
                            char.slist[f"enhagi"] = global_skill_list[f"enhagi"].copy()
                        if char.slist[skill][0] >= 6:
                            char.slist[f"grunenhagi"] = global_skill_list[f"grunenhagi"].copy()
                        if char.slist[skill][0] >= 7:
                            char.slist[f"enhavi"] = global_skill_list[f"enhavi"].copy()
                        if char.slist[skill][0] >= 8:
                            char.slist[f"grunenhavi"] = global_skill_list[f"grunenhavi"].copy()
                        if char.slist[skill][0] >= 9:
                            char.slist[f"enhate"][2] = 5
                            char.slist[f"enhavi"][2] = 5
                            char.slist[f"enhalk"][2] = 5
                            char.slist[f"enhagi"][2] = 5
                            char.slist[f"grunenhate"][2] = 14
                            char.slist[f"grunenhavi"][2] = 14
                            char.slist[f"grunenhalk"][2] = 14
                            char.slist[f"grunenhagi"][2] = 14
                        if char.slist[skill][0] >= 10:
                            char.slist[f"enhate"][2] = 4
                            char.slist[f"enhavi"][2] = 4
                            char.slist[f"enhalk"][2] = 4
                            char.slist[f"enhagi"][2] = 4
                            char.slist[f"grunenhate"][2] = 12
                            char.slist[f"grunenhavi"][2] = 12
                            char.slist[f"grunenhalk"][2] = 12
                            char.slist[f"grunenhagi"][2] = 12

                    elif char.char_class == herald or char.char_class.name == "Herald":
                        if char.slist[skill][0] >= 2:
                            char.slist[f"grun{skill.lower()}"] = global_skill_list[f"grun{skill}"].copy()
                        if char.slist[skill][0] >= 3:
                            char.slist[f"enhavi"] = global_skill_list[f"enhavi"].copy()
                        if char.slist[skill][0] >= 4:
                            char.slist[f"grunenhavi"] = global_skill_list[f"grunenhavi"].copy()
                        if char.slist[skill][0] >= 5:
                            char.slist[f"enhagi"] = global_skill_list[f"enhagi"].copy()
                        if char.slist[skill][0] >= 6:
                            char.slist[f"grunenhagi"] = global_skill_list[f"grunenhagi"].copy()
                        if char.slist[skill][0] >= 7:
                            char.slist[f"enhalk"] = global_skill_list[f"enhalk"].copy()
                        if char.slist[skill][0] >= 8:
                            char.slist[f"grunenhalk"] = global_skill_list[f"grunenhalk"].copy()
                        if char.slist[skill][0] >= 9:
                            char.slist[f"enhast"][2] = 5
                            char.slist[f"enhavi"][2] = 5
                            char.slist[f"enhalk"][2] = 5
                            char.slist[f"enhagi"][2] = 5
                            char.slist[f"grunenhast"][2] = 14
                            char.slist[f"grunenhavi"][2] = 14
                            char.slist[f"grunenhalk"][2] = 14
                            char.slist[f"grunenhagi"][2] = 14
                        if char.slist[skill][0] >= 10:
                            char.slist[f"enhast"][2] = 4
                            char.slist[f"enhavi"][2] = 4
                            char.slist[f"enhalk"][2] = 4
                            char.slist[f"enhagi"][2] = 4
                            char.slist[f"grunenhast"][2] = 12
                            char.slist[f"grunenhavi"][2] = 12
                            char.slist[f"grunenhalk"][2] = 12
                            char.slist[f"grunenhagi"][2] = 12
                    pass

        elif "enfe" in skill:
            
            descriptor = (f"{skill.upper()} (Level: {skill_level}) is a skill that {global_skill_list[skill][1]}\n")
            
            if char.char_class == arcanist or char.char_class.name == "Arcanist":
                if skill_level <2:
                    descriptor += (f" At Level 2 you learn GRUN{skill.upper()}, which {global_skill_list[f'grun{skill}'][1]}\n")
                if skill_level <3:
                    descriptor += (f" At Level 3 you learn ENFELK, which {global_skill_list['enfelk'][1]}\n")
                if skill_level <4:
                    descriptor += (f" At Level 4 you learn GRUNENFELK, which {global_skill_list['grunenfelk'][1]}\n")
                if skill_level <5:
                    descriptor += (f" At Level 5 you learn ENFEVI, which {global_skill_list['enfevi'][1]}\n")
                if skill_level <6:
                    descriptor += (f" At Level 6 you learn GRUNENFEVI, which {global_skill_list['grunenfevi'][1]}\n")
                if skill_level <7:
                    descriptor += (f" At Level 7 you learn ENFEGI, which {global_skill_list['enfegi'][1]}\n")
                if skill_level <8:
                    descriptor += (f" At Level 8 you learn GRUNENFEGI, which {global_skill_list['grunenfegi'][1]}\n")
                if skill_level <9:
                    descriptor += (f" At Level 9 you learn ENFEST, which {global_skill_list['enfest'][1]}\n")
                if skill_level <10:
                    descriptor += (f" At Level 10 you learn GRUNENFEST, which {global_skill_list['grunenfest'][1]}\n")
            

            
            if choice_final == True:
                if char.skillpts >0:
                    char.slist[skill][0] += 1
                    char.skillpts -= 1

                    if char.char_class == arcanist or char.char_class.name == "Arcanist":
                        if char.slist[skill][0] >= 2:
                            char.slist[f"grun{skill.lower()}"] = global_skill_list[f"grun{skill}"].copy()
                        if char.slist[skill][0] >= 3:
                            char.slist[f"enfelk"] = global_skill_list[f"enfelk"].copy()
                        if char.slist[skill][0] >= 4:
                            char.slist[f"grunenfelk"] = global_skill_list[f"grunenfelk"].copy()
                        if char.slist[skill][0] >= 5:
                            char.slist[f"enfevi"] = global_skill_list[f"enfevi"].copy()
                        if char.slist[skill][0] >= 6:
                            char.slist[f"grunenfevi"] = global_skill_list[f"grunenfevi"].copy()
                        if char.slist[skill][0] >= 7:
                            char.slist[f"enfegi"] = global_skill_list[f"enfegi"].copy()
                        if char.slist[skill][0] >= 8:
                            char.slist[f"grunenfegi"] = global_skill_list[f"grunenfegi"].copy()
                        if char.slist[skill][0] >= 9:
                            char.slist[f"enfest"] = global_skill_list[f"enfest"].copy()
                        if char.slist[skill][0] >= 10:
                            char.slist[f"grunenfest"] = global_skill_list[f"grunenfest"].copy()
                        
                    pass

        elif "taunt" in skill:
            
            descriptor = (f"{skill.upper()} (Level: {skill_level}) is a skill that {global_skill_list[skill][1]}\n")
            
            if char.char_class == knight or char.char_class.name == "Knight":
                descriptor += (f" At Levels 2, 4, 6, 8 and 10, your defense while taunting rises more.\n")
                descriptor += (f" At Levels 3, 5, 7, and 9, you draw more attention from enemies.\n")
                descriptor += (f" At Levels 3, 6, and 9, the TP cost of TAUNT is reduced.")


            if choice_final == True:
                if char.skillpts >0:
                    char.slist[skill][0] += 1
                    char.skillpts -= 1

                    if char.char_class == knight or char.char_class.name == "Knight":
                        if char.slist[skill][0] >= 3:
                            char.slist[skill][2] = 7
                        if char.slist[skill][0] >= 6:
                            char.slist[skill][2] = 6
                        if char.slist[skill][0] >= 9:
                            char.slist[skill][2] = 5

        elif "protect" in skill:
            
            descriptor = (f"{skill.upper()} (Level: {skill_level}) is a skill that {global_skill_list[skill][1]}\n")
            
            if char.char_class == knight or char.char_class.name == "Knight":
                descriptor += (f" Every level increases the effect of PROTECT.\n")
                descriptor += (f" At Levels 3, 5, and 9, the duration of PROTECT increases by 1 turn.")

            if choice_final == True:
                if char.skillpts >0:
                    char.slist[skill][0] += 1
                    char.skillpts -= 1

        elif "decoy" in skill:
            
            descriptor = (f"{skill.upper()} (Level: {skill_level}) is a skill that {global_skill_list[skill][1]}\n")
            
            if char.char_class == scout or char.char_class.name == "Scout":
                descriptor += (f" Every level increases the effect of DECOY, increasing all of its stats.\n")

            if choice_final == True:
                if char.skillpts >0:
                    char.slist[skill][0] += 1
                    char.skillpts -= 1

        elif "appraise" in skill:
            
            descriptor = (f"{skill.upper()} (Level: {skill_level}) is a skill that {global_skill_list[skill][1]}\n")
            
            if char.char_class == quartermaster or char.char_class.name == "Quartermaster":
                descriptor += (f" Every level increases the effect of APPRAISE.\n")

            if choice_final == True:
                if char.skillpts >0:
                    char.slist[skill][0] += 1
                    char.skillpts -= 1

        elif "bomb" in skill:
            
            descriptor = (f"{skill.upper()} (Level: {skill_level}) is a skill that {global_skill_list[skill][1]}\n")
            
            if char.char_class == quartermaster or char.char_class.name == "Quartermaster":
                descriptor += (f" Every level increases the effect of BOMB.\n")

            if choice_final == True:
                if char.skillpts >0:
                    char.slist[skill][0] += 1
                    char.skillpts -= 1

        elif "coating" in skill:
            
            descriptor = (f"{skill.upper()} (Level: {skill_level}) is a skill that {global_skill_list[skill][1]}\n")
            
            if char.char_class == quartermaster or char.char_class.name == "Quartermaster":
                descriptor += (f" Every level increases the effect of COATING.\n")
                descriptor += (f" At Levels 3, 5, and 9, the duration of COATING increases by 1 turn.")

            if choice_final == True:
                if char.skillpts >0:
                    char.slist[skill][0] += 1
                    char.skillpts -= 1

        elif "sneak" in skill:
            
            descriptor = (f"{skill.upper()} (Level: {skill_level}) is a skill that {global_skill_list[skill][1]}\n")
            

            descriptor += (f" Every level increases the effect of SNEAK.\n")
            descriptor += (f" At Levels 5 and 9, the effects of SNEAK increases even further, along with TP costs.")

            if choice_final == True:
                if char.skillpts >0:
                    char.slist[skill][0] += 1
                    char.skillpts -= 1

                    if char.slist[skill][0] >= 5:
                        char.slist[skill][2] = 8

                    if char.slist[skill][0] >= 9:
                        char.slist[skill][2] = 10

        elif "hunt" in skill:
            
            descriptor = (f"{skill.upper()} (Level: {skill_level}) is a skill that {global_skill_list[skill][1]}\n")
            

            descriptor += (f" At Levels 2, 4, 6, 8, and 10, the effects of HUNT increases.\n")
            descriptor += (f" At Levels 3, 5, 7, and 9, the TP cost of HUNT decreases.")

            if choice_final == True:
                if char.skillpts >0:
                    char.slist[skill][0] += 1
                    char.skillpts -= 1

                    if char.slist[skill][0] >= 3:
                        char.slist[skill][2] = 14

                    if char.slist[skill][0] >= 5:
                        char.slist[skill][2] = 13

                    if char.slist[skill][0] >= 7:
                        char.slist[skill][2] = 12

                    if char.slist[skill][0] >= 9:
                        char.slist[skill][2] = 10           

        elif "cleave" in skill:
            
            descriptor = (f"{skill.upper()} (Level: {skill_level}) is a skill that {char.slist[skill][1]}\n")
            

            descriptor += (f" At Levels 2, 4, 6, 8, and 10, the maximum number of attacks increases by 1.\n")
            descriptor += (f" At Levels 3, 5, 7, and 9, the minimum number of attacks increases by 1.\n")
            descriptor += (f" Every level increases the TP cost of CLEAVE by 1.")

            "Attacks random enemies multiple (1-3) times."

            if choice_final == True:
                if char.skillpts >0:
                    char.slist[skill][0] += 1
                    char.skillpts -= 1

                    if char.slist[skill][0] >= 2:
                        char.slist[skill][1] = "Attacks random enemies multiple (1-4) times."
                    
                    if char.slist[skill][0] >= 3:
                        char.slist[skill][1] = "Attacks random enemies multiple (2-4) times."

                    if char.slist[skill][0] >= 4:
                        char.slist[skill][1] = "Attacks random enemies multiple (2-5) times."

                    if char.slist[skill][0] >= 5:
                        char.slist[skill][1] = "Attacks random enemies multiple (3-5) times."
                    
                    if char.slist[skill][0] >= 6:
                        char.slist[skill][1] = "Attacks random enemies multiple (3-6) times."

                    if char.slist[skill][0] >= 7:
                        char.slist[skill][1] = "Attacks random enemies multiple (4-6) times."

                    if char.slist[skill][0] >= 8:
                        char.slist[skill][1] = "Attacks random enemies multiple (4-7) times."

                    if char.slist[skill][0] >= 9:
                        char.slist[skill][1] = "Attacks random enemies multiple (5-7) times."

                    if char.slist[skill][0] >= 10:
                        char.slist[skill][1] = "Attacks random enemies multiple (5-8) times."

                    char.slist[skill][2] = 4 + char.slist[skill][0] # TP cost == Skill LVL + 4

        else:
            descriptor = (f"{skill.upper()} (Level: {skill_level}) is a skill that {global_skill_list[skill][1]}\n")

    def expPlus():
        for char in party:
            char.exp += 1500
            checkLevel(char)

    def levelUpChar(char):
        # global chartolevel.char_class
        global charstattolevel
        global chartolevel

        # chartolevel.char_class = pickClass(char.char_class)
        charstattolevel = None
        chartolevel = char

        if chartolevel != None and chartolevel.char_class != None:
            renpy.call_screen("levelUpScreen")

        char.level += 1
        char.skillpts += 1
        
        #Increase base stats
        char.maxhp += chartolevel.char_class.improv[0]*chartolevel.char_class.hp
        char.hp += chartolevel.char_class.improv[0]*chartolevel.char_class.hp
        char.maxtp += chartolevel.char_class.improv[1]*chartolevel.char_class.tp
        char.tp += chartolevel.char_class.improv[1]*chartolevel.char_class.tp
        char.str += chartolevel.char_class.improv[2]
        char.tec += chartolevel.char_class.improv[3]
        char.vit += chartolevel.char_class.improv[4]
        char.agi += chartolevel.char_class.improv[5]
        char.lck += chartolevel.char_class.improv[6]
        char.dmg += chartolevel.char_class.improv[7]


        # while choice_made == False:
        
            # choice = input(f"Choose one stat to improve:\n Max (H)P: {math.floor(char.maxhp)} >>> {math.floor(char.maxhp+chartolevel.char_class.hp)}\n Max (TP): {math.floor(char.maxtp)} >>> {math.floor(char.maxtp+chartolevel.char_class.tp)}\n (S)tr: {math.floor(char.str)} >>> {math.floor(char.str+1)}\n (T)ec: {math.floor(char.tec)} >>> {math.floor(char.tec+1)}\n (V)it: {math.floor(char.vit)} >>> {math.floor(char.vit+1)}\n (A)gi: {math.floor(char.agi)} >>> {math.floor(char.agi+1)}\n (L)ck: {math.floor(char.lck)} >>> {math.floor(char.lck+1)}\n\n")

        if charstattolevel == "hp":
            # final_choice = input(f"\nThis will increase your Max HP by {math.floor(chartolevel.char_class.hp)}.\n Proceed? (Y/N)\n")
            # if final_choice.lower() == "y" or final_choice.lower == "yes":
            char.maxhp += chartolevel.char_class.hp
            char.hp += chartolevel.char_class.hp

    
        if charstattolevel == "tp":
            char.maxtp += chartolevel.char_class.tp
            char.tp += chartolevel.char_class.tp

        if charstattolevel == "str":
                char.str += 1
                choice_made = True

        if charstattolevel == "tec":
                char.tec += 1

        if charstattolevel == "vit":
                char.vit += 1

        if charstattolevel == "agi":
                char.agi += 1

        if charstattolevel == "lck":
                char.lck += 1

    ####

# RENPY DEFAULTS

default drav = Character(
        name = "Dravroth", char_class = herald, race = r_dragonkin,
        level = 1, maxhp = 60, hp = 60, maxtp = 30, tp = 30,
        str = 7, dmg = 1, tec = 4, vit = 4, agi = 5, lck = 4,
        acted = False, defending = False, weak = [], resist = [], exp = 0, init = 0, skillpts= 0, perkpts= 0, effects={}, threat=10,
        equip = {
        "Weapon":weapon1,
        "Armor":armor1,
        "Accessory":None,
        "Charm":None},
        slist =  {
            "cura": global_skill_list["cura"].copy(),
            "firo": global_skill_list["firo"].copy(),
            "enhast": global_skill_list["enhast"].copy() })
default dan = Character(
        name = "Thorudan", char_class= thaumaturge, race = r_faefolk,
        level=1, maxhp=60, hp=60, maxtp=60, tp=60,
        str = 5, dmg = 1, tec = 6, vit = 3, agi = 3, lck = 4,
        acted = False, defending = False, weak = [], resist = [], exp = 0, init = 0, skillpts= 0, perkpts= 0, effects={}, threat=10,
        equip = {
        "Weapon":weapon1,
        "Armor":armor1,
        "Accessory":None,
        "Charm":None},
        slist = {"cura": global_skill_list["cura"].copy(),
                "tera": global_skill_list["tera"].copy(),
                "revita": global_skill_list["revita"].copy()})
default mars = Character(
        name = "Mars", char_class = knight, race = r_orc,
        level = 1, maxhp = 100, hp = 100, maxtp = 20, tp = 20,
        str = 7, dmg = 3, tec = 2, vit = 6, agi = 3, lck = 3,
        acted= False, defending = False, weak = [], resist = [], exp = 0, init = 0, skillpts= 0, perkpts= 0,effects={}, threat=10,
        equip = {
        "Weapon":weapon1,
        "Armor":armor1,
        "Accessory":None,
        "Charm":None},
        slist = {
            "cleave": global_skill_list["cleave"].copy(),
            "protect": global_skill_list["protect"].copy(),
            "taunt": global_skill_list["taunt"].copy()})
default eck = Character(
        name="Eckbert", char_class= scout, race = r_faefolk,
        level=1, maxhp=60, hp=60, maxtp=30, tp=30,
        str=6, dmg=2, tec=2, vit=3, agi=7, lck=6,
        acted=False, defending=False, weak=[], resist = [], exp=0, init=0, skillpts= 0, perkpts= 0,effects={}, threat=10,
        equip={
        "Weapon":weapon1,
        "Armor":armor1,
        "Accessory":None,
        "Charm":None},
        slist={"decoy": global_skill_list["decoy"].copy(),
            "hunt": global_skill_list["hunt"].copy(),
            "sneak": global_skill_list["sneak"].copy()})
default khoy = Character(
    name = "Khoyat", char_class = arcanist, race = r_lizardfolk,
        level = 1, maxhp = 40, hp = 40, maxtp = 70, tp = 70,
        str = 4, dmg = 1, tec = 9, vit = 2, agi = 5, lck = 2,
        acted = False, defending = False, weak = [], resist = [], exp = 0, init = 0, skillpts= 0, perkpts= 0, effects={}, threat=10,
        equip = {
        "Weapon":weapon1,
        "Armor":armor1,
        "Accessory":None,
        "Charm":None},
        slist =  {
            "veno": global_skill_list["veno"].copy(),
            "enhate": global_skill_list["enhate"].copy(),
            "enfete": global_skill_list["enfete"].copy() })
default doekel = Character(
    name = "Doekel", char_class = thaumaturge, race = r_dwarf,
        level = 1, maxhp = 70, hp = 70, maxtp = 50, tp = 50,
        str = 5, dmg = 1, tec = 6, vit = 3, agi = 3, lck = 4,
        acted = False, defending = False, weak = [], resist = [], exp = 0, init = 0, skillpts= 0, perkpts= 0, effects={}, threat=10,
        equip = {
        "Weapon":weapon1,
        "Armor":armor1,
        "Accessory":None,
        "Charm":None},
        slist =  {
            "cura": global_skill_list["cura"].copy(),
            "revita": global_skill_list["revita"].copy(),
            "volt": global_skill_list["volt"].copy() })
default okebur = Character(
    name = "Okebur", char_class = quartermaster, race = r_beastfolk,
        level = 1, maxhp = 60, hp = 60, maxtp = 30, tp = 30,
        str = 5, dmg = 1, tec = 1, vit = 6, agi = 7, lck = 5,
        acted = False, defending = False, weak = [], resist = [], exp = 0, init = 0, skillpts= 0, perkpts= 0, effects={}, threat=10,
        equip = {
        "Weapon":weapon1,
        "Armor":armor1,
        "Accessory":None,
        "Charm":None},
        slist =  {
            "appraise": global_skill_list["appraise"].copy(),
            "bomb": global_skill_list["bomb"].copy(),
            "coating": global_skill_list["coating"].copy() })


default character_roster = [khoy,okebur]
default party = [drav, dan, mars, eck]
default party_money = 100

# default chartolevel = None
# default charstattolevel = None
# default chartolevel.char_class = None