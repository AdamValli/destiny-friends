## Destiny Leaderboard

from pprint import PrettyPrinter
from player import Player
import users



pp = PrettyPrinter()

ubzy = Player("4611686018504046881", "2")
bnet_ubzy_data = ubzy.handlerMethodTestBnet()
dest_ubzy_data = ubzy.handlerMethodTestProfile()
pp.pprint(bnet_ubzy_data)
pp.pprint(dest_ubzy_data)
print("")

# gundo = Player("4611686018431047411", "2")
# gundo.populateMembershipDetails()
# pp.pprint(gundo.getAllMembershipDetails())
print("")

# ish = Player("4611686018445613615", "2")
# ish.getBungieGlobalDisplayName()
# all_data = ish.getAllHandlerData()

# pp.pprint(all_data)