# -*- coding: latin-1 -*-
"""
Created on Mon Feb 22 15:37:08 2016

@author: Celestin
"""

from Kaafhet.Inter import register, run, makeDefaultWorld, counter, display

from sac import sac
from gro import gro

register(sac)
register(gro)

run(makeDefaultWorld(), counter, display)
