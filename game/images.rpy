transform scenery:
    yalign 0.5
    yoffset -50
    easein 2.0 xpos -500

transform scenerydark:
    yalign 0.5
    yoffset -50
    matrixcolor TintMatrix("#334477")
    xpos -1000
    easein 2.0 xpos -500

image bg Town:
    "BG/Hundwick.png"
    zoom 1.20

image bg Tavern:
    "BG/Tavern.png"
    zoom 1.20

image bg Shop:
    "BG/Shop.png"
    zoom 1.20

image bg Arena:
    "BG/Arena.png"
    zoom 1.20

image bg Dungeon:
    "BG/Dungeon.png"
    zoom 1.20

init python:
    selected_character = None


# DUNGEON TILES

image dgfloor:
    "Map/Floor.png"
    zoom 0.5
image dgwall:
    "Map/Wall.png"
    zoom 0.5
image dgchesto:
    "Map/ChestO.png"
    zoom 0.5
image dgchestc:
    "Map/ChestC.png"
    zoom 0.5
image dgdoor:
    "Map/Door.png"
    zoom 0.5
image dgstairsu:
    "Map/StairsU.png"
    zoom 0.5
image dgstairsd:
    "Map/StairsD.png"
    zoom 0.5
image dgpassw:
    "Map/PassW.png"
    zoom 0.5
image dgpasse:
    "Map/PassE.png"
    zoom 0.5
image dgpassn:
    "Map/PassN.png"
    zoom 0.5
image dgpasss:
    "Map/PassS.png"
    zoom 0.5
image dgpassns:
    "Map/PassNS.png"
    zoom 0.5
image dgpasswe:
    "Map/PassWE.png"
    zoom 0.5
image dgmerch:
    "Map/Merch.png"
    zoom 0.5

image partyN:
    "Map/PartyN.png"
    zoom 0.5

image partyS:
    "Map/PartyS.png"
    zoom 0.5

image partyW:
    "Map/PartyW.png"
    zoom 0.5

image partyE:
    "Map/PartyE.png"
    zoom 0.5

image dgdark:
    "Map/Dark.png"
    zoom 0.5

image buttonhandidle:
    "Map/BtnHand_hover.png"
    zoom 0.7
image buttonhandhover:
    "Map/BtnHand_selected.png"
    zoom 0.7

image buttonpartyidle:
    "Map/Party_idle.png"
    zoom 0.7
image buttonpartyhover:
    "Map/Party_hover.png"
    zoom 0.7

image buttonforwidle:
    "Map/BtnU_hover.png"
    zoom 0.7
image buttonforwhover:
    "Map/BtnU_selected.png"
    zoom 0.7

image buttonbackidle:
    "Map/BtnU_hover.png"
    zoom 0.7 yzoom -1
image buttonbackhover:
    "Map/BtnU_selected.png"
    zoom 0.7 yzoom -1

image buttonleftidle:
    "Map/BtnR_hover.png"
    zoom 0.7 xzoom -1
image buttonlefthover:
    "Map/BtnR_selected.png"
    zoom 0.7 xzoom -1

image buttonrightidle:
    "Map/BtnR_hover.png"
    zoom 0.7
image buttonrighthover:
    "Map/BtnR_selected.png"
    zoom 0.7

image buttonturncwidle:
    "Map/BtnTCW_hover.png"
    zoom 0.7
image buttonturncwhover:
    "Map/BtnTCW_selected.png"
    zoom 0.7

image buttonturnccwidle:
    "Map/BtnTCW_hover.png"
    zoom 0.7
    xzoom -1
image buttonturnccwhover:
    "Map/BtnTCW_selected.png"
    zoom 0.7
    xzoom -1