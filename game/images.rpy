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

transform blur:
    easein 1.0 blur 5.0 matrixcolor TintMatrix("#1e1f20")

transform unblur:
    blur 5.0
    easein 2.0 blur 0.0 matrixcolor TintMatrix("#ffffff00")

transform unblurdark:
    blur 5.0
    easein 2.0 blur 0.0 matrixcolor TintMatrix("#334477")

transform enemydie:
    easein 1.0 blur 5.0 alpha 0.0

image bg Town:
    "BG/Hundwick.webp"
    zoom 1.20

image bg Tavern:
    "BG/Tavern.webp"
    zoom 1.20

image bg Shop:
    "BG/Shop.webp"
    zoom 1.20

image bg Arena:
    "BG/Arena.webp"
    zoom 1.20

image bg Dungeon:
    "BG/Dungeon.webp"
    zoom 1.20

init python:
    selected_character = None


# DUNGEON TILES

image dgfloor:
    "Map/Floor.webp"
    zoom 0.5
image dgwall:
    "Map/Wall.webp"
    zoom 0.5
image dgchesto:
    "Map/ChestO.webp"
    zoom 0.5
image dgchestc:
    "Map/ChestC.webp"
    zoom 0.5
image dgdoor:
    "Map/Door.webp"
    zoom 0.5
image dgstairsu:
    "Map/StairsU.webp"
    zoom 0.5
image dgstairsd:
    "Map/StairsD.webp"
    zoom 0.5
image dgpassw:
    "Map/PassW.webp"
    zoom 0.5
image dgpasse:
    "Map/PassE.webp"
    zoom 0.5
image dgpassn:
    "Map/PassN.webp"
    zoom 0.5
image dgpasss:
    "Map/PassS.webp"
    zoom 0.5
image dgpassns:
    "Map/PassNS.webp"
    zoom 0.5
image dgpasswe:
    "Map/PassWE.webp"
    zoom 0.5
image dgpasssecret:
    "Map/PassSecret.webp"
    zoom 0.5
image dgmerch:
    "Map/Merch.webp"
    zoom 0.5

image partyN:
    "Map/PartyN.webp"
    zoom 0.5

image partyS:
    "Map/PartyS.webp"
    zoom 0.5

image partyW:
    "Map/PartyW.webp"
    zoom 0.5

image partyE:
    "Map/PartyE.webp"
    zoom 0.5

image dgdark:
    "Map/Dark.webp"
    zoom 0.5

image buttonmapidle:
    "Map/Btnmapidle.webp"
    zoom 0.7

image buttonmaphover:
    "Map/Btnmaphover.webp"
    zoom 0.7

image buttonhandidle:
    "Map/BtnHand_hover.webp"
    zoom 0.7
image buttonhandhover:
    "Map/BtnHand_selected.webp"
    zoom 0.7

image buttonpartyidle:
    "Map/Party_idle.webp"
    zoom 0.7
image buttonpartyhover:
    "Map/Party_hover.webp"
    zoom 0.7

image buttonforwidle:
    "Map/BtnU_hover.webp"
    zoom 0.7
image buttonforwhover:
    "Map/BtnU_selected.webp"
    zoom 0.7

image buttonbackidle:
    "Map/BtnU_hover.webp"
    zoom 0.7 yzoom -1
image buttonbackhover:
    "Map/BtnU_selected.webp"
    zoom 0.7 yzoom -1

image buttonleftidle:
    "Map/BtnR_hover.webp"
    zoom 0.7 xzoom -1
image buttonlefthover:
    "Map/BtnR_selected.webp"
    zoom 0.7 xzoom -1

image buttonrightidle:
    "Map/BtnR_hover.webp"
    zoom 0.7
image buttonrighthover:
    "Map/BtnR_selected.webp"
    zoom 0.7

image buttonturncwidle:
    "Map/BtnTCW_hover.webp"
    zoom 0.7
image buttonturncwhover:
    "Map/BtnTCW_selected.webp"
    zoom 0.7

image buttonturnccwidle:
    "Map/BtnTCW_hover.webp"
    zoom 0.7
    xzoom -1
image buttonturnccwhover:
    "Map/BtnTCW_selected.webp"
    zoom 0.7
    xzoom -1