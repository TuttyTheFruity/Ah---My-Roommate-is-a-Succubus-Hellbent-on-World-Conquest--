#########################
# Character Declaration #
#########################
#IMPORTANT CHARACTERS
define yum = Character("Yumi", color="#FFFFFF", voice_tag="yum", callback=speaker("yumi"))
define kam = Character("Kamika", color="#FFFFFF", voice_tag="kam", callback=speaker("kamika"))
define sta = Character("Stacey", color="#FFFFFF", voice_tag="sta", callback=speaker("stacey"))
define luc = Character("Lucca", color="#FFFFFF", voice_tag="luc", callback=speaker("lucca"))
define lev = Character("Levi", color="#FFFFFF", voice_tag="lev", callback=speaker("levi"))
define moe = Character("Moe", color="#FFFFFF", voice_tag="moe", callback=speaker("moe"))
define sat = Character("S-Tan", color="#FFFFFF", voice_tag="sat", callback=speaker("satan"))

init:
    $ luc_name = "Weird Exchange Student"
    $ kam_name = "???"

init python:
    DefineImages('bgs', prepend='bg')
    DefineImages('cgs', prepend='cg')
    layerorder = ['base','mouth','eyes','brow','cry', 'glasses', 'optional']
    DefineImages("sprites", overrideLayerOrder=layerorder)

        #use map emotes to compile complex emotions with layers

    #STACEY
    MapEmote('stacey smugclosed', 'stacey base md default ec default brow default')
    MapEmote('stacey smug', 'stacey base md default ed default brow default')
    MapEmote('stacey confused', 'stacey base md flat ed default brow raised')
    MapEmote('stacey neutral', 'stacey base md sad ed default brow default')
    MapEmote('stacey neutrallook', 'stacey base md sad ed side brow default')
    MapEmote('stacey smuglook', 'stacey base md default ed side brow default')
    MapEmote('stacey grinclosed', 'stacey base mc grin ec default side brow default')
    MapEmote('stacey grin', 'stacey base mc grin ed default brow default')
    MapEmote('stacey sarcasticlook', 'stacey base md think ed side brow raised')
    MapEmote('stacey sarcastic', 'stacey base md think ed default brow raised')
    MapEmote('stacey eyebrow', 'stacey base md sad ed default brow raised')
    MapEmote('stacey sad', 'stacey base md sad ed default brow sad')
    MapEmote('stacey sadclosed', 'stacey base md sad ec default brow sad')
    MapEmote('stacey therock', 'stacey base md default ed default brow raised')

    #KAMIKA LOOKING AT READER, HUMAN DISGUISE
    MapEmote('kamika u thinkingclosed', 'kamika pose1 public md default ec default brow furrow')
    MapEmote('kamika u thinking', 'kamika pose1 public md default ed default brow furrow')
    MapEmote('kamika u evilgrin', 'kamika pose1 public mc grin ed squint brow mad')
    MapEmote('kamika u surprise', 'kamika pose1 public m shout ed default brow surprise')
    MapEmote('kamika u angrysurprise', 'kamika pose1 public m shout ed default brow mad')
    MapEmote('kamika u shout', 'kamika pose1 public md mad ed default brow mad optional angryvein')
    MapEmote('kamika u glare', 'kamika pose1 public md sad ed squint brow mad')
    MapEmote('kamika u shoutclosed', 'kamika pose1 public md mad ec default brow mad optional angryvein')
    MapEmote('kamika u mad', 'kamika pose1 public md mad ed default brow mad')
    MapEmote('kamika u madclosed', 'kamika pose1 public md mad ec default brow mad')
    MapEmote('kamika u confident', 'kamika pose1 public md happy ed default brow mad')
    MapEmote('kamika u smugclosed', 'kamika pose1 public md happy ec default brow sad')
    MapEmote('kamika u smug', 'kamika pose1 public md happy ed default brow sad')
    MapEmote('kamika u smugsquint', 'kamika pose1 public md happy ed squint brow sad')
    MapEmote('kamika u wideeyes', 'kamika pose1 public md default ed squint brow surprise')
    MapEmote('kamika u happyclosed', 'kamika pose1 public md happy ec happy brow surprise')
    MapEmote('kamika u happy', 'kamika pose1 public md happy ed happy brow surprise')
    MapEmote('kamika u sigh', 'kamika pose1 public md mad happy ec default brow sad')
    #PAST THIS POINT IS NEW SHIT

    #KAMIKA LOOKING AT READER (DEMON FORM)
    MapEmote('kamika d thinkingclosed', 'kamika pose1 base md default ec default brow furrow')
    MapEmote('kamika d thinking', 'kamika pose1 base md default ed default brow furrow')
    MapEmote('kamika d evilgrin', 'kamika pose1 base mc grin ed squint brow mad')
    MapEmote('kamika d surprise', 'kamika pose1 base m shout ed default brow surprise')
    MapEmote('kamika d angrysurprise', 'kamika pose1 base m shout ed default brow mad')
    MapEmote('kamika d shout', 'kamika pose1 base md mad ed default brow mad optional angryvein')
    MapEmote('kamika d glare', 'kamika pose1 base md sad ed squint brow mad')
    MapEmote('kamika d shoutclosed', 'kamika pose1 base md mad ec default brow mad optional angryvein')
    MapEmote('kamika d mad', 'kamika pose1 base md mad ed default brow mad')
    MapEmote('kamika d madclosed', 'kamika pose1 base md mad ec default brow mad')
    MapEmote('kamika d confident', 'kamika pose1 base md happy ed default brow mad')
    MapEmote('kamika d smugclosed', 'kamika pose1 base md happy ec default brow sad')
    MapEmote('kamika d smug', 'kamika pose1 base md happy ed default brow sad')
    MapEmote('kamika d smugsquint', 'kamika pose1 base md happy ed squint brow sad')
    MapEmote('kamika d wideeyes', 'kamika pose1 base md default ed squint brow surprise')
    MapEmote('kamika d happyclosed', 'kamika pose1 base md happy ec happy brow surprise')
    MapEmote('kamika d happy', 'kamika pose1 base md happy ed happy brow surprise')
    MapEmote('kamika d sigh', 'kamika pose1 base md mad happy ec default brow sad')
    #PAST THIS POINT IS NEW SHIT

    #KAMIKA LOOKING AWAY

    #LUCCA
    MapEmote('lucca neutral', 'lucca base md default ed default brow default')
    MapEmote('lucca nervous', 'lucca base md default ed default brow sad')
    MapEmote('lucca nervousopen', 'lucca base m default ed default brow sad')
    MapEmote('lucca nervousclose', 'lucca base md default ec default brow sad')
    MapEmote('lucca nervouser', 'lucca base md default ed default brow sadder')
    MapEmote('lucca nervouseropen', 'lucca base m default ed default brow sadder')
    MapEmote('lucca sigh', 'lucca base m sad ec default brow sad')
    MapEmote('lucca uwah', 'lucca base m uwah ec uwah brow sad')
    MapEmote('lucca doh', 'lucca base mc default ec uwah brow sadder blush')

    #MOE
    MapEmote('moe neutral', 'moe base md default ed default brow default')
    MapEmote('moe neutrallook', 'moe base md default ed side brow default')
    MapEmote('moe squint', 'moe base md default ed squint brow default')
    MapEmote('moe neutralclosed', 'moe base md default ec default brow default')
    MapEmote('moe madside', 'moe base md default ed side brow mad')
    MapEmote('moe mad', 'moe base md default ed default brow mad')
    MapEmote('moe sigh', 'moe base md default ec default brow sad')
    MapEmote('moe sighsweat', 'moe base md default ec default brow sad optional sweatdrop')



#MINOR CHARACTERS
define dee = Character('Mr. Deeks', color="#FFFFFF", voice_tag="dee")
define ber = Character('Mrs. Bernardinelli', color="#FFFFFF", voice_tag="ber")
define mst = Character('Male Student', color="#FFFFFF", voice_tag="mst")
define fst = Character('Female Student', color="#FFFFFF", voice_tag="fst")
define pg1 = Character('Partygoer 1', color="#FFFFFF", voice_tag="pg1")
define pg2 = Character('Partygoer 2', color="#FFFFFF", voice_tag="pg2")

######################
# Flags              #
######################

$ minion = False
$ sawstacey = False
$ helpkamika = False
$ kamika_points = 0
$ stacey_points = 0
$ lucca_points = 0

######################
# Sprite Declaration #
######################

##################
# BG Declaration #
##################

###################
# CGs             #
###################

#FULL CGS

#MINOR CGS
image transformdemon = "cgs/transformdemon.png"
image transformhuman = "cgs/transformhuman.png"

#######
# VFX #
#######

###################
# SFX             #
###################

###################
# Music           #
###################
label start:
    jump scene1
