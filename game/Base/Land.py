import random as rand
from Entity import Entity, e
from Struct import Struct, s
from Defs import *

class Land:
    """ Terrain de jeux
    """
#{
    def __init__(self, size=tuple):
        """ size = (w,h) integers

            create a plane landscape
        """
        self.width, self.height = size
        self.landscape = [[0 for j in range(self.width)] for i in range(self.height)]
        self.isGenerated = False

    def setSeed(rs):
        """ preset the seed for random generation
        """
        rand.seed(rs)

    def generateRandomStructures(wilderness, occurences=tuple):
        """ occurences ratios (betwen 0 and 1) of folowing structures:
                TREE
                SHOAL
                BUSH
                ORE_STONE
                ORE_IRON
                ORE_GOLD

            wilderness: empty civz to fill w/ nat_structs
        """
        pass

    def spawnRandomEntities(wilderness, occurences=tuple):
        """ occurences ratios (betwen 0 and 1) of folowing entities:
                SHEEP

            wilderness: empty civz to fill w/ nat_structs
        """
        pass
#}
