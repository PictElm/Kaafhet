from Kaafhet.Base import Base
from Kaafhet.Base.Defs import *

class Entity(Base.Base):
    """ Entite autonome se deplace librement selon les mecaniques de pathfinding

        Methodes :
            addGoal
            removeLastGoal
            removeAllGoal
            interract
            die
            run
    """
#{
    def __init__(self, position = Coord, civz = 42, ID = int, kindOf = float):
    #{
        if kindOf == TAG:
            self.kind = kindOf
            self.pos = position

        else:
            Base.Base.__init__(self, position, civz, ID, kindOf)
            meta = getMetas(kindOf)
            self.speed = meta[SPEED] # depend de kind # depend de level
            self.goal = []
            #SEEN ?: #self.actions = [] # none # dispensable
            self.isGoal = False # aucun but dans la vie
    #}

    #TODO : all
    def addGoal(self, goal):#, whatFor = ['g', 00] # goal : Coord ou Base
        """ Ajoute un but ou une destination

            Si goal est instances de Pos, ajoute une entite TAG
        """
    #{
        if not self.isAlive:
            return False

        self.isGoal = True # il a un but
        if isinstance(goal, Coord):
            # cree une entity temp (kind = TAG) marqueur
            self.goal.append(e(goal, 0, 0, TAG))
            #self.actions.append(DROP_RESSOURCE+EXTEND(0))

        elif isinstance(goal, Base.Base):
            self.goal.append(goal)
            #self.actions.append(action)

        else:
            for it in goal:
                self.goal.append(it)
            #raise TypeError("wrong instance in addGoal(goal)")
        print("goal added")
    #}
    def removeLastGoal(self):
        """ Retire le dernier but de l'entite
        """
        if self.isGoal:
            self.goal.pop(-1)
            if len(self.goal) == 0:
                self.isGoal = False
    def removeAllGoal(self):
        """ Retire touts les buts de l'entite
        """
        if self.isGoal:
            self.goal = [] # aucun but
            self.isGoal = False

    def interract(self, goal):# True si fin d'interraction (ded, ect...)
        """ NO YOU DONT

            Interractions fondamentales
                - atteindre une destinnation (appel onReachTag)
                - utiliser les batiments aliers (voir Struct.use)
                - recolter les ressources (si c'est une entity ded direct ?)
                - sinon frapper
        """
    #{
        if not self.isAlive:
            return False

        if goal.kind == TAG:
            print("reach {}".format(goal.pos))
            self.onReachTag(self, goal.pos)
            return True

        if goal.team == self.team:
            print("reach {}".format(goal.pos)) #SEE mise en sakizon
            return True #TODO : all #SEE #USE : Struct.use

        elif goal.team == WHILD: #SEE : mm si c'est une entity ?
            apt = getMetas(self.kind)[APTITUDE]
            if getGroup(goal.kind) == WAFFLES:
                harvest = apt[0]
            elif getGroup(goal.kind) == WOODS:
                harvest = apt[1]
            elif goal.kind == ORE_STONE:
                harvest = apt[2]
            elif goal.kind == ORE_IRON:
                harvest = apt[3]
            elif goal.kind == ORE_GOLD:
                harvest = apt[4]
            else: harvest = 0

            goal.life-= harvest
            dif = 0
            r = False
            if goal.life <= 0: # si il a retirer plus qu'il n'en restait
                dif = abs(goal.life)
                r = True # ressources epuisees
            # si l'inventaire ne correspond pas, les ressources sont perdu
            if getGroup(self.inventoryKind) != getGroup(goal.kind):
                self.inventoryQuantity+= harvest-dif
            return r

        else: # kill 'em all
            return self.attackObj(goal)

        return False
    #}

    def die(self): # init^-1
        """ NO YOU DONT

            reset l'entitee
            a une forme de vie type algue ~
        """
    #{
        self.level = 0
        self.scope = 0
        self.attack = 0
        self.life = 0
        self.lifeMax = 0

        #redisplay

        self.inventoryQuantity = 0

        self.onAttacker = nullf
        self.onReachTag = nullf
        self.onSpawning = nullf

        self.attackers = [] # liste de 'Base'
        self.isAttacker = False # personne ne l'attaque
        self.goal = []
        self.isGoal = False
        self.isAlive = False
    #}

    def run(self):
        """ NO YOU DONT

            Si l'entite est mort
                renvoie False

            Si l'entite n'est pas spawn (si spawn, appel onSpawning)
                renvoie True

            Si l'entite meure (SEE onDed ?)
                renvoie False

            Si l'entite est attacer (appel onAttacker)
                renvoie True

            Si elle a un but (appel interract)
                renvoie True
        """
    #{
        if not self.isAlive: # ils ont tuer Keny
            return False

        if not self.isReady: # tant qu'il n'a pas atteint son max de vie
            if self.life < self.lifeMax:
                self.life+= 1
            else:
                self.isReady = True
                self.onSpawning(self)
            return True

        if self.life <= 0: # a l'instant de la mort
            #ded
            print("entity died : {}".format(self.civzID))
            self.die()
            return False

        if self.isAttacker:
            #print("entity attacked")
            removeLater = []
            for i in range(len(self.goal)): # suppr les ded
                if not self.goal[i].isAlive:
                    removeLater.append(i)
            for it in removeLater:
                self.goal.pop(it)
            self.onAttacker(self, self.attackers)
            return True # TODO ?: add hasInterract

        #SEE : /!\ unique action du tour [up] SEE : prioritees ??
        if self.isGoal:
            # test la possibilitee d'interraction
            if self.pos.getDistanceStraight(self.goal[0].pos) <= self.scope:
                # si fin d'interraction (ded, reach...)
                if self.interract(self.goal[0]):
                    self.goal.pop(0) # alors ce n'est plus un but
                    if len(self.goal) == 0:
                        self.isGoal = False # plus aucun but
            # sinon se deplace vers goal[0]
            else:
                print("from {}".format(self.pos),)
                mov = self.pos.getUnitVector(self.goal[0].pos, self.speed)
                dist = self.pos.getDistanceStraight(self.goal[0].pos)
                # distance a parcourir > distance d'interraction
                if dist > self.scope:
                    # distance parcourablu > distance a parcourir
                    if self.speed > dist:
                        #TODO : fix +0.1
                        mov = self.pos.getUnitVector(self.goal[0].pos, dist-self.scope + 0.01)
                    self.pos.x+= mov.x
                    self.pos.y+= mov.y
                print("move to {}".format(self.pos))

        return True
    #}
#}
def e(position = Coord, civz = 42, ID = int, kindOf = float):
    """ Voir Entity
    """
    return Entity(position, civz, ID, kindOf)
