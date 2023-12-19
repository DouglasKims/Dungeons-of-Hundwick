## All effects go here!
init python:
    import math


    def applyEffect (caster, effect, char):

        if "enha" in effect:
            effectvalue = (math.sqrt(caster.tec)/10+1) * 5 * caster.slist[effect][0]
        elif "enfe" in effect:
            effectvalue = ((math.sqrt(caster.tec)/10+1) * 5 * caster.slist[effect][0]) * -1


        # ENHA
        if "enha" in effect:
            char.effects.update({effect: [effectvalue, 4]})
            if effect == "enhast":
                char.str += effectvalue
                
            elif effect == "enhate":
                char.tec += effectvalue
            
            elif effect == "enhavi":
                char.vit += effectvalue

            elif effect == "enhagi":
                char.agi += effectvalue

            elif effect == "enhalk":
                char.lck += effectvalue

        # ENFE
        if "enfe" in effect:
            char.effects.update({effect: [effectvalue, 4]})
            if effect == "enfest":
                char.str += effectvalue
                
            elif effect == "enfete":
                char.tec += effectvalue
            
            elif effect == "enfevi":
                char.vit += effectvalue

            elif effect == "enfegi":
                char.agi += effectvalue

            elif effect == "enfelk":
                char.lck += effectvalue

        # PROTECT
        if "protect" in effect:
            char.effects.update({effect: [caster.slist[effect][0], math.ceil(caster.slist[effect][0]/3)+1]})
            pass

        # TAUNT
        if "taunt" in effect:
            threat_increase = caster.slist[effect][0] * 5
            stat_increase = caster.slist[effect][0]//2 * 2
            caster.effects.update({effect: [[threat_increase,stat_increase], 4]})
            caster.threat += threat_increase
            caster.vit += stat_increase
            caster.tec += stat_increase
            pass

        # COATING
        if "coating" in effect:
            char.effects.update({effect: [caster.slist[effect][0], math.ceil(caster.slist[effect][0]/3)+1]})
            pass


    def tickEffect (char):

        effect_keys = list(char.effects.keys())

        for n in effect_keys:
            # Reduces effect duration by 1
            char.effects[n][1] -= 1
            

            if char.effects[n][1] == 0:
                
                # Revert de/buffs from effects
                if n == "enhast":
                    char.str -= char.effects[n][0]
                elif n == "enhate":
                    char.tec -= char.effects[n][0]
                elif n == "enhavi":
                    char.vit -= char.effects[n][0]
                elif n == "enhagi":
                    char.agi -= char.effects[n][0]
                elif n == "enhalk":
                    char.lck -= char.effects[n][0]

                elif n == "enfest":
                    char.str -= char.effects[n][0]
                elif n == "enfete":
                    char.tec -= char.effects[n][0]
                elif n == "enfevi":
                    char.vit -= char.effects[n][0]
                elif n == "enfegi":
                    char.agi -= char.effects[n][0]
                elif n == "enfelk":
                    char.lck -= char.effects[n][0]
                
                elif n == "taunt":
                    char.threat -= char.effects[n][0][0]
                    char.vit -= char.effects[n][0][1]
                    char.tec -= char.effects[n][0][1]
                
                char.effects.pop(n)

## 