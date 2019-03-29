Civilization(self, loop, start, name, pos)


isKnown(self, pos) #TODO #USED getTeam

goReach(self, who, where) #TODO #?
goAttack(self, who, what) #TODO #? #SEE #USE isKnown

getTownHall(self)
getTeamTownHall(self, team) #SEE #USE isKnown

setLoop(self, loop) #SEE

#Gestion de entities
#{
upgEntity(self, who, where) #USE pay
newEntity(self) #USE pay

getLastEntity(self)

getRandomEntity(self, kindOf)
getNearestEntity(self, position, kindOf) #TODO

getTeamRandomEntity(self, kindOf, team) #USE isKnown
getTeamNearestEntity(self, position, kindOf, team) #TODO #SEE #USE isKnown

forEachEntity(self, fonction)
#}

#Gestion de structs
#{
upgStruct(self, builders, what) #USE pay
newStruct(self, builders, building) #USE pay

getLaseStruct(self)

getRandomStruct(self, kindOf)
getNearestStruct(self, position, kindOf) #TODO

getTeamRandomStruct(self, kindOf, team) #USE isKnown
getTeamNearestStruct(self, position, kindOf, team) #TODO #SEE #USE isKnown

forEachStruct(self, fonction)
#}

#Fonction internes (ne pas utiliser)
#{
pay(self, cost)
autorun(self)
#}

setCallback(self, callbacks = function)
    onAttacker
    onReachTag
    onSpawning