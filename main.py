## Destiny Leaderboard

from pprint import PrettyPrinter
from player import Player
import users



pp = PrettyPrinter()

ubzy = Player("4611686018504046881", "2")
print(ubzy.getBungieGlobalDisplayName())
all_ubzy_data = ubzy.getAllHandlerData()
pp.pprint(all_ubzy_data)
print("")

# gundo = Player("4611686018431047411", "2")
# gundo.populateMembershipDetails()
# pp.pprint(gundo.getAllMembershipDetails())
print("")

# ish = Player("4611686018445613615", "2")
# ish.getBungieGlobalDisplayName()
# all_data = ish.getAllHandlerData()

# pp.pprint(all_data)