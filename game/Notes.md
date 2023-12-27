
# PROJECT OVERALL
    # Create a file just for characters and classes (DONE)

# PERKS
    # Every 5/10(?) levels, characters get access to new spell level/type

    # Allow classes to get any skills

    # Implement Leveling tools (to alleviate grind)
    
# DUNGEON CRAWLER PART
    # Try to implement a random dungeon generator?
    # DUNGEON Maker tool in Ren'py (DONE)

    # Field Bosses (REDO)
        # To do this, the code needs a "fieldmap" that contains the whole dungeon, but shows only where the group is at, at a 3x3/5x5 grid around the party. (doable, but requires big rewrite, however, allows for Field bosses)

    # Implement Doors and Objects (chests/treasure) (DONE)
    # Implement Stairs down
        # Implement more floors
        # Implement enemy difficulty by floor (as well as party level)
    # Implement Rest Area (DONE)
    # Implement Merchant (DONE)

    # Implement Traps and Puzzles

    # More unique enemy types

    # Have different, unconnected dungeons of different types (forest, cave, etc.)


# IMPLEMENT CITY (& QUESTS?)
    # City Tavern (DONE)
    # City Shop (DONE)
    # City Trainer (DONE) // Missing Perks 
    # Implement Quests / Goals
    # Implement random conversations / Lore Drop

    # Implement Story and Canon companions (Dravroth (Herald), Mars (Knight), Eckbert (Scout), Doekel (Thaumaturge), Khoyat (Arcanist), Okebur (Quartermaster))

# COMBAT & SKILLS
    # Rename Skills (DONE)
    # Use items in combat (DONE)
    # Escape combat (DONE)
    # create buff, debuff skills (DONE)

    # Enemy Generator? (DONE)
    # Fix formulas (DONE) (Do AGAIN)

# CLASS SKILLS
    # KNIGHT
        # SKILLS
            #       CHARGE attack 1 opp up to 3 times (minumum increases by 1 per 2 levels)(damage increases every 3 levels)(lvl 1/10)
            # TAUNT Taunts enemies and increases own defense.
            # CLEAVE attack random opps up to 5 times (mininum increases by 1 per 2 levels)(lvl 1/10)
            # PROTECT reduce damage to all by 10%/lvl (lvl 1/10)
        # PERKS
            #   STR boost for one lv1 / party lv3 for lvl turns (lvl 1/5)
            #   VIT boost for one lv1 / party lv3 for lvl turns (lvl 1/5)
            # 
            # 
            # ENDURE Chance to resist death 10%/lvl (lvl 1/5)

    # THAUMATURGE
        # SKILLS # FP cost reduced / lvl
            # ELEMENTAL damage weak lv1 / multi lvl 3 / med lvl 5 / heavy lvl 7 (lvl 1/10)
            # HEALING weak lvl 1 / multi lvl 2 / med lvl 3 / heavy lvl 4 (lvl 1/10)
            # REVIVE weak lvl 1 / med lvl 3 / full lvl 5 / --- lvl 7 (lvl 1/10)
        # PERKS
            # Restore HP at end of combat lvl 1 / per turn lvl 3 / per step lvl 5 (lvl 1/5)
            # Healing skills restore TP as well (lvl 1/5)
            # Life drain attack

    # ARCANIST
        # SKILLS # FP cost reduced / lvl
            # ELEMENTAL damage weak lvl 1 / multi lvl 2 / med lvl 3 / heavy lvl 4 (lvl 1/10)
            # ENHA TEC %/lvl (lvl 1/10)
            # ENFE TEC (lvl 1/10)
        # PERKS
            # Restore FP per enemy you kill lvl1 / at end of combat lvl 3 / per turn lvl 5 (lvl 1/5)
            # Reflect damage to enemies (lvl 1/5)
            # New Element Type (lvl 1/5)

    # SCOUT
        # SKILLS
            # SNEAK hit one opp with increased crit chance (lvl 1/10)
            # DECOY Create a false target with it's own HP pool (lvl 1/10)
            # HUNT deal more damage to a creature whose HP is higher (lvl 1/10)
        # PERKS
            # ANALYZE enemy weaknesses and resistances, HP and STATS (lvl 1/5)
            # COUNTER deal back damage to attacker (lvl 1/5)
            # RIPOSTE freely attack an enemy that misses you (lvl 1/5)

    # HERALD
        # SKILLS
            # ELEMENTAL damage weak lvl 1 / multi lvl 4 / med lvl 8 (lvl 1/10)
            # HEALING weak lvl 1 / multi lvl 3 / med lvl 5 / hvy lvl 7 (lvl 1/10)
            # ENHA STR lvl 1/ MSTR lvl 2 / VIT lvl 3 / MVIT lvl 4 / TEC lvl 5 / MTEC lvl 6 / AGI lvl 7 / MAGI lvl 8 / LCK lvl 9 / MLCK lvl 10 (lvl 1/10)
        # PERKS
            # Boosting allies restores HP (lvl 1/5)
            # Killing enemies restores HP (lvl 1/5)
            # Healing allies grants a random boon (lvl 1/5)

    # QUARTERMASTER
        # SKILLS
            #      (?) MONEY SHOOT Attack with money, increasing STR and LCK the more money is spent (lvl 1/10)
            # APPRAISE increases EXP gain / high TP cost (lvl 1/10)
            # BOMB Throws a makeshift bomb that deals elemental damage to all enemies per level (lvl 1/10) (phys/fire/ice/thunder/toxic)
            # COATING grants elemental resistance for a few turns / for party (lvl 1/10)
        # PERKS
            # Increase loot drop rate (lvl 1/5)
            # Freely produces a consumable after X amount of steps (lvl 1/5)
            # Chance of not consuming items (lvl 1/5)




