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
        self.addPlayer() # reflexive usage of class method in constructor

        self.initDestinyId = destinyId
        self.initMembershipType = membershipType
        self.handler = self.createHandler()

        
        self.profile_data={
        }
        self.character_data={
        }

        self.stats={}

        self.initProfileData()
        
    # INTERNAL-USE ONLY. PRIVATE METHODS.
    # usage Player.classMethod(); independant of instance
    @classmethod
    def addPlayer(cls):
        cls.number_of_players += 1

    @classmethod
    def getNumberOfPlayers(cls):
        return cls.number_of_players
    
    def createHandler(self):
        return DataHandler(dmid=self.getInitDestinyId(), dmtype=self.getInitMembershipType())
    
    def initProfileData(self):
        self.profile_data["bnet"]=self.handler.retrieveBnetProfileData()
        self.profile_data["destiny"]=self.handler.retrieveDestinyProfileData()
        self.profile_data["characterIds"] = self.handler.retrieveCharacterIds()
    
    def __str__(self) -> str:
        return self.getBnetProfile().get("supplementalDisplayName") + "\nMembership ID: " + self.getInitDestinyId() + "\nMembership Type: " + self.getInitMembershipType()
    
    # PUBLIC

    # getters
    def getInitDestinyId(self):
        return self.initDestinyId
    
    def getInitMembershipType(self):
        return self.initMembershipType
    
    def getSupplementalDisplayName(self):
        return self.profile_data.get("bnet").get("supplementalDisplayName")

    def getCharacterIds(self):
        return self.profile_data.get("characterIds")

    def getBnetProfile(self):
        return self.profile_data.get("bnet")

    def getDestinyProfile(self):
        return self.profile_data.get("destiny")
    
    def getProfile(self):
        return self.profile_data    
    

    
    # Test
    def getAllHandlerData(self):
        self.handler.retrieveCharacterIds()
        return self.handler.getData()
    
    def handlerMethodTestBnet(self):
        return self.handler.retrieveBnetProfileData()

    def handlerMethodTestProfile(self):
        return self.handler.retrieveDestinyProfileData()
