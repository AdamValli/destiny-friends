
from cgitb import handler
import json
from pprint import PrettyPrinter

from destiPy.destiPy import DestiPy

# use destiPy to gather / return custom, formatted datasets
# FUNCTION-BASED CLASS
class DataHandler():
    API_KEY = "1e9e5c9d953f4f73aeaac1e3bc27efd6"
    def __init__(self, dmid, dmtype):
        self.createApiObject(api_key=self.API_KEY)
        self.data = {}

        # get meta data upon initialisation
        self.populateMetaData(dmid, dmtype)
    
    
    # FOR INTERNAL-USE ONLY (PRIVATE)

    @classmethod
    def createApiObject(cls, api_key):
        cls.api = DestiPy(api_key)
        
    # add dictionary data to 'data dictionary'
    def addData(self, data):
        for k,v in data.items():
            self.data.setdefault(k,v)

    def getData(self):
        return self.data
    

    # retrieve basic meta data (profiles) from Bungie API
    def populateMetaData(self, dmid, dmtype) -> None:
        path_params = {
            "membershipId":str(dmid),
            "membershipType":str(dmtype)
        }
        query_params = {
            "query_get_linked_profiles":{"getAllMemberships":"True"},
            "query_get_profile":{"components":"100"}
        }
        json_linked_profiles = self.api.getLinkedProfiles(query_params=dict(query_params.get("query_get_linked_profiles")), path_params=path_params)
        dict_linked_profiles = json.loads(json_linked_profiles)
        self.addData(dict_linked_profiles.get("Response"))

        json_profiles = self.api.getProfile(path_params=path_params, query_params=dict(query_params.get("query_get_profile")))
        dict_profiles = json.loads(json_profiles)
        self.addData(dict_profiles.get("Response").get("profile").get("data"))

    
    # EXTERNAL-USE ONLY (PUBLIC)
    def retrieveBnetProfileData(self):
        
        # curated data of profile info
        bnet_data = {
            "bungieGlobalDisplayName":self.data.get("bnetMembership").get("bungieGlobalDisplayName"),
            "bungieGlobalDisplayNameCode":self.data.get("bnetMembership").get("bungieGlobalDisplayNameCode"),
            "displayName":self.data.get("bnetMembership").get("displayName"),
            "bnetMembershipId":self.data.get("bnetMembership").get("membershipId"),
            "bnetMembershipType":self.data.get("bnetMembership").get("membershipType"),
            "supplementalDisplayName":self.data.get("bnetMembership").get("supplementalDisplayName"),
        }
        return bnet_data

    
    def retrieveDestinyProfileData(self):
        profile_list = self.data.get("profiles")
        profile_dict = dict(profile_list[0])
        # curated destiny profile data
        dest_prof_data = {
            "bungieGlobalDisplayName":profile_dict.get("bungieGlobalDisplayName"),
            "bungieGlobalDisplayNameCode":profile_dict.get("bungieGlobalDisplayNameCode"),
            "displayName":profile_dict.get("displayName"),
            "destinyMembershipId":profile_dict.get("membershipId"),
            "destinyMembershipType":profile_dict.get("membershipType")
        }
        return dest_prof_data