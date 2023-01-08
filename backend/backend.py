import genshinstats as gs
import glob
import re
import os
import time
import pandas as pd

#token ID and login ID

class PlayerUser:
    def __init__(self):
        # looking for user_profiles.txt
        self.profile = os.path.join(".","backend","user_profiles.txt")
        file = glob.glob(os.path.join(".","backend","*"))
        if self.profile not in file:
            new_profile = open(self.profile, 'w')
            new_profile.write(">> user")
            new_profile.close()
        
    def show_users(self):
        self.profile_list = open(self.profile, 'r')
        users = {}
        user_count = 0
        for line in self.profile_list:
            find_user = line.split("\t>"); 
            if len(find_user) == 2:
                user_count += 1
                users[user_count] = find_user[1].strip()
        self.profile_list.close()
        return users

    def add_user(self, username: str, hoyolab_id: int, hoyo_token: str, game_uid: int ):
        self.profile_list = open(self.profile, 'a')
        self.profile_list.write(f"\t> {username.strip()}\n")
        self.profile_list.write(f"\t\tltuid: {hoyolab_id}\n")
        self.profile_list.write(f"\t\tltoken: {hoyo_token}\n")
        self.profile_list.write(f"\t\tuid: {game_uid}\n")
        self.profile_list.close()

    def find_user(self, find_username: str, show_info = True):
        print("Note: The username is case-sensitive.")
        self.profile_list = open(self.profile, 'r')
        self.info = [["name", find_username]]
        load_profile = self.profile_list.readlines()
        for i, line in enumerate(load_profile):
            find_user = line.split("\t>")
            if len(find_user) == 2 and find_user[1].strip() == find_username:
                if show_info == True:
                    [self.info.append(y.strip().split(": ")) for x,y in enumerate(load_profile) if x == i + 1 or  x == i + 2 or  x == i + 3]
        self.profile_list.close()
        if len(self.info) != 4:
            return f"No user with name {find_username}"
        else:
            return dict(self.info)

    def choose_user(self):
        print(" ---- + List of registered users + ----")
        for i, users in self.show_users().items():
            print(f"{i}: {users}")
        
        while True:
            try:
                user_choose = int(input("Select the USERNAME number from registered list: "))
                print("Fetching user info..."); time.sleep(1.5)
                user_tag = self.show_users()[user_choose]
            except Exception:
                print("USERNAME INVALID| Please pass a valid input.")
            else:
                break

        try:
            fetch_info = self.find_user(user_tag)
            read_currentuserprofile = open("backend/current_userprofile.txt",'w')
            read_currentuserprofile.write(f"name: {user_tag}\nuid: {fetch_info['uid']}\nltuid: {fetch_info['ltuid']}\nltoken: {fetch_info['ltoken']}")
            print("Successfully updated current user profile")
        except Exception:
            print("An error occured.")

        return fetch_info

    def ingame_resources(self):
        #fetching userinfo from current user profile
        rd = open("backend/current_userprofile.txt","r")
        content = rd.read()
        id = re.findall(r"name:.*", content, re.MULTILINE)[0].replace("name: ","")
        uinfo = self.find_user(id)
        #Fetch Geenshin impact infonotes
        gs.set_cookie(ltuid=uinfo['ltuid'], ltoken=uinfo['ltoken'])
        ingame_resources = gs.get_notes(uinfo["uid"])

        content.close()
        return ingame_resources

    def ingame_resources(self):
        #fetching userinfo from current user profile
        rd = open("backend/current_userprofile.txt","r")
        content = rd.read()
        id = re.findall(r"name:.*", content, re.MULTILINE)[0].replace("name: ","")
        uinfo = self.find_user(id)
        #Fetch Geenshin impact infonotes
        gs.set_cookie(ltuid=uinfo['ltuid'], ltoken=uinfo['ltoken'])
        ingame_resources = gs.get_notes(uinfo["uid"])

        rd.close()
        return ingame_resources

    def ingame_info(self):
        #fetching userinfo from current user profile
        rd = open("backend/current_userprofile.txt","r")
        content = rd.read()
        id = re.findall(r"name:.*", content, re.MULTILINE)[0].replace("name: ","")
        uinfo = self.find_user(id)

        #Fetch Geenshin impact infonotes
        gs.set_cookie(ltuid=uinfo['ltuid'], ltoken=uinfo['ltoken'])
        ingame_info = gs.get_all_user_data(uinfo["uid"])
        rd.close()
        return ingame_info

if __name__ == "__main__":
    Genshin = PlayerUser()
    #update current user
    # Genshin.choose_user()
    a = Genshin.ingame_info()
    # print(a.keys())
    # dict_keys(['name', 'rarity', 'element', 'level', 'friendship', 'constellation', 'icon', 'image', 'id', 'collab', 'weapon', 'artifacts', 'constellations', 'outfits'])
    print(a['stats'])