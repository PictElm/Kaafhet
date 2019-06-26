# -*- coding: latin-1 -*-
"""
Created on Thu Mar 10 17:41:37 2016

@author: Celestin
"""

from Inter import *

TEAM_ENEMY = WHILD

def once():
    global TEAM_ENEMY
    if gro.team == TEAM_1:
        TEAM_ENEMY = TEAM_2
    elif gro.team == TEAM_2:
        TEAM_ENEMY = TEAM_1

def loop(turn):
    if gro.waffle >= 20:
        gro.newEntity()
    elif gro.getLastEntity():
        if not gro.getLastEntity().isGoal:
            for it in gro.entities:
                it.addGoal(gro.getTeamTownHall(TEAM_ENEMY))
            #gro.forEachEntity(lambda this: this.addGoal(gro.getTeamTownHall(TEAM_ENEMY)))


gro = c(loop, once, "gro", p(32, 32))
