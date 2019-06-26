# -*- coding: latin-1 -*-
"""
Created on Mon Feb 22 15:38:28 2016

@author: Celestin
"""

from Kaafhet.Inter import *

def humanOnAttkd(attacked, attacker):
    print("{} is attacked by {} of team {}"
            .format(attacked.civzID, attacker.civzID, attacker.team))

def humanOnReach(entity, position):
    print("{} reach {}".format(entity.civzID, position))

def humanStart():
    for it in human.entities:
        it.setCallback(humanOnAttkd, humanOnReach)
    for it in human.structs:
        it.setCallback(humanOnAttkd, humanOnReach)

# fonction principale
def humanCivilCode(turn):
    if turn == 1:
        human.entities[0].addGoal(human.getTeamTownHall(TEAM_1))
    elif turn == 3:
        human.entities[1].addGoal(human.getTeamTownHall(TEAM_1))

human = c(humanCivilCode, humanStart, "humain", p(7, 8))
