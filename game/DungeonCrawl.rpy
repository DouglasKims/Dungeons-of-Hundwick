init 5 python:
    import math
    import random
    import time
    import copy

    C = "C" # Chest
    O = "O" # Open Chest
    U = "U" # Stairs Up
    D = "D" # Stairs Down
    N = "N" # Secret passage north only
    NO = "NO" # Secret passage north only open
    S = "S" # Secret Passage South only
    SO = "SO" # Secret Passage South only open
    W = "W" # Secret Passage West only
    WO = "WO" # Secret Passage West only open
    E = "E" # Secret Passage East only
    EO = "EO" # Secret Passage East only open
    R = "R" # Resting Area
    M = "M" # Merchant
    """
    testdungeon = [
        [1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,2,0,0,0,1],
        [1,0,1,1,9,1,0,1,0,1],
        [1,0,1,0,0,1,0,1,0,1],
        [1,2,1,0,1,1,0,0,0,1],
        [1,0,1,0,1,0,0,0,0,1],
        [1,0,1,0,0,0,0,0,0,1],
        [1,D,1,1,1,0,1,1,0,1],
        [1,0,0,0,0,0,1,0,0,1],
        [1,1,1,1,1,1,1,1,1,1]
    ]


    dungeon11 = [
        [1, U,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1], 

        [1, 0,0,0,1,0, C,1,1,1,0, E,0,0,0,0, 0,1,0,0,0, 0,0,1,0,1, 0,0,0,0,0, 1], #1
        [1, 0,0,0,2,0, 0,1,C,0,0, 1,0,1,0,1, 0,1,0,1,1, 1,0,0,0,0, 0,1,0,0,0, 1], #2
        [1, 0,0,0,1,0, 0,1,1,1,0, 1,0,1,1,1, 0,0,0,0,0, 1,1,1,1,0, 1,1,0,0,0, 1], #3
        [1, 1,1,1,1,0, 0,9,0,0,0, 1,0,1,0,1, 0,1,0,1,0, 0,1,0,1,0, 1,0,0,1,1, 1], #4
        [1, 0,0,0,0,0, 0,1,1,1,0, 1,0,1,0,1, 0,1,0,1,1, 0,1,0,0,0, 1,0,0,1,C, 1], #5
    #    0  1 2 3 4 5  6 7 8 9 10 1 2 3 4 5  6 7 8 9 20 1 2 3 4 5  6 7 8 9 30 1
        [1, 0,1,1,0,1, 1,1,0,0,0, 1,0,0,0,0, 0,1,0,0,1, 0,1,0,1,9, 1,0,1,1,0, 1],
        [1, 0,0,1,0,0, 0,1,0,1,1, 1,1,2,1,1, 1,1,0,C,1, 0,1,1,1,0, 1,0,1,1,0, 1],
        [1, 0,1,1,1,1, 0,1,0,1,1, 1,0,0,M,1, 1,1,1,1,1, 0,1,0,1,0, 1,0,9,0,0, 1],
        [1, 0,0,0,0,1, 0,0,0,0,0, 2,0,0,0,2, 0,0,0,0,0, 0,1,0,0,0, 1,0,1,1,1, 1],
        [1, 1,1,1,0,1, 0,1,0,1,1, 1,0,0,0,1, 1,1,1,1,1, 1,1,0,1,0, 1,0,0,0,0, 1], #10
    #    0  1 2 3 4 5  6 7 8 9 10 1 2 3 4 5  6 7 8 9 20 1 2 3 4 5  6 7 8 9 30 1
        [1, 0,0,0,0,1, 0,1,0,0,0, 1,1,2,1,1, C,1,0,0,0, 1,1,0,1,1, 1,1,1,1,0, 1],
        [1, 0,1,1,0,1, 0,1,1,1,0, 1,0,0,1,C, 0,0,0,0,0, 1,0,0,0,0, 0,0,C,1,0, 1],
        [1, 0,C,1,0,0, 0,1,0,0,0, 1,0,1,1,1, C,1,0,1,1, 1,0,1,1,1, 1,1,1,1,0, 1],
        [1, 0,1,1,0,1, 0,1,1,1,1, 1,0,1,C,1, 1,1,0,1,0, 0,0,1,0,0, 0,0,0,0,0, 1],
        [1, 0,0,0,0,1, 0,1,0,C,0, 1,0,1,0,0, 0,0,0,1,0, 1,0,1,0,1, 1,1,1,1,1, 1], #15
    #    0  1 2 3 4 5  6 7 8 9 10 1 2 3 4 5  6 7 8 9 20 1 2 3 4 5  6 7 8 9 30 1
        [1, 1,1,1,1,1, S,1,0,0,0, 1,0,1,1,1, 1,1,2,1,2, 1,1,1,0,1, C,0,0,2,0, 1],
        [1, 0,0,0,0,0, 0,1,1,0,1, 1,0,1,0,0, 0,2,0,0,0, 2,0,0,0,1, C,0,0,1,0, 1],
        [1, 0,1,1,1,1, 0,0,0,0,0, 0,0,1,0,1, 1,1,0,0,0, 1,1,1,0,1, C,0,0,1,2, 1],
        [1, 0,0,0,0,1, 1,1,1,0,1, 1,0,1,0,1, 0,2,0,0,0, 2,0,1,0,1, 1,1,1,1,0, 1],
        [1, 0,1,1,0,0, 0,0,1,2,1, 0,0,1,C,1, 0,1,2,1,2, 1,0,1,0,0, 0,0,0,1,0, 1], #20
    #    0  1 2 3 4 5  6 7 8 9 10 1 2 3 4 5  6 7 8 9 20 1 2 3 4 5  6 7 8 9 30 1
        [1, 0,0,1,1,1, 1,2,1,0,1, 0,1,1,1,1, 0,1,0,1,0, 1,0,1,1,1, 1,1,0,0,0, 1],
        [1, 1,0,0,0,0, 1,0,0,0,1, 0,0,0,0,0, 0,1,0,1,0, 1,0,1,0,0, C,1,1,1,1, 1],
        [1, 1,0,1,1,0, 1,1,0,1,1, 1,1,1,1,1, 1,1,0,1,0, 1,0,0,0,1, 1,1,0,0,0, 1],
        [1, 1,0,0,1,0, 0,0,0,0,0, 0,0,1,0,0, 0,0,0,1,0, 1,1,1,0,C, 1,0,0,1,0, 1],
        [1, 0,0,1,1,1, 1,1,S,1,1, 1,0,1,0,1, 1,S,1,1,0, 0,0,1,C,1, 1,0,1,1,0, 1], #25
    #    0  1 2 3 4 5  6 7 8 9 10 1 2 3 4 5  6 7 8 9 20 1 2 3 4 5  6 7 8 9 30 1
        [1, 0,0,1,C,1, 0,0,0,0,0, 1,0,1,0,1, M,0,0,1,1, 1,0,1,1,1, 0,0,1,0,0, 1],
        [1, 0,1,1,0,1, 0,1,0,1,0, 1,0,1,0,1, 0,0,0,2,0, 1,0,1,0,0, 0,1,1,2,1, 1],
        [1, 0,1,0,0,1, 0,1,C,1,0, 1,0,0,0,1, 0,0,0,1,0, 1,0,0,0,1, 1,1,0,0,0, 1],
        [1, 0,1,0,0,1, 0,1,1,1,0, 1,1,1,1,1, 1,2,1,1,0, 1,1,1,1,1, 0,2,0,0,0, 1],
        [1, 0,0,0,0,1, 0,0,0,0,0, 2,0,0,0,0, 0,0,1,1,0, 0,0,0,0,0, 0,1,0,0,D, 1], #30

        [1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1]
    ]#   0  1 2 3 4 5  6 7 8 9 10 1 2 3 4 5  6 7 8 9 20 1 2 3 4 5  6 7 8 9 30 1

    dungeon11loot = {
        "1,6": (item1, 1,6),
        "2,8": (item1 ,2,8),
        "13,2": (item2 ,13,2),
        "26,4": (armor3 ,26,4),
        "14,9": (armor2 ,14,9),
        "28,8": (weapon3 ,28,8),
        "14,14": (item5 ,14,14),
        "20,14": (chr1 ,20,14),
        "11,16": (item1 ,11,16),
        "12,15": (item2 ,12,15),
        "13,16": (item2 ,13,16),
        "7,19": (item1 ,7,19),
        "12,28": (weapon4 ,12,28),
        "16,26": (item2 ,16,26),
        "17,26": (item3 ,17,26),
        "18,26": (item1 ,18,26),
        "22,26": (item2 ,22,26),
        "24,25": (item2 ,24,25),
        "25,24": (item2 ,25,24),
    }

    dungeon11_laid1 = {
        0: (1,12,8),
        1: (1,13,6),
        2: (1,12,4),
        3: (2,12,2),
        "step": (0)
    }

    dungeon_bosses = [dungeon11_laid1]
    dungeon11_entry = [1,1]
    dungeon11_rest = [
        lambda y, x: 8 <= y <= 10 and 12 <= x <= 14,
        lambda y, x: 17 <= y <= 19 and 18 <= x <= 20,
        lambda y, x: 1 <= y <= 3 and 1 <= x <= 3,
    ]


    dungeon_current_loot = None
    dungeon_current = dungeon11
    dungeon_current_loot = dungeon11loot
    """
    party = party
    party_facing = 2
    danger = 0
    danger_level = ""
    dungeon_level = 1
    vision = None
    # hour_names = [f"Dawn",f"Morning",f"Noon",f"Afternoon",f"Twilight",f"Evening",f"Midnight",f"Witching Hour"]
    # Dark between time = 4*90 and time = 7*90 // Each 90 steps advances the clock
    hour_name = "Morning"
    hour = 9
    steps = 0

    #Game Logic
    def update_coord(x,y):
        global party_coord
        global check
        party_coord[0] += y
        party_coord[1] += x
        check = dungeon_blueprint[party_coord[0]][party_coord[1]]
        
        update_time()
        update_mapcompletion()    
        # update_laid()
        if not restAreaCheck():
            update_danger()

    # FIX
    # def update_laid():

    #     for n in dungeon_bosses:
    #         # Get new position
    #         n["step"] += 1
    #         if n["step"] == len(n)-1:
    #             n["step"] = 0

    #         step_n = n["step"]
    #         step_prev = step_n-1
            
    #         if step_prev < 0:
    #             step_prev = len(n)-2

    #         ly = n[step_n][0]
    #         lx = n[step_n][1]
    #         ly_prev = n[step_prev][0]
    #         lx_prev = n[step_prev][1]

    #         # Clears previous position
    #         dungeon_blueprint[ly_prev][lx_prev] = 0


    #         if n[step_n][2] is not None:
    #             if n[step_n][2] == 8:
    #                 dungeon_blueprint[ly][lx] = f"{RED}▲{RESET}"

    #             elif n[step_n][2] == 2:
    #                 dungeon_blueprint[ly][lx] = f"{RED}▼{RESET}"

    #             elif n[step_n][2] == 4:
    #                 dungeon_blueprint[ly][lx] = f"{RED}◄{RESET}"
                
    #             elif n[step_n][2] == 6:
    #                 dungeon_blueprint[ly][lx] = f"{RED}►{RESET}"

    #             # add to "local map"
    #                 # make local map be shared between party and boss

    def checkHour(int):
        global hour
        
        if int == 1:
            hour += 1
        if int == 0:
            return hour

    def update_time():
        global steps
        global hour
        global hour_name

        steps += 1

        if steps >= 30:
            hour += 1
            steps = 0

        if hour >= 24:
            hour = 0

        if hour >= 18 or hour <= 5:
            switchTime(False)
        else:
            switchTime(True)

        update_hourname()

    def update_hourname():
        global hour_name
        if hour != None: # Hour names
            if hour >= 0 and hour <=2:
                hour_name = "Midnight"
            if hour >= 3 and hour <= 5:
                hour_name = "Witching Hour"
            if hour >= 6 and hour <= 8:
                hour_name = "Dawn"
            if hour >= 9 and hour <= 11:
                hour_name = "Morning"
            if hour >= 12 and hour <= 14:
                hour_name = "Noon"
            if hour >= 15 and hour <= 17:
                hour_name = "Afternoon"
            if hour >= 18 and hour <= 20:
                hour_name = "Twilight"
            if hour >= 21 and hour <= 23:
                hour_name = "Evening"

    def update_mapcompletion():
        global mapcompletion

        tiles_maped = 0
        # dungeon_playermap
        for ny in range(len(dungeon_playermap)):
            for nx in dungeon_playermap[ny]:
                if nx != "":
                    tiles_maped += 1

        mapcompletion = round(tiles_maped * 100 / 1024, ndigits=2)


    time_day = True
    def switchTime(x):
        global time_day

        if x == False and time_day == True:
            time_day = False
            renpy.scene()
            renpy.show("bg Dungeon",at_list=[scenerydark])
        elif x == True and time_day == False:
            time_day = True
            renpy.scene()
            renpy.show("bg Dungeon",at_list=[scenery])

    def update_danger():
        global danger
        global danger_level

        danger += random.randint(1,6)

        if danger >= 100:
                # logText("Enemies have appeared!")
                danger = 0
                renpy.call("combat_label")
                danger_level = f"None"

    view_distance = 2
    localmap = []
    def getMap():

        global dungeon_blueprint
        global view_distance
        global localmap
        localmap = []
        map_coords = {}
        

        if hour >= 18 or hour <=5:
            view_distance = 1
        else:
            view_distance = 2

        # Creates a 3x3 / 5x5 empty grid for @localmap
        for ny in range((view_distance*2+1)):
            localmap.append([])
            for nx in range((view_distance*2+1)):
                localmap[ny].append("")

        # Adding map coordinates based on minimap size. From @dungeon_blueprint to @map_coords
        # try:
        #     for iy in range(view_distance*-1, view_distance+1):
        #         for jx in range(view_distance*-1, view_distance+1):
        #             if iy != 0 or jx != 0:
        #                 map_coords[f"{iy+view_distance},{jx+view_distance}"] = (dungeon_blueprint[party_coord[0]+iy][party_coord[1]+jx], iy+view_distance, jx+view_distance)
        # except IndexError:
        #     map_coords[f"{iy+view_distance},{jx+view_distance}"] = (None, iy+view_distance, jx+view_distance)

        try:
            for iy in range(view_distance * -1, view_distance + 1):
                for jx in range(view_distance * -1, view_distance + 1):
                    target_i = party_coord[0] + iy
                    target_j = party_coord[1] + jx

                    # Check if the target indices are within the bounds of dungeon_blueprint
                    if 0 <= target_i < len(dungeon_blueprint) and 0 <= target_j < len(dungeon_blueprint[0]):
                        if iy != 0 or jx != 0:
                            map_coords[f"{iy + view_distance},{jx + view_distance}"] = (
                            dungeon_blueprint[target_i][target_j], iy + view_distance, jx + view_distance
                        )
                    else:
                        # Handle out-of-bounds indices, for example, by marking them as walls
                        map_coords[f"{iy + view_distance},{jx + view_distance}"] = (1, iy + view_distance, jx + view_distance)
        except IndexError:
            # Handle any other potential index errors here
            pass



        # Check visibility and turn "seen" tiles to True.
        map_coords_check = {
            "NW": (dungeon_blueprint[party_coord[0]-1][party_coord[1]-1], view_distance-1, view_distance-1),
            "N" : (dungeon_blueprint[party_coord[0]-1][party_coord[1]], view_distance-1, view_distance),
            "NE" : (dungeon_blueprint[party_coord[0]-1][party_coord[1]+1], view_distance-1, view_distance+1),
            "W": (dungeon_blueprint[party_coord[0]][party_coord[1]-1], view_distance, view_distance-1),
            "E" : (dungeon_blueprint[party_coord[0]][party_coord[1]+1], view_distance, view_distance+1),
            "SW": (dungeon_blueprint[party_coord[0]+1][party_coord[1]-1], view_distance+1, view_distance-1),
            "S" : (dungeon_blueprint[party_coord[0]+1][party_coord[1]], view_distance+1, view_distance),
            "SE" : (dungeon_blueprint[party_coord[0]+1][party_coord[1]+1], view_distance+1, view_distance+1)
        }

        if view_distance != None: # Check surrounding tiles as seen
            dungeon_playermap[party_coord[0]-1][party_coord[1]-1] = dungeon_blueprint[party_coord[0]-1][party_coord[1]-1]
            dungeon_playermap[party_coord[0]-1][party_coord[1]] = dungeon_blueprint[party_coord[0]-1][party_coord[1]]
            dungeon_playermap[party_coord[0]-1][party_coord[1]+1] = dungeon_blueprint[party_coord[0]-1][party_coord[1]+1]

            dungeon_playermap[party_coord[0]][party_coord[1]-1] = dungeon_blueprint[party_coord[0]][party_coord[1]-1]
            dungeon_playermap[party_coord[0]][party_coord[1]] = dungeon_blueprint[party_coord[0]][party_coord[1]]
            dungeon_playermap[party_coord[0]][party_coord[1]+1] = dungeon_blueprint[party_coord[0]][party_coord[1]+1]

            dungeon_playermap[party_coord[0]+1][party_coord[1]-1] = dungeon_blueprint[party_coord[0]+1][party_coord[1]-1]
            dungeon_playermap[party_coord[0]+1][party_coord[1]] = dungeon_blueprint[party_coord[0]+1][party_coord[1]]
            dungeon_playermap[party_coord[0]+1][party_coord[1]+1] = dungeon_blueprint[party_coord[0]+1][party_coord[1]+1]

            

        if view_distance > 1: #Check visibility // If tile is blocked, conceal tiles behind it.
            
            if map_coords_check["NW"][0] in (1, 9, N, S, E, W, 2, 3, U, D, 8, 6, None, "SO","NO","EO","WO"):
                map_coords["0,0"]=(None, view_distance-2, view_distance-2)
                map_coords["0,1"]=(None, view_distance-2, view_distance-1)
                map_coords["1,0"]=(None, view_distance-1, view_distance-2)
            else: #Toggle SEEN for NW tiles
                dungeon_playermap[party_coord[0]-2][party_coord[1]-2] = dungeon_blueprint[party_coord[0]-2][party_coord[1]-2]
                dungeon_playermap[party_coord[0]-2][party_coord[1]-1] = dungeon_blueprint[party_coord[0]-2][party_coord[1]-1]
                dungeon_playermap[party_coord[0]-1][party_coord[1]-2] = dungeon_blueprint[party_coord[0]-1][party_coord[1]-2]
                pass

            if map_coords_check["NE"][0] in (1, 9, N, S, E, W, 2, 3, U, D, 8, 6, None, "SO","NO","EO","WO"):
                map_coords["0,3"]=(None, view_distance-2, view_distance+1)
                map_coords["0,4"]=(None, view_distance-2, view_distance+2)
                map_coords["1,4"]=(None, view_distance-1, view_distance+2)
            else:
                dungeon_playermap[party_coord[0]-2][party_coord[1]+1] = dungeon_blueprint[party_coord[0]-2][party_coord[1]+1]
                dungeon_playermap[party_coord[0]-2][party_coord[1]+2] = dungeon_blueprint[party_coord[0]-2][party_coord[1]+2]
                dungeon_playermap[party_coord[0]-1][party_coord[1]+2] = dungeon_blueprint[party_coord[0]-1][party_coord[1]+2]
                pass
            
            if map_coords_check["SW"][0] in (1, 9, N, S, E, W, 2, 3, U, D, 8, 6, None, "SO","NO","EO","WO"):
                map_coords["3,0"]=(None, view_distance+1, view_distance-2)
                map_coords["4,0"]=(None, view_distance+2, view_distance-2)
                map_coords["4,1"]=(None, view_distance+2, view_distance-1)
            else:
                dungeon_playermap[party_coord[0]+1][party_coord[1]-2] = dungeon_blueprint[party_coord[0]+1][party_coord[1]-2]
                dungeon_playermap[party_coord[0]+2][party_coord[1]-2] = dungeon_blueprint[party_coord[0]+2][party_coord[1]-2]
                dungeon_playermap[party_coord[0]+2][party_coord[1]-1] = dungeon_blueprint[party_coord[0]+2][party_coord[1]-1]
                pass
            
            if map_coords_check["SE"][0] in (1, 9, N, S, E, W, 2, 3, U, D, 8, 6, None, "SO","NO","EO","WO"):
                map_coords["4,4"]=(None, view_distance+2, view_distance+2)
                map_coords["3,4"]=(None, view_distance+1, view_distance+2)
                map_coords["4,3"]=(None, view_distance+2, view_distance+1)
            else:
                dungeon_playermap[party_coord[0]+2][party_coord[1]+2] = dungeon_blueprint[party_coord[0]+2][party_coord[1]+2]
                dungeon_playermap[party_coord[0]+1][party_coord[1]+2] = dungeon_blueprint[party_coord[0]+1][party_coord[1]+2]
                dungeon_playermap[party_coord[0]+2][party_coord[1]+1] = dungeon_blueprint[party_coord[0]+2][party_coord[1]+1]
                pass

            if map_coords_check["N"][0] in (1, 9, N, S, E, W, 2, 3, U, D, 8, 6, None, "SO","NO","EO","WO"):
                map_coords["0,2"]=(None, view_distance-2, view_distance)
            else:
                dungeon_playermap[party_coord[0]-2][party_coord[1]] = dungeon_blueprint[party_coord[0]-2][party_coord[1]]
                pass

            if map_coords_check["W"][0] in (1, 9, N, S, E, W, 2, 3, U, D, 8, 6, None, "SO","NO","EO","WO"):
                map_coords["2,0"]=(None, view_distance, view_distance-2)
            else:
                dungeon_playermap[party_coord[0]][party_coord[1]-2] = dungeon_blueprint[party_coord[0]][party_coord[1]-2]
                pass

            if map_coords_check["E"][0] in (1, 9, N, S, E, W, 2, 3, U, D, 8, 6, None, "SO","NO","EO","WO"):
                map_coords["2,4"]=(None, view_distance, view_distance+2)
            else:
                dungeon_playermap[party_coord[0]][party_coord[1]+2] = dungeon_blueprint[party_coord[0]][party_coord[1]+2]
                pass

            if map_coords_check["S"][0] in (1, 9, N, S, E, W, 2, 3, U, D, 8, 6, None, "SO","NO","EO","WO"):
                map_coords["4,2"]=(None, view_distance+2, view_distance)
            else:
                dungeon_playermap[party_coord[0]+2][party_coord[1]] = dungeon_blueprint[party_coord[0]+2][party_coord[1]]
                pass

        if party_facing is not None: # Print Party Facing to middle of @localmap
            if party_facing == 8:
                localmap[view_distance][view_distance] = "▲"
                # dungeon_playermap[party_coord[0]][party_coord[1]] = "▲"

            elif party_facing == 2:
                localmap[view_distance][view_distance] = "▼"
                # dungeon_playermap[party_coord[0]][party_coord[1]] = "▼"

            elif party_facing == 4:
                localmap[view_distance][view_distance] = "◄"
                # dungeon_playermap[party_coord[0]][party_coord[1]] = "◄"
            
            elif party_facing == 6:
                localmap[view_distance][view_distance] = "►"
                # dungeon_playermap[party_coord[0]][party_coord[1]] = "►"

            
        
        for key, values in map_coords.items():
            t, y, x = values
            if t == 0:
                localmap[y][x] = ' '
            elif t == 1 or t == 9 or t == N or t == S or t == W or t == E:
                localmap[y][x] = '■'
            elif t == 2 or t == 3:
                localmap[y][x] = '□'
            elif t == "U":
                localmap[y][x] = '♦'
            elif t == "D":
                localmap[y][x] = '♠'
            elif t == "C":
                localmap[y][x] = f'●'
            elif t == "O":
                localmap[y][x] = '○'
            elif t == "R":
                localmap[y][x] = '♥'
            elif t == "M":
                localmap[y][x] = '☺'
            elif t == "SO":
                localmap[y][x] = '↑'
            elif t == "NO":
                localmap[y][x] = '↓'
            elif t == "WO":
                localmap[y][x] = '→'
            elif t == "EO":
                localmap[y][x] = '←'
            elif t == 8:
                localmap[y][x] = '↕'
            elif t == 6:
                localmap[y][x] = '↔'
            elif t == None or t == "out":
                localmap[y][x] = 'X'

            elif t == f"{RED}▲{RESET}":
                localmap[y][x] = f"{RED}▲{RESET}"
            elif t == f"{RED}▼{RESET}":
                localmap[y][x] = f"{RED}▼{RESET}"
            elif t == f"{RED}◄{RESET}":
                localmap[y][x] = f"{RED}◄{RESET}"
            elif t == f"{RED}►{RESET}":
                localmap[y][x] = f"{RED}►{RESET}"
        
        #                   0       1       2       3           4           5       6           7
        # hour_names = ["Dawn","Morning","Noon","Afternoon","Twilight","Evening","Midnight","Witching Hour"]

    def restAreaCheck():
        # in_rest_area = any(area(*party_coord) for area in dungeon11_rest)
        global party_coord

        for loc in dungeon11_rest:
            if loc[0] <= party_coord[0] <= loc[1] and loc[2] <= party_coord[1] <= loc[3]:
                return True
            
        return False

            # 8 <= party_coord[0] <= 10 and 12 <= party_coord[1] <= 14

        # in_rest_area = any(restarea)

        # if in_rest_area:
        #     return True
        # else:
        #     return False


    def openDoor():
        

        if party_facing == 8:
            doorcoord = party_coord[0]-1, party_coord[1]
        elif party_facing == 4:
            doorcoord = party_coord[0], party_coord[1]-1
        elif party_facing == 2:
            doorcoord = party_coord[0]+1, party_coord[1]
        elif party_facing == 6:
            doorcoord = party_coord[0], party_coord[1]+1

        door = dungeon_blueprint[doorcoord[0]][doorcoord[1]]
        
        if door == 2:
            logText("You open the door and go through it.")
            if party_facing == 8:
                update_coord(0,-2)
            elif party_facing == 4:
                update_coord(-2,0)
            elif party_facing == 2:
                update_coord(0,2)
            elif party_facing ==6:
                update_coord(+2,0)
        
        elif door == 8 or door == 6:
            logText("You go through the passageway.")
            if party_facing == 8:
                update_coord(0,-2)
            elif party_facing == 4:
                update_coord(-2,0)
            elif party_facing == 2:
                update_coord(0,2)
            elif party_facing ==6:
                update_coord(+2,0)

        elif door == D:
            logText("The door seems to be locked.")
        elif door == 9:
            logText("You find a secret passage in the wall!")
            
            logText("You go across the passage.")
            if party_facing == 8:
                dungeon_blueprint[doorcoord[0]][doorcoord[1]] = 8
                update_coord(0,-2)
            elif party_facing == 4:
                dungeon_blueprint[doorcoord[0]][doorcoord[1]] = 6
                update_coord(-2,0)
            elif party_facing == 2:
                dungeon_blueprint[doorcoord[0]][doorcoord[1]] = 8
                update_coord(0,2)
            elif party_facing == 6:
                dungeon_blueprint[doorcoord[0]][doorcoord[1]] = 6
                update_coord(+2,0)
            else:
                logText("Nevermind.")

        elif door == NO or door == SO or door == EO or door == WO:
            if party_facing == 8 and door == SO:
                logText("You find a secret passage in the wall!")
                logText("You go across the passage.")
                update_coord(0,-2)

            elif party_facing == 8 and door == NO:
                logText("It's a one-way passage, but you can't access it from this side.")
            
            elif party_facing == 4 and door == EO:
                logText("You find a secret passage in the wall!")
                
                logText("You go across the passage.")
                update_coord(-2,0)
            elif party_facing == 4 and door == WO:
                logText("It's a one-way passage, but you can't access it from this side.")

            elif party_facing == 2 and door == NO:
                logText("You find a secret passage in the wall!")
                
                logText("You go across the passage.")
                update_coord(0,2)
            elif party_facing == 2 and door == SO:
                logText("It's a one-way passage, but you can't access it from this side.")
            
            elif party_facing == 6 and door == WO:
                logText("You find a secret passage in the wall!")

                logText("You go across the passage.")
                update_coord(+2,0)
            elif party_facing == 6 and door == EO:
                logText("It's a one-way passage, but you can't access it from this side.")
            
            else:
                logText("Nevermind.")

        elif door == N or door == S or door == E or door == W:
            
            logText("You find a secret passage in the wall!")
            if party_facing == 8 and door == S:
                update_coord(0,-2)
                dungeon_blueprint[doorcoord[0]][doorcoord[1]] = SO

            elif party_facing == 8 and door == N:
                logText("But it seems blocked from this side.")

            elif party_facing == 4 and door == E:
                dungeon_blueprint[doorcoord[0]][doorcoord[1]] = EO
                update_coord(-2,0)

            elif party_facing == 4 and door == W:
                logText("But it seems blocked from this side.")

            elif party_facing == 2 and door == N:
                update_coord(0,2)
                dungeon_blueprint[doorcoord[0]][doorcoord[1]] = NO

            elif party_facing == 2 and door == S:
                logText("But it seems blocked from this side.")

            elif party_facing == 6 and door == W:
                update_coord(+2,0)
                dungeon_blueprint[doorcoord[0]][doorcoord[1]] = WO

            elif party_facing == 6 and door == E:
                logText("But it seems blocked from this side.")

            else:
                logText("Nevermind.")
    
    def interact():
        global logtext
        global dungeon_level
        global danger

        if party_facing == 8:
            object = party_coord[0]-1, party_coord[1]
        elif party_facing == 4:
            object = party_coord[0], party_coord[1]-1
        elif party_facing == 2:
            object = party_coord[0]+1, party_coord[1]
        elif party_facing == 6:
            object = party_coord[0], party_coord[1]+1

        objecttype = dungeon_blueprint[object[0]][object[1]]

        if objecttype == "U":

            if dungeon_level == 1:
                logText("Returning to city.")
                checkExploring(False)

                danger = 0
                renpy.hide_screen("dungeon_danger")
                renpy.hide_screen("dungeon_explore")
                renpy.jump("town_scene")
                
            else:
                dungeon_level -= 1
                logText("Climbing up to higher level.")
        
        if objecttype == "D":
            logText("Climbing Down to next level.")

        if objecttype == "C":
            getLoot(object[0],object[1])

        if objecttype == "O":
            logText("There's nothing else here.")

        if objecttype == M:
            renpy.call("merchant_label")

    def getLoot(looty,lootx):

        logText("You scavenge for loot.")

        lootcoord = f"{looty},{lootx}"
        
        if lootcoord in dungeon_current_loot:
            lootitem = dungeon_current_loot[lootcoord][0]

            if lootitem.type == "Weapon" or lootitem.type == "Armor" or lootitem.type == "Accessory" or lootitem.type == "Charm":
                if len(inventory) >20:
                    logText(f"Found a {lootitem.name}, but the party's stash is full.")
                else:
                    inventory.append(copy.deepcopy(lootitem))
                    dungeon_blueprint[looty][lootx] = "O"
                    dungeon_current_loot.pop(lootcoord)
                    logText(f"Found a {lootitem.name}. Added to party's stash.")
            else:
                if len(consumables) >20:
                    logText(f"Found a {lootitem.name}. But the party stash is full.")    
                else:
                    consumables.append(copy.deepcopy(lootitem))
                    dungeon_blueprint[looty][lootx] = "O"
                    dungeon_current_loot.pop(lootcoord)
                    logText(f"Found a {lootitem.name}. Added to party's stash.")
        else:
            logText("But something in the code went wrong.\n")

    directions = {
        8: ("N", (0, -1)),
        4: ("W", (-1, 0)),
        6: ("E", (1, 0)),
        2: ("S", (0, 1))
    }


    #Game Loop

    def initializeDungeon():
        global steps
        global danger
        global danger_level
        global party_facing
        global party_coord
        global dungeon11_entry
        steps = 0
        danger = 0
        danger_level = f"None"
        party_coord[0] = dungeon11_entry[0]
        party_coord[1] = dungeon11_entry[1]
        party_facing = 2
        update_coord(0,0)



    exploring = False
    def checkExploring(option):
        global exploring
        if option == True:
            exploring = True
        if option == False:
            exploring = False
        if option == None:
            return exploring
        return exploring


    def exploreDungeon():
        global danger
        global danger_level
        global party_facing
        global party_coord
        
        danger = 0
        danger_level = f"None"
        party_coord[0] = dungeon11_entry[0]
        party_coord[1] = dungeon11_entry[1]
        party_facing = 2
        update_coord(0,0)

        checkExploring(True)

        while checkExploring(None) == True:

            if gameover(party):
                exploring = False
                break


                
                break
            if danger >= 100:
                print("Enemies have appeared!")
                input("Time to fight! (Press anything to begin)")
                danger = 0
                danger_level = f"None"
                runCombat()
                steps += rounds
                os.system("cls")
            
            getMap()


