#enum #define
CIVILIZATIONS = 0
WAR_WALKERS = 1
WAR_MACHINES = 2
WAFFLES = 3
WOODS = 4
ORES = 5

RESSOURCE  = 0.0
NAT_ENTITY = 0.1
NAT_STRUCT = 0.2
CIV_ENTITY = 0.3
CIV_STRUCT = 0.4

# si plusieur objets on le meme identifient
def EXTEND(wut = int): return wut/100

#void_entity
TAG             = CIVILIZATIONS +RESSOURCE # marqueur de destination pour Entity.goal

#civiz
CIVIL           = CIVILIZATIONS +CIV_ENTITY
TOWN_HALL       = CIVILIZATIONS +CIV_STRUCT

#war_wallker
SOLDIER         = WAR_WALKERS   +CIV_ENTITY     +EXTEND(0)
BOWMAN          = WAR_WALKERS   +CIV_ENTITY     +EXTEND(1)
HORSEMAN        = WAR_WALKERS   +CIV_ENTITY     +EXTEND(2)
BARRACK         = WAR_WALKERS   +CIV_STRUCT

#war_machine
RAM             = WAR_MACHINES  +CIV_ENTITY     +EXTEND(0)
CATTAPULTE      = WAR_MACHINES  +CIV_ENTITY     +EXTEND(1)
SIEGE_MACHINE   = WAR_MACHINES  +CIV_STRUCT

#waffles
WAFFLE          = WAFFLES       +RESSOURCE
SHEEP           = WAFFLES       +NAT_ENTITY
SHOAL           = WAFFLES       +NAT_STRUCT     +EXTEND(0)
BUSH            = WAFFLES       +NAT_STRUCT     +EXTEND(1)
FARMER          = WAFFLES       +CIV_ENTITY
FARME           = WAFFLES       +CIV_STRUCT

#wood
WOOD            = WOODS         +RESSOURCE
TREE            = WOODS         +NAT_STRUCT
LUMBERJACK      = WOODS         +CIV_ENTITY
CARPENTRY       = WOODS         +CIV_STRUCT

#ore
STONE           = ORES          +RESSOURCE      +EXTEND(0)
IRON            = ORES          +RESSOURCE      +EXTEND(1)
GOLD            = ORES          +RESSOURCE      +EXTEND(2)
ORE_STONE       = ORES          +NAT_STRUCT     +EXTEND(0)
ORE_IRON        = ORES          +NAT_STRUCT     +EXTEND(1)
ORE_GOLD        = ORES          +NAT_STRUCT     +EXTEND(2)
MINER           = ORES          +CIV_ENTITY
FOUNDRY         = ORES          +CIV_STRUCT

#meta_id
COST                   = 0 # list int : [waffles, wood, stone, iron, gold]
LIFE                   = 1 # int
SCOPE                  = 2 # float
ATTACK                 = 3 # int ou float

SPEED                  = 4 # int ou float
APTITUDE               = 5 # list int : [waffles, wood, stone, iron, gold]

SIZE                   = 4 # int

def getGroup(wut): return int(wut)              #retourne ]x].xx
def getForm(wut): return round(wut, 1)-int(wut) #retourne x[.x]x
def getMetas(wut):                              #retourne details
    """ Caracteristiques de wut

        Sous forme de liste, indices :
            COST
            LIFE
            SCOPE
            ATTACK

            SPEED
            APTITUDE

            SIZE
    """
    r = list(range(6)) # voir #meta_id pour trouver chaque donnees
    if getForm(wut) == NAT_ENTITY or getForm(wut) == CIV_ENTITY:
        if wut == CIVIL:
            r[COST] = [20, 0, 0, 0, 0]
            r[LIFE] = 20
            r[SCOPE] = 0.5
            r[ATTACK] = 1
            r[SPEED] = 1
            r[APTITUDE] = [1, 1, 1, 1, 1]

    elif getForm(wut) == NAT_STRUCT or getForm(wut) == CIV_STRUCT:
        if wut == TOWN_HALL: #SEEN on peut pas en construire d'autres
            r[COST] = [0, 0, 0, 0, 0]
            r[LIFE] = 80
            r[SCOPE] = 0.5
            r[ATTACK] = 0
            r[SIZE] = p(2, 2)
    #TODO : completer
    #SEE
    return r

#teams
WHILD  = 0
TEAM_1 = 1
TEAM_2 = 2
TEAM_3 = 3
TEAM_4 = 4

##actions a effectuer lorsque goal est atteint
#DROP_RESSOURCE  = -1
#GET_RESSOURCE   = 1
#ATTACK          = 1
##SEEN HEAL            = -1
#UPGRADE         = 4
# au_tomates : une seule action possible suivant goal

from math import sqrt
class Coord:
    """ Classe modelisant un vecteur ou une position

        Attention au instances pointeur !
        deux objets ne doivent pas avoir les memes cordonees

        Methodes :
            cpy

            getVector
            getUnitVector

            getDistanceStraight
            getDistancePath
    """
#{
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "({}; {})".format(round(self.x, 2), round(self.y, 2))

    def cpy(self):
        """ retourne une copie pour eviter les passages de pointeurs
        """
        return p(self.x, self.y) # par copy

    def getVector(self, head):
        """ retourne le vecteur self -> head
        """
        return p(head.x-self.x, head.y-self.y)

    def getUnitVector(self, head, lenth = 1):
        """ retourne un vecteur unitaire orienter self -> head
        """
        ln = self.getDistanceStraight(head)
        return p(lenth* (head.x-self.x)/ln, lenth* (head.y-self.y)/ln)

    def getDistanceStraight(self, goal):
        """ retourne la distance a vol de piaf
        """
        return sqrt((self.x-goal.x)**2 + (self.y-goal.y)**2)

    def getDistancePath(self, goal): # TODO : path
        """ retourne la distance en utilisant le moteur de pathfinding
        """
        return #SEE
#}s
def p(x, y):
    """ Voir Coord
    """
    return Coord(x, y) # creer un point coord(x; y)

def nullf(a = 0, b = 0, c = 0): # fnc vide
    pass #lel
    return
