from Base.Entity import Entity, e
from Base.Struct import Struct, s

from Base.Civz import Civilization, c
from Base.Land import Land

from Base.Draw import display
from Base.Defs import *

wilderness = Civilization(nullf, nullf, "whild", p(0, 0)) # dath team

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

turn = 0

def counter(): # fnc temporaire : compte des tours + arret au bout de x? tours
    """ osef
    """
    global turn, isMainLoop
    if isMainLoop:
        turn+= 1
        print "\n\tturn {}".format(turn)
    return turn > 100-1

def getTurn(): # renvoie le nombre de tours passes (premier tour : 1)
    """ Numero du toure acctuel

        Premier tour a 1
    """
    global turn
    return turn

civiList = [wilderness]
isMainLoop = False

def register(civz = Civilization): # ajouter une civilization
    """ Rajoute une equipe si la partie n'a pas commencer

        Creer les deux entitees et la structure disponible de base
    """
    global civiList, isMainLoop
    if not isMainLoop:
        civz.team = len(civiList)#+1? # set sa team

        # cree les entitees et structures de base #TODO : d
        for it in civz.entities:
            it.team = civz.team
        for it in civz.structs:
            it.team = civz.team

        civiList.append(civz)

def createLandscapes(settings=((.5, .5, .5, .5, .5, .5), (.5))):
    """ create and return a landscape
        you can adjust settings, but I won't bother doc'ing it
    """
    landscape = Land((8, 8))

    landscape.generateRandomStructures(settings[0])
    landscape.spawnRandomEntities(settings[1])

    return landscape

def makeDefaultWorld():
    return (civiList, createLandscapes())

def run(world, stopCondition, displayFunction): # boucle principale
    """ Boucle princiale

        Quite si la fonction stopCondition retourne True

        world = (civz_list, landscape)
    """
    global isMainLoop
    civiList, landscape = world

    print "start", "\n"
    for it in civiList:
        print it, "\n"

    for it in civiList:
        if not isinstance(it, Civilization):
            continue
        it.feu(civiList)

    isMainLoop = True
    while not stopCondition():
        displayFunction(world)

        for i in range(len(civiList)):
            it = civiList[i]

            if not isinstance(it, Civilization):
                continue
            print "> team {} :".format(it.name)

            if it.autorun():
                it.run(getTurn())
            else:
                print "\n '-> removing civz (ded)"
                civiList[i] = None # override civz if town_hall destroyed (autorun=False)

    for it in civiList:
        print it, "\n"
    print "\n", "end"