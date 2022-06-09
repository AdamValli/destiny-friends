
from cgitb import handler
import json
from pprint import PrettyPrinter

from destiPy.destiPy import DestiPy

# use destiPy to gather / return custom, formatted datasets
class DataHandler():
    API_KEY = "1e9e5c9d953f4f73aeaac1e3bc27efd6"
    def __init__(self, dmid, dmtype):
        self.createApiObject(api_key=self.API_KEY)
        self.data = {}
        params = {}
        queries = {}
        headers = {}
        print(f"DataHandler has received {dmid} and {dmtype}")
        self.populateAllMetaData(dmid, dmtype)

    @classmethod
    def createApiObject(cls, api_key):
        cls.api = DestiPy(api_key)

    def setParams(self, params):
        self.params = params

    def setQueries(self, queries):
        self.queries = queries
    
    def setAllParams(self, params, queries):
        self.setParams(params=params)
        self.setQueries(queries=queries)
    
    def addData(self, data):
        for k,v in data.items():
            self.data.setdefault(k,v)

    def getData(self):
        return self.data
    
    def getDisplayNames(self, id, mtype):

        params = {
            "membershipType":mtype,
            "membershipId":id
        }
        queries = {"getAllMemberships":"true"}
        
        response = self.api.getLinkedProfiles(path_params=params, query_params=queries)
        response_dict = json.loads(response)

        profiles_list = response_dict.get("Response").get("profiles")
        profiles_dict = profiles_list[0]

        bnetMembership_dict = response_dict.get("Response").get("bnetMembership")

        displayNames = {
            "destiny":{
                "displayName":profiles_dict.get("displayName"),
                "bungieGlobalDisplayName": profiles_dict.get("bungieGlobalDisplayName")
                },
            "bnetMembership":{
                "displayName":bnetMembership_dict.get("displayName"),
                "supplementalDisplayName":bnetMembership_dict.get("supplementalDisplayName"),
            }
        }

        return displayNames


    def getMembershipCodes(self, id, mtype):
        params = {
            "membershipType":mtype,
            "membershipId":id
        }
        queries = {"getAllMemberships":"true"}
                
        response = self.api.getLinkedProfiles(path_params=params, query_params=queries)
        response_dict = json.loads(response)

        profiles_list = response_dict.get("Response").get("profiles")
        profiles_dict = profiles_list[0]

        bnetMembership_dict = response_dict.get("Response").get("bnetMembership")

        membershipDetails = {
            "destiny":{
                "membershipId":profiles_dict.get("membershipId"),
                "membershipType": profiles_dict.get("membershipType")
                },
            "bnetMembership":{
                "bnetMembershipId":bnetMembership_dict.get("membershipId"),
                "bnetMembershipType":bnetMembership_dict.get("membershipType"),
                "supplementalDisplayNameCode":bnetMembership_dict.get("supplementalDisplayNameCode")

            }
        }
        return membershipDetails
    
    # dmid = destiny membership id
    # dmtype = destiny membership type
    # comp = componenet code; 200 for characters, see Bungie API > Destiny.DestinyComponentType 
    def getAllCharacters(self, dmid, dmtype, comp):
        
        path_params = {
            "membershipId":str(dmid),
            "membershipType":str(dmtype)
        }
        query_params = {
            "component":str(comp)
        }
        response = self.api.getProfile(path_params, query_params)
        
        # json -> dict; Return
        response_dict = json.loads(response)
        chars = dict(response_dict.get("Response").get("characters").get("data"))

        return chars


    # INTERNAL-USE ONLY
    def populateAllMetaData(self, dmid, dmtype):

        path_params={
            "membershipId":str(dmid),
            "membershipType":str(dmtype)
        }
        query_params={
            "component":"100,200"
        }

        # get profile & character dats
        profile_json = self.api.getProfile(path_params, query_params)
        profile_dict = json.loads(profile_json)

        # store in this handler object
        self.addData(profile_dict.get("Response"))




    def testApi(self, dmid, dmtype, comp):
        path_params = {
            "membershipId":dmid,
            "membershipType":dmtype
        }
        query_params = {
            "component":comp
        }
        response = self.api.getProfile(path_params, query_params)
        
        # json -> dict; Return
        response_dict = json.loads(response)

        return response_dict