## RENPY FUNCTIONS

    def genDGPlayerMap(dungeon):
        dgplayermap = []

        for ny in range(len(dungeon)):
            dgplayermap.append([])
            for nx in range(len(dungeon[ny])):
                dgplayermap[ny].append("")

        return dgplayermap

    def turnLeft():
        global party_facing

        if party_facing == 8:
            party_facing = 4
        elif party_facing == 4:
            party_facing = 2
        elif party_facing == 2:
            party_facing = 6
        elif party_facing ==6:
            party_facing = 8

        getMap()

    def turnRight():
        global party_facing

        if party_facing == 8:
            party_facing = 6
        elif party_facing == 6:
            party_facing = 2
        elif party_facing == 2:
            party_facing = 4
        elif party_facing == 4:
            party_facing = 8

        getMap()

    def moveForwards():
        global party_facing

        if party_facing == 8:
            facing = N
            dx = 0
            dy = -1
        elif party_facing == 6:
            facing = E
            dx = 1
            dy = 0
        elif party_facing == 4:
            facing = W
            dx = -1
            dy = 0
        elif party_facing == 2:
            facing = S
            dx = 0
            dy = 1

        if facing is not None:
            if party_facing == 8:
                tilecoords = party_coord[0]-1, party_coord[1]
            elif party_facing == 4:
                tilecoords = party_coord[0], party_coord[1]-1
            elif party_facing == 2:
                tilecoords = party_coord[0]+1, party_coord[1]
            elif party_facing == 6:
                tilecoords = party_coord[0], party_coord[1]+1

            tileface = dungeon_blueprint[tilecoords[0]][tilecoords[1]]

            if tileface == 0:
                update_coord(dx,dy)
            # elif tileface in [f"{RED}▲{RESET}",f"{RED}▼{RESET}",f"{RED}◄{RESET}",f"{RED}►{RESET}"]:
            #     logText("You walk into a Làidir!")
            #     bossbattle = True
            #     runCombat()
            #     update_coord(dx,dy)
            elif tileface == 1:
                logText ("You bonk against a wall.")
            elif tileface == 2:
                logText ("There is a door in front of you.")
            elif tileface == C:
                logText ("There is a closed chest in front of you.")
            elif tileface == O:
                logText ("There is a looted chest in front of you.")
            elif tileface == U:
                logText ("These are the stairs upwards.")
            elif tileface == D:
                logText ("These are the stairs downwards.")
            elif tileface == R:
                logText ("This is a resting area, you can camp here.")
            elif tileface == M:
                logText ("This person has merchandise to sell.")
            elif tileface in (N,S,W,E):
                logText ("This seems like a one-way passageway.")
            elif tileface in (NO,SO,WO,EO):
                logText ("This seems like a one-way passageway.")
            elif tileface in (9,8,6):
                logText ("This seems like a passageway in the wall.")

        getMap()

    def interactKey():
        openDoor()
        interact()
        getMap()



