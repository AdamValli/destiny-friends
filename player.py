# Represents a Destiny player
# usage: build a destiny of player using destiPy wrapper
# 1. Set Destiny ID and Character Type
# 2. Populate data with methods


from pprint import PrettyPrinter
from dataHandler import DataHandler


class Player():
    # class variables
    number_of_players = 0


    all_membership_details = {}
    all_stats= {}

    # default constructor
    # sets up data handler for this player + data structures  
    def __init__(self, destinyId=None, membershipType="2") -> None:
        self.initDestinyId = destinyId
        self.initMembershipType = membershipType

        self.handler = self.createHandler()

        self.addPlayer() # reflexive usage of class method in constructor
        
        self.profile_data={
            "character_ids":{},
            "destiny":{},
            "bnet":{}
        }
        self.character_data={
            "characters":{}
        }

        self.stats={}

    # usage Player.classMethod(); independant of instance
    @classmethod
    def addPlayer(cls):
        cls.number_of_players += 1

    @classmethod
    def getNumberOfPlayers(cls):
        return cls.number_of_players
    
    def createHandler(self):
        return DataHandler(dmid=self.getInitDestinyId(), dmtype=self.getInitMembershipType())
    
    # getters
    def getInitDestinyId(self):
        return self.initDestinyId
    
    def getInitMembershipType(self):
        return self.initMembershipType

    def getAllMembershipDetails(self):
        return self.profile_data    
    

    # PUBLIC


    # Test
    def getAllHandlerData(self):
        return self.handler.retrieveBnetProfileData()
    
    def handlerMethodTestBnet(self):
        return self.handler.retrieveBnetProfileData()

    def handlerMethodTestProfile(self):
        return self.handler.retrieveDestinyProfileData()