# DAMAGES AND ELEMENTS names, types?
    # Almighty        buff / debuff / damage / Heal
    # yabarag         atk + / atk - / thunder / rage-
    # haka pf'hagan   haste / slow / decay / regen
    # igglebeth       resist death + / kill / toxic / revive
    # irgh d'ebram    mdef + / mdef -/ ice / poison-
    # famphegor       reflect / sleep / air / confuse -
    # gaaphadur       pdef + / pdef - / earth / condition -
    # pasperon        lck + / lck- / fire / heal
    # khosme          - / - / chaos / 

    # Grun > Several targets
    # Lag > weak damage / negative (weak / lag)
    # Comas > medium damage / negative (capable / comasach)
    # Asmatha > heavy damage / negative (biggest/motha)
    # Tin > weak heal / positive (ill / tinn)
    # Cruai > medium heal / positive (tough / cruaidh)
    # Fallain > heavy heal / positive (fallain / healthy)
    # Leas > buff (improve / leasaich)
    # Mios > debuff (worse / nas miosa)

    # fire > Grun/Pas/mor // /Pas/matha
    # water > Grun/Irg/mor // Irg/matha
    # earth > Grun/Gaa/mor // Gaa/matha
    # air > Grun/Fam/mor // Fam/matha

    Fire    //  Firo / mor / matha
    Ice     //  Gelo
    Earth   //  Tera
    Air     //  Gale
    Thunder //  Volt
    Creation//  Cura
    Toxic   //  Veno
    Chaos   //  Nuke

    Revive  //  Revita / mor / matha
    Buff    //  Enha / st / te / vi / ag / lk 
    Debuff  //  Enfe / st / te / vi / ag / lk

    Weak damage spell = 4 TP
    weak damage spell group (grun) = 10 TP
    medium damage spell (mor) =  8 TP
    medium damage spell group (grun/mor) = 16 TP
    heavy damage spell (matha) = 12 TP
    heavy damage spell group (grun/matha) = 22 TP

    cura 3 TP               5
    gruncura 7 TP           10
    curamor 7 TP            10
    gruncuramor 12 TP
    curamatha 18 TP
    gruncuramatha 30 TP

    revita 10 TP / 9 / 8 / 7 / 6 / 5
    revitamor 18 TP / 16 / 14 / 12 / 10 / 8
    revitamatha 30 TP / 27 / 24 / 21 / 18 / 15