#RENPY DEFAULTS 1

default party_coord = [1,1]



# DUNGEON 11 Defaults
default dungeon11_mapcompletion = 0
default dungeon11loot = {
        "1,6": (item1, 1,6),
        "2,8": (item1 ,2,8),
        "5,30": (item5, 5,30),
        "13,2": (item2 ,13,2),
        "26,4": (armor3 ,26,4),
        "15,9": (chr2 ,15,9),
        "28,8": (weapon3 ,28,8),
        "14,14": (item5 ,14,14),
        "20,14": (chr1 ,20,14),
        "11,16": (item1 ,11,16),
        "12,15": (item2 ,12,15),
        "13,16": (item2 ,13,16),
        "7,19": (item1 ,7,19),
        "12,28": (weapon4 ,12,28),
        "16,26": (item2 ,16,26),
        "17,26": (item3 ,17,26),
        "18,26": (item1 ,18,26),
        "22,26": (item2 ,22,26),
        "24,25": (item2 ,24,25),
        "25,24": (item2 ,25,24),
    }
default dungeon11 = [
        [1, U,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1], 

        [1, 0,0,0,1,0, C,1,1,1,0, E,0,0,0,0, 0,1,0,0,0, 0,0,1,0,1, 0,0,0,0,0, 1], #1
        [1, 0,0,0,2,0, 0,1,C,0,0, 1,0,1,0,1, 0,1,0,1,1, 1,0,0,0,0, 0,1,0,0,0, 1], #2
        [1, 0,0,0,1,0, 0,1,1,1,0, 1,0,1,1,1, 0,0,0,0,0, 1,1,1,1,0, 1,1,0,0,0, 1], #3
        [1, 1,1,1,1,0, 0,9,0,0,0, 1,0,1,0,1, 0,1,0,1,0, 0,1,0,1,0, 1,0,0,1,1, 1], #4
        [1, 0,0,0,0,0, 0,1,1,1,0, 1,0,1,0,1, 0,1,0,1,1, 0,1,0,0,0, 1,0,0,1,C, 1], #5
    #    0  1 2 3 4 5  6 7 8 9 10 1 2 3 4 5  6 7 8 9 20 1 2 3 4 5  6 7 8 9 30 1
        [1, 0,1,1,0,1, 1,1,0,0,0, 1,0,0,0,0, 0,1,0,0,1, 0,1,0,1,9, 1,0,1,1,0, 1],
        [1, 0,0,1,0,0, 0,1,0,1,1, 1,1,2,1,1, 1,1,0,C,1, 0,1,1,1,0, 1,0,1,1,0, 1],
        [1, 0,1,1,1,1, 0,1,0,1,1, 1,0,0,M,1, 1,1,1,1,1, 0,1,0,1,0, 1,0,9,0,0, 1],
        [1, 0,0,0,0,1, 0,0,0,0,0, 2,0,0,0,2, 0,0,0,0,0, 0,1,0,0,0, 1,0,1,1,1, 1],
        [1, 1,1,1,0,1, 0,1,0,1,1, 1,0,0,0,1, 1,1,1,1,1, 1,1,0,1,0, 1,0,0,0,0, 1], #10
    #    0  1 2 3 4 5  6 7 8 9 10 1 2 3 4 5  6 7 8 9 20 1 2 3 4 5  6 7 8 9 30 1
        [1, 0,0,0,0,1, 0,1,0,0,0, 1,1,2,1,1, C,1,0,0,0, 1,1,0,1,1, 1,1,1,1,0, 1],
        [1, 0,1,1,0,1, 0,1,1,1,0, 1,0,0,1,C, 0,0,0,0,0, 1,0,0,0,0, 0,0,C,1,0, 1],
        [1, 0,C,1,0,0, 0,1,0,0,0, 1,0,1,1,1, C,1,0,1,1, 1,0,1,1,1, 1,1,1,1,0, 1],
        [1, 0,1,1,0,1, 0,1,1,1,1, 1,0,1,C,1, 1,1,0,1,0, 0,0,1,0,0, 0,0,0,0,0, 1],
        [1, 0,0,0,0,1, 0,1,0,C,0, 1,0,1,0,0, 0,0,0,1,0, 1,0,1,0,1, 1,1,1,1,1, 1], #15
    #    0  1 2 3 4 5  6 7 8 9 10 1 2 3 4 5  6 7 8 9 20 1 2 3 4 5  6 7 8 9 30 1
        [1, 1,1,1,1,1, S,1,0,0,0, 1,0,1,1,1, 1,1,2,1,2, 1,1,1,0,1, C,0,0,2,0, 1],
        [1, 0,0,0,0,0, 0,1,1,0,1, 1,0,1,0,0, 0,2,0,0,0, 2,0,0,0,1, C,0,0,1,0, 1],
        [1, 0,1,1,1,1, 0,0,0,0,0, 0,0,1,0,1, 1,1,0,0,0, 1,1,1,0,1, C,0,0,1,2, 1],
        [1, 0,0,0,0,1, 1,1,1,0,1, 1,0,1,0,1, 0,2,0,0,0, 2,0,1,0,1, 1,1,1,1,0, 1],
        [1, 0,1,1,0,0, 0,0,1,2,1, 0,0,1,C,1, 0,1,2,1,2, 1,0,1,0,0, 0,0,0,1,0, 1], #20
    #    0  1 2 3 4 5  6 7 8 9 10 1 2 3 4 5  6 7 8 9 20 1 2 3 4 5  6 7 8 9 30 1
        [1, 0,0,1,1,1, 1,2,1,0,1, 0,1,1,1,1, 0,1,0,1,0, 1,0,1,1,1, 1,1,0,0,0, 1],
        [1, 1,0,0,0,0, 1,0,0,0,1, 0,0,0,0,0, 0,1,0,1,0, 1,0,1,0,0, C,1,1,1,1, 1],
        [1, 1,0,1,1,0, 1,1,0,1,1, 1,1,1,1,1, 1,1,0,1,0, 1,0,0,0,1, 1,1,0,0,0, 1],
        [1, 1,0,0,1,0, 0,0,0,0,0, 0,0,1,0,0, 0,0,0,1,0, 1,1,1,0,C, 1,0,0,1,0, 1],
        [1, 0,0,1,1,1, 1,1,S,1,1, 1,0,1,0,1, 1,S,1,1,0, 0,0,1,C,1, 1,0,1,1,0, 1], #25
    #    0  1 2 3 4 5  6 7 8 9 10 1 2 3 4 5  6 7 8 9 20 1 2 3 4 5  6 7 8 9 30 1
        [1, 0,0,1,C,1, 0,0,0,0,0, 1,0,1,0,1, M,0,0,1,1, 1,0,1,1,1, 0,0,1,0,0, 1],
        [1, 0,1,1,0,1, 0,1,0,1,0, 1,0,1,0,1, 0,0,0,2,0, 1,0,1,0,0, 0,1,1,2,1, 1],
        [1, 0,1,0,0,1, 0,1,C,1,0, 1,0,0,0,1, 0,0,0,1,0, 1,0,0,0,1, 1,1,0,0,0, 1],
        [1, 0,1,0,0,1, 0,1,1,1,0, 1,1,1,1,1, 1,2,1,1,0, 1,1,1,1,1, 0,2,0,0,0, 1],
        [1, 0,0,0,0,1, 0,0,0,0,0, 2,0,0,0,0, 0,0,1,1,0, 0,0,0,0,0, 0,1,0,0,D, 1], #30

        [1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1,1,1,1,1, 1]
    ]#   0  1 2 3 4 5  6 7 8 9 10 1 2 3 4 5  6 7 8 9 20 1 2 3 4 5  6 7 8 9 30 1
# default dungeon11_rest = [
#         lambda y, x: 8 <= y <= 10 and 12 <= x <= 14,
#         lambda y, x: 17 <= y <= 19 and 18 <= x <= 20,
#         lambda y, x: 1 <= y <= 3 and 1 <= x <= 3,
#     ]
# default dungeon11_rest = [
#     8 <= party_coord[0] <= 10 and 12 <= party_coord[1] <= 14,
#     17 <= party_coord[0] <= 19 and 18 <= party_coord[1] <= 20,
#     1 <= party_coord[0] <= 3 and 1 <= party_coord[1] <= 3,
# ]

default dungeon11_rest =  [
    [8,10, 12,14],
    [17,19, 18,20],
    [1,3, 1,3]
]

default dungeon_current = dungeon11
default dungeon_current_loot = dungeon11loot
default dungeon_playermap = genDGPlayerMap(dungeon11)
default mapcompletion = dungeon11_mapcompletion

## RENPY DEFAULTS

default dungeon_blueprint = dungeon11
default check = dungeon_blueprint[party_coord[0]][party_coord[1]]


###