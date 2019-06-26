from Kaafhet.Base.Defs import *
#from Kaafhet.Inter import Civilization #SEEN <- nop

class Base:
    """ Classe mere de Entity et Struct

        Methodes :
            getPos
            attackObj
            setCallback
    """
#{
    def __init__(self, position = Coord, civz = 42, ID = int, kindOf = float):
    #{
        meta = getMetas(kindOf)
        self.pos = position
        self.team = civz.team
        self.kind = kindOf
        self.level = 1
        self.scope = meta[SCOPE] # depend de kind # depend de level
        self.attack = meta[ATTACK] # depend de kind # depend de level
        self.life = 1 # augmente avec sa formation (up to lifemax = rady)
        self.isReady = False
        self.lifeMax = meta[LIFE] # depend de kind # depend de level
        self.isAlive = True
        #self.display

        self.civz = civz
        self.civzID = ID

        self.inventoryKind = getGroup(kindOf) # pas pour les war_x +entity
        self.inventoryQuantity = 0

        self.attackers = [] # liste de 'Base'
        self.isAttacker = False # personne ne l'attaque

        self.onAttacker = nullf
        self.onReachTag = nullf
        self.onSpawning = nullf
    #}

    def __str__(self):
        return "ID : {}, pos : {}, life : {}".format(self.civzID, self.pos, self.life)

    def getPos(self):
        return self.pos.cpy()

    def attackObj(self, obj): # l'event peut etre reperer par {is/on}Attacker
        """ NO YOU DONT
            False si ded

            Attaque l'objet
                s'ajoute a sa liste d'attaquant
                met isAttacker a True (POUR L'OBJET)
                (et provoque l'appel a onAttacker POUR L'OBJET)
        """
        if not self.isAlive or not obj.isAlive:
            return False

        obj.isAttacker = True
        if not self in obj.attackers:
            obj.attackers.append(self)
        obj.life-= self.attack
        return obj.life <= 0

    #TODO : nop, c'est lourd
#    def setCallback(self, callbacks):
#        self.onAttacker = callbacks.get("onAttacker", nullf)
#        self.onReachTag = callbacks.get("onReachTag", nullf)
#        self.onSpawning = callbacks.get("onSpawning", nullf)

    def setCallback(self, onAttacker=None, onReachTag=None, onSpawning=None):
        """ Modifier les fonctions appelees sur evenements

            Definitions :
                onAttacker(self, attackers)
                onReachTag(self, pos)
                onSpawning(self)
        """
        if onAttacker: self.onAttacker = onAttacker
        if onReachTag: self.onReachTag = onReachTag
        if onSpawning: self.onSpawning = onSpawning
#}
