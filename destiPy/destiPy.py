# non-exhaustive Bungie / Destiny 2 API Wrapper
#   created by Adam Valli

import requests

class DestiPy:
    api_key = ""
    cookie = 'Q6dA7j3mn3WPBQVV6Vru5CbQXv0q+I9ddZfGro+PognXQwjWM8PS+VE_=v1oNhRgw__OFa; __cflb=04dToX7HjFoF4QAzoaHehFaMj5fkjPR6poVjCBxPsR; bungleanon=sv=BAAAAACeNAAAAAAAAIijygAAAAAAAAAAAAAAAAC5ufer5z7aCEAAAADYDg7Z0Mt2ntYxE899v04v2smdaF+Yis3D4/xuVAT6pwF9kap56Ng8u7tji9PV0scY1GPY9m++2HrclM2z0j1e&cl=MC4xMzQ3MC4xMzI4MDEzNg==; bungled=7886619270921226958; bungledid=B6wBUh0zhmpHrgPwfJIlsEq5ufer5z7aCAAA'
    ROOT = "https://www.bungie.net/Platform/"


    def __init__(self, api_key):
        self.setApiKey(api_key)

    

    @classmethod
    def getApiKey(cls):
        return cls.api_key
    
    @classmethod
    def setApiKey(cls, api_key):
        cls.api_key = api_key
    
    @classmethod
    def setCookie(cls, cookie):
        cls.cookie = cookie
    
    @classmethod
    def getRoot(cls):
        return cls.ROOT
    
    @classmethod
    def getCookie(cls):
        return cls.cookie
    
# <------------ Methods for Retrieving Membership Details ------------->

    # return json; all memberships link to profile
    # > All membership ids, 
    # path_params: Dict, "membershipId" -> bnet or destiny membership id; "membershipType" -> type of membership the player has
    # query_params: Dict, "getAllMemberships" -> "true" or "false"
    def getLinkedProfiles(self, path_params, query_params):
        headers = {
            "x-api-key":self.getApiKey(),
            "Cookie":self.getCookie()
        }
        payload = {}
        root = self.getRoot()
        url = root + "Destiny2/"+path_params.get("membershipType")+"/Profile/"+path_params.get("membershipId")+"/LinkedProfiles/?getAllMemberships="+query_params.get("getAllMemberships")

        response = requests.get(url, headers=headers, data=payload)
        return response.content


    def getBungieNetUserById(self, path_params):
        headers = {
            "x-api-key":self.getApiKey(),
            "Cookie":self.getCookie()
        }
        payload = {}
        root = self.getRoot()
        url = root + "User/GetBungieNetUserById/"+ path_params.get("membershipId") +"/"

        response = requests.get(url, headers=headers, data=payload)
        return response.content


    # get friends list
    # all membership info for all in friends list
    def getFriendsList(self):
        pass

    
    # User.GetMembershipDataById
    def getMembershipsById(self, mid, mtype):
        headers = {
            "x-api-key":self.getApiKey(),
            "Cookie":self.getCookie()
        }
        payload = {}
        root = self.getRoot()
        
        url = root + "/User/GetMembershipsById/"+mid+"/"+mtype+"/"

        response = requests.get(url, headers=headers, data=payload)
        return response.content

    # User.GetProfile
    # get CHARACTERS and more for given Id
    #   path_params: dmid = destiny membership id, mtype = membership type
    #   query_params: component = code for data to retrieve (character, profile, stats) etc. See API Docs for more info.
    def getProfile(self, path_params, query_params):
        headers = {
            "x-api-key":self.getApiKey(),
            "Cookie":self.getCookie()
        }
        payload = {}
        root = self.getRoot()
        
        url = root + "Destiny2/"+path_params.get("membershipType")+"/Profile/"+path_params.get("membershipId")+"/?components="+query_params.get("component")
        response = requests.get(url, headers=headers, data=payload)
        response.raise_for_status
        return response.content

# <------------- Methods for Retrieving Stats ----------->

    # GET getHistoricalData request
    # RETURN player historical data -> JSON 
    def getHistoricalData(self, path_params, query_params):

        headers = self.getHeaders()
        payload = {}
                
        # path creation
        path1 = "Destiny2/"+path_params.get("destinyMembershipType")+"/Account/"+path_params.get("destinyMembershipId")+"/Character"+"/"+path_params.get("characterId")+"/Stats"+"/?dayend="+query_params.get("dayEnd")+"&daystart="+query_params.get("dayStart")+"&groups="+query_params.get("groups")+"&modes="+query_params.get("modes")+"&periodType="+query_params.get("periodType")


        url = self.getRoot() + path1

        response = requests.get(url, headers=headers)

        response.raise_for_status()

        return response.content




