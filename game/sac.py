# -*- coding: latin-1 -*-
"""
Created on Mon Feb 22 15:48:15 2016

@author: Celestin
"""

from Inter import *

TEAM_ENEMY = WHILD
mainGoal = None
hasDefend = False

def defend(this, attacker):
    global mainGoal, hasDefend
    if not hasDefend:
        hasDefend = True
        mainGoal = attacker
        sac.forEachEntity(Entity.removeAllGoal)
        sac.forEachEntity(attack)

def attack(this):
    global mainGoal
    this.addGoal(mainGoal)

def once():
    global TEAM_ENEMY
    if sac.team == TEAM_1:
        TEAM_ENEMY = TEAM_2
    elif sac.team == TEAM_2:
        TEAM_ENEMY = TEAM_1

    sac.getTownHall().setCallback(onAttacker=defend)

def loop(turn):
    if sac.waffle >= 20:
        sac.newEntity()

    isGlobalGoal = 0
    for it in sac.entities:
        isGlobalGoal+= int(it.isGoal)

    global mainGoal, hasDefend
    if not isGlobalGoal and hasDefend:
        mainGoal = sac.getTeamTownHall(TEAM_ENEMY)
        sac.forEachEntity(attack)

sac = c(loop, once, "sac", p(16, 16))
