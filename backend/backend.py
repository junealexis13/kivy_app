import genshinstats as gs
import pandas as pd

#token ID and login ID

gs.set_cookie(ltuid=69270783, ltoken="RFTYzxIugEIsan7EUeCguSSHld8cdvI4XPacp81i") # search all browsers

uid = 811219969

data = gs.get_user_stats(uid)
notes = gs.get_notes(uid)

print(notes)
# print(data)
# for x in data:
#     print(x['name'], x['level'])