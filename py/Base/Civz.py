from Entity import Entity, e
from Struct import Struct, s
from Land import Land
from Defs import *
from random import randint

#TODO: connect civzList... somehow... if it mean anythings...
class Civilization:
    """ Classe interfaces

        Toutes les actions sont realisees a travers ses methodes
        Une Civilization doit etre passer a la fonction register pour etre prise en compt

        Methodes (#vrac) :
            isKnown

            goReach
            goAttack

            getTownHall
            getTeamTownHall

            setLoop

            upgEntity
            newEntity

            getLastEntity

            getRandomEntity
            getNearestEntity

            getTeamRandomEntity
            getTeamNearestEntity

            forEachEntity

            upgStruct
            newStruct

            getLaseStruct

            getRandomStruct
            getNearestStruct

            getTeamRandomStruct
            getTeamNearestStruct

            forEachStruct

            pay
            autorun
    """
#{
    def __init__(self, loop, start, name, pos): #SEE pos tmp
        self.name = name
        self.team = 0#len(civiList)+1#team
        self.run = loop
        self.start = start

        #TODO : structures naturelles
        #if name != "whild":
        self.waffle = 50
        self.wood = 50
        self.stone = 50
        self.iron = 50
        self.gold = 50

        self.entities = [e(pos.cpy(), self, 0, CIVIL), e(pos.cpy(), self, 1, CIVIL)]
        for it in self.entities:
            it.life = it.lifeMax

        self.structs = [s(pos, self, 0, TOWN_HALL)]
        for it in self.structs:
            it.life = it.lifeMax
            it.isUnderConstruction = False

    def feu(self, mates):
        self.civiList = mates
        self.start

    def __str__(self):
        eAlive = 0
        for it in self.entities:
            if it.isAlive:
                eAlive+= 1
        sAlive = 0
        for it in self.structs:
            if it.isAlive:
                sAlive+= 1
        return "\
team {} : <\"{}\">\n\
\twaffle = {}\n\
\t  wood = {}\n\
\t stone = {}\n\
\t  iron = {}\n\
\t  gold = {}\n\
\t{} entities; {} alive\n\
\t{} structs; {} alive\n\
town hall : {}\
".format(self.team, self.name,
self.waffle, self.wood, self.stone, self.iron, self.gold,
len(self.entities), eAlive, len(self.structs), sAlive, self.getTownHall())

    def setLoop(self, loop):
        """ Changer la boucle principale (a tout moment)
        """
        self.run = loop

    def pay(self, cost): # liste : [waffle, wood, stone, iron, gold]
        """ NO YOU DONT

            Test ET DEPENCE le tableau des ressources de la forme
            cost : [waffle, wood, stone, iron, gold]
        """
        if self.waffle >= cost[0] and \
           self.wood   >= cost[1] and \
           self.stone  >= cost[2] and \
           self.iron   >= cost[3] and \
           self.gold   >= cost[4]:

            self.waffle-= cost[0]
            self.wood  -= cost[1]
            self.stone -= cost[2]
            self.iron  -= cost[3]
            self.gold  -= cost[4]
            return True # transaction realisee
        return False # ressources insuffisantes

    def forEachEntity(self, fonction): # applique fonction foreach
        """ Applique la fonction pour chaque entitee

            Definitions : fonction(Entity)
        """
        for it in self.entities:
            fonction(it)
            #self.entities[i] = fonction(self.entities[i])

    def forEachStruct(self, fonction): # applique fonction foreach
        """ Applique la fonction pour chaque batiment

            Definitions : fonction(Struct)
        """
        for it in self.structs:
            fonction(it)
            #self.structs[i] = fonction(self.structs[i])

    def getTownHall(self):
        return self.structs[0]

    def getTeamTownHall(self, team): #SEE
        """ Uniquement si le batiment est visible ? (strat?)
        """
        return self.civiList[team].structs[0]

