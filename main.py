## Destiny Leaderboard

from pprint import PrettyPrinter
from player import Player
import users



pp = PrettyPrinter()

ubzy = Player(users.ubzy.get("destiny_membership_id"), users.ubzy.get("destiny_membership_type"))
adam = Player(users.gundo.get("destiny_membership_id"), users.gundo.get("destiny_membership_type"))
ish = Player(users.ish.get("destiny_membership_id"), users.ish.get("destiny_membership_type"))

