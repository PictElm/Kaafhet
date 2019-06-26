# -*- coding: latin-1 -*-
"""
Created on Mon Feb 22 15:48:15 2016

@author: Celestin
"""

from Kaafhet.Inter import *

def loop(turn):
    if sac.waffle >= 20:
        sac.newEntity()
    elif not sac.getLastEntity().isGoal:
        for it in sac.entities:
            it.addGoal(sac.getTeamTownHall(TEAM_2))

sac = c(loop, nullf, "sac", p(16, 16))
