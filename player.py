# Represents a Destiny player
# usage: build a destiny of player using destiPy wrapper
# 1. Set Destiny ID and Character Type
# 2. Populate data with methods


from pprint import PrettyPrinter
from textwrap import indent
from dataHandler import DataHandler


class Player():
    # class variables
    number_of_players = 0


    all_membership_details = {}
    all_stats= {}

    # default constructor
    # no overloaded constructors in Python :(  
    # so I will use default, then use set method/s  
    def __init__(self, destinyId=None, membershipType=None) -> None:
        self.initDestinyId = destinyId
        self.initMembershipType = membershipType

        self.handler = self.createHandler()

        self.addPlayer() # reflexive usage of class method in constructor
        
        self.membership_details={
            "destiny":{
            },
            "bnet":{
            }
        }
        self.characters={}

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
        return self.membership_details    
    
    def getDisplayName(self):
        return self.membership_details.get("destiny").get("displayName")
    
    def getMembershipId(self):
        return self.membership_details.get("destiny").get("membershipId")
    
    def getMembershipType(self):
        return self.membership_details.get("destiny").get("membershipType")
    
    def getBnetDisplayName(self):
        return self.membership_details.get("bnet").get("displayName")
    
    def getBnetMembershipId(self):
        return self.membership_details.get("bnet").get("membershipId")
    
    def getBnetMembershipType(self):
        return self.membership_details.get("bnet").get("membershipType")
    
    def getSupplementalDisplayName(self):
        return self.membership_details.get("bnet").get("supplementalDisplayName")

    def getSupplementalDisplayNameCode(self):
        return self.membership_details.get("bnet").get("supplementalDisplayNameCode")
    
    def getBungieGlobalDisplayName(self):
        return self.membership_details.get("destiny").get("bungieGlobalDisplayName")


    def printAllMembershipDetails(self):
        for key, value in self.membership_details.items():
            print(f"{key}: {value}")
    def printAllCharacters(self):
        for key,value in self.characters.items():
            print(f"{key}: {value}")

    # setters    
    def setInitDestinyId(self, id):
        self.initDestinyId = id
    
    def setInitMembershipType(self, mtype):
        self.initMembershipType = mtype

    def setDisplayName(self, dname):
        self.membership_details.get("destiny")["displayName"] = dname

    def setMembershipId(self, did):
        self.membership_details.get("destiny")["membershipId"] = did

    def setMembershipType(self, dtype):
        self.membership_details.get("destiny")["membershipType"] = dtype

    def setBnetDisplayName(self, bname):
        self.membership_details.get("bnet")["displayName"] = bname

    def setBnetMembershipId(self, bid):
        self.membership_details.get("bnet")["membershipId"] = bid

    def setBnetMembershipType(self, btype):
        self.membership_details.get("bnet")["membershipType"] = btype

    def setSupplementalDisplayName(self, sname):
        self.membership_details.get("bnet")["supplementalDisplayName"] = sname
    
    def setSupplementalDisplayNameCode(self, scode):
        self.membership_details.get("bnet")["supplementalDisplayNameCode"] = scode
    
    def setBungieGlobalDisplayName(self, bgname):
        self.membership_details.get("destiny")["bungieGlobalDisplayName"] = bgname

    def setAllDisplayNames(self, dname, bname, sname, bgname):
        self.setDisplayName(dname)
        self.setBnetDisplayName(bname)
        self.setSupplementalDisplayName(sname)
        self.setBungieGlobalDisplayName(bgname)

    def setAllMembershipCodes(self, did, dtype, bid, btype, scode):
        self.setMembershipId(did)
        self.setMembershipType(dtype)
        self.setBnetMembershipId(bid)
        self.setBnetMembershipType(btype)
        self.setSupplementalDisplayNameCode(scode)

    def setAllMembershipDetails(self, dname, did, dtype, bname, bid, btype, sname, scode, bgname):
        self.setDisplayName(dname)
        self.setMembershipId(did)
        self.setMembershipType(dtype)
        self.setBnetDisplayName(bname)
        self.setBnetMembershipId(bid)
        self.setBnetMembershipType(btype)
        self.setSupplementalDisplayName(sname)
        self.setSupplementalDisplayNameCode(scode)
        self.setBungieGlobalDisplayName(bgname)

    # char = dict single char data {"id":"data"}
    def setCharacter(self, char):
        for id,data in char.items():
            self.characters.setdefault(id,data)

    def setAllCharacters(self, chars_dict):
        for char in chars_dict.items():
            print(char)
            self.setCharacter(char)
    # -------------------------------- #

    # gets all memberships details and stores in membership_details dict
    def populateMembershipDetails(self):

        # get display names + membership codes
        displayNames = self.handler.getDisplayNames(id=self.destinyId, mtype=self.membershipType)
        membershipCodes = self.handler.getMembershipCodes(id=self.destinyId, mtype=self.membershipType)


        # store in this object
        self.setAllDisplayNames(dname=displayNames.get("destiny").get("displayName"), bname=displayNames.get("bnetMembership").get("displayName"), sname=displayNames.get("bnetMembership").get("supplementalDisplayName"), bgname=displayNames.get("destiny").get("bungieGlobalDisplayName"))
        self.setAllMembershipCodes(btype=membershipCodes.get("bnetMembership").get("bnetMembershipType"),did=membershipCodes.get("destiny").get("membershipId"), bid=membershipCodes.get("bnetMembership").get("bnetMembershipId"), scode=displayNames.get("bnetMembership").get("supplementalDisplayNameCode"), dtype=membershipCodes.get("destiny").get("membershipType"))    
    
    # retrieve + populate character IDs, avatar, emblem, race, light levels, etc.
    def populateCharacters(self):
        chars_dict = self.handler.getAllCharacters(dmid=self.getMembershipId(), dmtype=self.getMembershipType(), comp=200)
        self.setAllCharacters(chars_dict)

    
    def populateHistoricalStats(self):
        pass

    def testHandlerMethod(self):
        pp = PrettyPrinter()
        self.handler.populateAllMetaData(dmid=self.getInitDestinyId(), dmtype=self.getInitMembershipType())
        return self.handler.getData()



    # INTERNAL-USE ONLY
    def getAllHandlerData(self):
        return self.handler.getData()