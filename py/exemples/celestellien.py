# -*- coding: latin-1 -*-
"""
Created on Mon Feb 22 15:37:51 2016

@author: Celestin
"""

from Inter import *

def angelicOnAttkd(attacked, attacker):
    print "{} is attacked by {} of team {}\
    ".format(attacked.civzID, attacker.civzID, attacker.team)
    for it in celestellien.entities:
        it.addGoal(attacker)

def angelicOnReach(entity, position):
    print "{} reach {}".format(entity.civzID, position)

def angelicStart():
    for it in celestellien.entities:
        it.setCallback(angelicOnAttkd, angelicOnReach)
    for it in celestellien.structs:
        it.setCallback(angelicOnAttkd, angelicOnReach)

# fonction principale
def angelicCivilCode(turn):
    if celestellien.waffle >= 20:
        celestellien.newEntity().setCallback(angelicOnAttkd, angelicOnReach)

celestellien = Civilization(angelicCivilCode, angelicStart, p(4,2))
