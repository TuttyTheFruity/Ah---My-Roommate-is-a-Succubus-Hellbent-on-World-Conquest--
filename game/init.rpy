#########################
# Character Declaration #
#########################
#IMPORTANT CHARACTERS
define yum = Character("Yumi", color="#FFFFFF", voice_tag="yum", callback=speaker("yum"))
define kam = Character("Kamika", color="#FFFFFF", voice_tag="kam", dynamic=True, callback=speaker("kam"))
define sta = Character("Stacey", color="#FFFFFF", voice_tag="sta", callback=speaker("sta"))
define luc = Character("Lucca", color="#FFFFFF", voice_tag="yum", dynamic=True, callback=speaker("luc"))
define lev = Character("Levi", color="#FFFFFF", voice_tag="lev", callback=speaker("lev"))
define moe = Character("Moe", color="#FFFFFF", voice_tag="moe", callback=speaker("moe"))
define sat = Character("S-Tan", color="#FFFFFF", voice_tag="sat", callback=speaker("sat"))

init:
    $ luc_name = "???"
    $ kam_name = "???"

init python:
    DefineImages('bgs', prepend='bg')
    DefineImages('cgs', prepend='cg')
    DefineImages("sprites")

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
