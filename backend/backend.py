import genshinstats as gs
import glob
import os
import pandas as pd

#token ID and login ID

class PlayerUser:
    def __init__(self):
        # looking for profile.txt
        self.profile = os.path.join(".","backend","profile.txt")
        file = glob.glob(os.path.join(".","backend","*"))
        if self.profile not in file:
            new_profile = open(self.profile, 'w')
            new_profile.write(">> user")
            new_profile.close()
        
    def show_users(self):
        self.profile_list = open(self.profile, 'r')
        for line in self.profile_list:
            find_user = line.split("\t>")
            if len(find_user) == 2:
                print(find_user[1].strip())
        self.profile_list.close()

    def add_user(self, username: str, hoyolab_id: int, hoyo_token: str, game_uid: int ):
        self.profile_list = open(self.profile, 'a')
        self.profile_list.write(f"\t> {username.strip()}\n")
        self.profile_list.write(f"\t\tltuid: {hoyolab_id}\n")
        self.profile_list.write(f"\t\tltoken: {hoyo_token}\n")
        self.profile_list.write(f"\t\tuid: {game_uid}\n")
        self.profile_list.close()

    def find_user(self, find_username: str, show_info = False):
        print("Note: The username is case-sensitive.")
        self.profile_list = open(self.profile, 'r')
        load_profile = self.profile_list.readlines()
        for i, line in enumerate(load_profile):
            find_user = line.split("\t>")
            if len(find_user) == 2 and find_user[1].strip() == find_username:
                print(find_user[1].strip())
                # if show_info == True:
                #     for (line_ind, info_line), r in zip(enumerate(load_profile), range(1,4)):
                #         if line_ind == i + r:
                #             print(r)

        self.profile_list.close()


if __name__ == "__main__":
    Genshin = PlayerUser()
    Genshin.find_user("Cheonsa",show_info=True)
    # Genshin.show_users()




# gs.set_cookie(ltuid=169469751, ltoken="iIaZf8sNY5cIjNaSaLFbNjCdxikE6AZFVwADFVaw") # search all browsers

# uid = 841830081

# data = gs.get_user_stats(uid)
# # notes = gs.get_notes(uid)
# notes = gs.get_notes(uid)
# print(notes)
# # print(data)
# # for x in data:
# #     print(x['name'], x['level'])