#{
    def getRandomEntity(self, kindOf):
        """ Une entitee aleatoire du type precisee (vivante)
        """
        match = []
        for it in self.entities:
            if it.kind == kindOf:
                match.append(it)
        if len(match) > 0:
            i = randint(0, len(match)-1)
            if match[i].isAlive and match[i].isReady:
                return match[i]
        return False
    #TODO : def getNearestEntity(self, position = Coord, kindOf = int):
    #? distance path ou straight - 4 fonctions
    def getLastEntity(self):
        """ Derniere entitee former (apres onSpawning)
        """
        if self.entities[-1].isAlive and self.entities[-1].isReady:
            return self.entities[-1]
        else:
            return False

    def getTeamRandomEntity(self, kindOf, team = int):
        """ Une entitee aleatoire du type precisee (vivante et visible)
        """
        match = []
        for it in self.civiList[team].entities:
            if it.kind == kindOf:
                match.append(it)
        if len(match) > 0:
            i = randint(0, len(match)-1)
            if match[i].isAlive and match[i].isReady:
                return match[i]
        return False
    #TODO : def getTeamNearestEntity(self, position = Coord, kindOf = int, team = int):
#}
#{
    def getRandomStruct(self, kindOf):
        """ Un batiment aleatoire du type precise (vivante)
        """
        match = []
        for it in self.structs:
            if it.kind == kindOf:
                match.append(it)
        if len(match) > 0:
            i = randint(0, len(match)-1)
            if match[i].isAlive and match[i].isReady:
                return match[i]
        return False
    #TODO : def getNearestStruct(self, position = Coord, kindOf = int):
    def getLaseStruct(self):
        """ Dernier batiment former (apres onSpawning)
        """
        if self.structs[-1].isAlive and self.structs[-1].isReady:
            return self.structs[-1]
        else:
            return False

    def getTeamRandomStruct(self, kindOf, team = int):
        """ Un batiment aleatoire du type precise (vivante et visible)
        """
        match = []
        for it in self.civiList[team].entities:
            if it.kind == kindOf:
                match.append(it)
        if len(match) > 0:
            i = randint(0, len(match)-1)
            if match[i].isAlive and match[i].isReady:
                return match[i]
        return False
    #TODO : def getTeamNearestStruct(self, position = Coord, kindOf = int, team = int):
#}

    def upgEntity(self, who = Entity, where = Struct):
        """ Modifie le type d'une entitee suivant le batiment precise
            SEE : quand faire le test de ressources ??
        """
        #TODO : pop it puis append l'evoluee ? non : conserve son civzID (strat)
        who.addGoal(where)

    def upgStruct(self, builders = [], what = Struct):
        """ Envois les entitees a l'amelioration du batiment
            SEE : quand faire le test de ressources ??
        """
        for it in builders:
            it.addGoal(what)
        #TODO : idem que pour entity (toujours dans interract)

    def newEntity(self):
        """ Creer une nouvelle entitee (si ressources disponible)
            l'entitee cree ne peut pas etre utiliser directement
        """
        cost = getMetas(CIVIL)[COST]
        if self.pay(cost):#SEE + limite de population
            self.entities.append(e(self.getTownHall().getPos().cpy(), self, len(self.entities), CIVIL))
            self.getTownHall().use(self.entities[-1], 0)
            return self.entities[-1] # len()-1
        else:
            return False # summon impossible

    def newStruct(self, builders = [], building = Struct): #SEE : building ? kindOf ?
        """ Envois les entitees a la fabrication du batiment
        """
        # false : construction impossible
        if getForm(building.kind) != CIV_STRUCT:
            return False
        for it in builders:
            if getForm(it.kind) != CIV_ENTITY:
                return False

        # true : consturuction lancee
        #SEE : les builders vont chercher les ressources ?
        #TODO : batiment le plus proche
        for it in builders:
            it.addGoal(self.structs[0])
            it.addGoal(building)
        self.structs.append(building) # s(?!)
        return True

    def autorun(self):#TODO : ded #SEE : bla #HJSDVFWXIJXLHBCHHZQKL
        """ NO YOU DONT

            run tt les entitees et tt les batiments auto
        """
        for it in self.entities:
            it.run()
#            if not it.run():
#                self.entities.pop(it.civzID)
#                #TODO : yaurait bezoin de decaler tt ls civzID ?!? <== solution: override it
#                #                                           (set it a overridable, or something...)
        for it in self.structs:
            if it.run() == False and it.kind == TOWN_HALL:
                return False #TODO : isalive pour tout

        return True
#}
def c(loop, start, name, pos):
    """ Voir Civilization
    """
    return Civilization(loop, start, name, pos)
