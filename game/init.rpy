#########################
# Character Declaration #
#########################
#IMPORTANT CHARACTERS
define yum = Character("Yumi", color="#FFFFFF", voice_tag="yum", callback=speaker("yumi"))
define kam = Character("Kamika", color="#FFFFFF", voice_tag="kam", dynamic=True, callback=speaker("kamika"))
define sta = Character("Stacey", color="#FFFFFF", voice_tag="sta", callback=speaker("stacey"))
define luc = Character("Lucca", color="#FFFFFF", voice_tag="yum", dynamic=True, callback=speaker("lucca"))
define lev = Character("Levi", color="#FFFFFF", voice_tag="lev", callback=speaker("levi"))
define moe = Character("Moe", color="#FFFFFF", voice_tag="moe", callback=speaker("moe"))
define sat = Character("S-Tan", color="#FFFFFF", voice_tag="sat", callback=speaker("satan"))

init:
    $ luc_name = "???"
    $ kam_name = "???"

init python:
    DefineImages('bgs', prepend='bg')
    DefineImages('cgs', prepend='cg')
    layerorder = ['base','mouth','eyes','brow','optional']
    DefineImages("sprites", overrideLayerOrder=layerorder)

        #use map emotes to compile complex emotions with layers
    MapEmote('sta neutral', 'sta base md default ed default brow default')

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
