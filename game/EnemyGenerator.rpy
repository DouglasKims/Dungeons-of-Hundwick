#Enemy Generator
init python:
    import copy
    import random
    import math

    class Enemy:
        def __init__(self,name,level,maxhp,hp,tp,str,dmg,tec,vit,agi,lck,defending,weak,resist,exp,money,init, slist, effects):
            self.name = name
            self.level = level
            self.maxhp = maxhp
            self.hp = hp
            self.tp = tp
            self.str = str
            self.dmg = dmg
            self.tec = tec
            self.vit = vit
            self.agi = agi
            self.lck = lck
            self.defending = defending
            self.weak = weak
            self.resist = resist
            self.exp = exp
            self.money = money
            self.init = init
            self.effects = effects
            self.slist = slist

    class EnemyType():
        def __init__(self, name, hp, tp, str, dmg, tec, vit, agi, lck, imphp, imptp, impstr, impdmg, imptec, impvit, impagi, implck):
            self.name = name
            self.hp = hp
            self.tp = tp
            self.str = str
            self.dmg = dmg
            self.tec = tec
            self.vit = vit
            self.agi = agi
            self.lck = lck
            self.imphp = imphp
            self.imptp = imptp
            self.impstr = impstr
            self.impdmg = impdmg
            self.imptec = imptec
            self.impvit = impvit
            self.impagi = impagi
            self.implck = implck

    #          0    1       2       3       4       5       6       7       8
    elem = ["phys","fire","wind","earth","ice","thunder","toxic","chaos","death"]

    defaultEnemy = Enemy(
        name = "Enemy", level = 1, maxhp=1, hp = 1, tp = 1,
        str = 1, dmg = 1, tec = 1, vit = 1, agi = 1, lck = 1,
        defending=False,weak=[],resist=[],exp=0,money=0,init=0,effects={}, slist= {}
        )

    enemylist = []

    def generateEnemy(type, leveltogen):
        new = copy.deepcopy(defaultEnemy)

        random.seed(None)
        if type == "Malla":
            model = EnemyType(
                    name = "Malla",
                    hp = round (80 * (random.random()/2 + 0.75)),
                    imphp = round((80 * (random.random()/2 + 0.75)) * 0.25),
                    tp = 4,
                    imptp = 2,
                    str = random.randint(5,7),
                    impstr = random.randint(4,6),
                    tec = random.randint(3,5),
                    imptec = random.randint(2,4),
                    dmg = 1,
                    impdmg = 1/3,
                    vit = random.randint(6,8),
                    impvit = random.randint(4,6),
                    agi = random.randint(5,7),
                    impagi = random.randint(4,6),
                    lck = random.randint(5,7),
                    implck = random.randint(4,6),
                    )
            money = random.randint(2,3)
            new.weak.append(random.choice(["fire","ice","wind","earth"]))
            new.resist.append("phys")

        if type == "Sgeu":
            model = EnemyType(
                    name = "Sgeu",
                    hp = round (80 * (random.random()/2 + 0.75)),
                    imphp = round((80 * (random.random()/2 + 0.75)) * 0.25),
                    tp = 4,
                    imptp = 3,
                    str = random.randint(4,6),
                    impstr = random.randint(3,5),
                    tec = random.randint(3,5),
                    imptec = random.randint(3,5),
                    dmg = 1,
                    impdmg = 1/4,
                    vit = random.randint(5,7),
                    impvit = random.randint(3,5),
                    agi = random.randint(9,11),
                    impagi = random.randint(5,7),
                    lck = random.randint(9,11),
                    implck = random.randint(5,7)
                    )
            money = random.randint(2,4)
            new.weak.append("phys")
            new.weak.append(random.choice(["ice","earth"]))

        if type == "Diogh":
            model = EnemyType(
                    name = "Diogh",
                    hp = round (150 * (random.random()/2 + 0.75)),
                    imphp = round((150 * (random.random()/2 + 0.75)) * 0.25),
                    tp = 5,
                    imptp = 3,
                    str = random.randint(4,6),
                    impstr = random.randint(5,7),
                    tec = random.randint(3,5),
                    imptec = random.randint(2,4),
                    dmg = 2,
                    impdmg = 1/2,
                    vit = random.randint(5,7),
                    impvit = random.randint(3,5),
                    agi = random.randint(3,5),
                    impagi = random.randint(4,6),
                    lck = random.randint(2,4),
                    implck = random.randint(3,5)
                    )
            money = random.randint(2,5)
            new.weak.append(random.choice(["fire","ice","wind","earth","thunder"]))
            new.weak.append("toxic")

        if type == "Colt":
            model = EnemyType(
                    name = "Colt",
                    hp = round (120 * (random.random()/2 + 0.75)),
                    imphp = round((120 * (random.random()/2 + 0.75)) * 0.25),
                    tp = 8,
                    imptp = 5,
                    str = random.randint(4,6),
                    impstr = random.randint(4,6),
                    tec = random.randint(4,6),
                    imptec = random.randint(2,4),
                    dmg = 1,
                    impdmg = 1/3,
                    vit = random.randint(7,9),
                    impvit = random.randint(3,5),
                    agi = random.randint(3,5),
                    impagi = random.randint(4,6),
                    lck = random.randint(3,5),
                    implck = random.randint(4,6)
                    )
            money = random.randint(2,6)
            new.weak.append(random.choice(["fire","ice","wind","earth","thunder","toxic"]))
            newelem = None
            while newelem in new.weak or newelem == None:
                newelem = random.choice(["fire","ice","wind","earth","thunder","toxic"])
            new.weak.append(newelem)

        if type == "Adhbah":
            model = EnemyType(
                    name = "Adhbah",
                    hp = round (80 * (random.random()/2 + 0.75)),
                    imphp = round((80 * (random.random()/2 + 0.75)) * 0.25),
                    tp = 12,
                    imptp = 8,
                    str = random.randint(2,4),
                    impstr = random.randint(2,4),
                    tec = random.randint(4,6),
                    imptec = random.randint(3,5),
                    dmg = 1,
                    impdmg = 1/5,
                    vit = random.randint(5,7),
                    impvit = random.randint(3,5),
                    agi = random.randint(3,5),
                    impagi = random.randint(4,6),
                    lck = random.randint(3,5),
                    implck = random.randint(4,6)
                    )
            money = random.randint(3,5)
            new.resist.append(random.choice(["fire","ice","wind","earth","thunder","toxic"]))
            
        if type == "Grain":
            model = EnemyType(
                    name = "Grain",
                    hp = round (60 * (random.random()/2 + 0.75)),
                    imphp = round((60 * (random.random()/2 + 0.75)) * 0.25),
                    tp = 15,
                    imptp = 10,
                    str = random.randint(2,4),
                    impstr = random.randint(2,4),
                    tec = random.randint(5,7),
                    imptec = random.randint(4,6),
                    dmg = 1,
                    impdmg = 1/6,
                    vit = random.randint(5,7),
                    impvit = random.randint(3,5),
                    agi = random.randint(3,5),
                    impagi = random.randint(4,6),
                    lck = random.randint(3,5),
                    implck = random.randint(4,6)
                    )
            money = random.randint(3,6)
            new.resist.append(random.choice(["fire","ice","wind","earth","thunder","toxic"]))
            newelem = None
            while newelem in new.resist or newelem == None:
                newelem = random.choice(["fire","ice","wind","earth","thunder","toxic"])
            new.resist.append(newelem)

        if type == "Laidir":
            model = EnemyType(
                    name = "Laidir",
                    hp = round (400 * (random.random()/2 + 0.75)),
                    imphp = round((200 * (random.random()/2 + 0.75)) * 0.55),
                    tp = 50,
                    imptp = 25,
                    str = random.randint(15,20),
                    impstr = random.randint(5,8),
                    tec = random.randint(8,12),
                    imptec = random.randint(2,6),
                    dmg = 3,
                    impdmg = 1/2,
                    vit = random.randint(12,15),
                    impvit = random.randint(2,8),
                    agi = random.randint(8,12),
                    impagi = random.randint(1,6),
                    lck = random.randint(8,12),
                    implck = random.randint(1,6)
                    )
            money = random.randint(40,80)

        if leveltogen is not None:
            if leveltogen == 0:
                new.name = f"{random.choice(['Puny','Weak','Cowardly'])}"
            elif leveltogen == 1:
                new.name = f"{random.choice(['Malicious','Insidious','Cruel'])}"
            elif leveltogen == 2:
                new.name = f"{random.choice(['Hateful','Spiteful','Wrathful'])}"
            elif leveltogen == 3:
                new.name = f"{random.choice(['Angry','Merciless','Viscerous'])}"
            elif leveltogen >= 4:
                new.name = f"{random.choice(['Cursed','Divisive','Unpleasant'])}"

        new.name += f" {model.name}"
        new.level = 1 + leveltogen
        new.maxhp = model.hp
        # new.maxhp += round(leveltogen * model.imphp)
        new.hp = new.maxhp

        new.tp = model.tp + (model.imptp * leveltogen)
        new.str = model.str + (leveltogen * model.impstr)
        new.dmg = model.dmg + (leveltogen * model.impdmg)
        new.tec = model.tec + (leveltogen * model.imptec)
        new.vit = model.vit + (leveltogen * model.impvit)
        new.agi = model.agi + (leveltogen * model.impagi)
        new.lck = model.lck + (leveltogen * model.implck)
        new.money = money * (leveltogen + 1)
        new.exp = 1
        new.slist["skill"] = {"skill": [new.level, "Causes weak elemental damage to one enemy.", 4]}
        new.slist["skillmor"] = {"skillmor": [new.level, "Causes weak elemental damage to one enemy.", 7]}

        enemylist.append(new)

        return new
