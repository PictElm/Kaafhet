from Base import Base
from Defs import *

class Struct(Base):
    """ Structure productive fixe

        Methodes :
            use
            run
    """
#{
    def __init__(self, position = Coord, civz = 42, ID = int, kindOf = float):
    #{
        Base.__init__(self, position, civz, ID, kindOf)
        meta = getMetas(kindOf)
        self.size = meta[SIZE] # depend de kind
        self.isUnderConstruction = True
        self.isSpawningEntity = False
        self.spawningEntity = 0
    #}

    def use(self, who, what): # what(kind) si plusieur possibilitees
        """ NO YOU DONT

            appeler par qui (Enity ou Civz/gui) ?
            gui, cree, ameliorer, mize en garnizon SEE...
        """
    #{
        if not self.isAlive:
            return False

        if self.kind == TOWN_HALL:
            self.isSpawningEntity = True
            self.spawningEntity = who
        #else: # upgrade d'une entity
            #TODO : all
            #SEE #?
    #}

    def run(self): # fnc temporaire? # tests?
        """ NO YOU DONT

            osef ?
        """
    #{
        if not self.isAlive:
            return False

        if self.life <= 0:
            #ded
            self.isAlive = False
            print "struct died : {}".format(self.civzID)
            return False

        if self.isAttacker:
            #print "struct attacked"
            self.onAttacker(self, self.attackers)
        #TODO : tower

        if self.isSpawningEntity:
            if self.spawningEntity.life < self.spawningEntity.lifeMax:
                self.spawningEntity.life+= self.level
            elif self.spawningEntity.life > self.spawningEntity.lifeMax:
                self.spawningEntity.life = self.spawningEntity.lifeMax
            else: # life == lifemax
                self.isSpawningEntity = False
            #SEE

        return True
    #}
#}
def s(position = Coord, civz = 42, ID = int, kindOf = float):
    """ Voir Struct
    """
    return Struct(position, civz, ID, kindOf)
