import genshinstats as gs
import glob
import sys
import re
import os
import time
import json

import requests

#token ID and login ID

class PlayerUser:
    def __init__(self, hoyoid, hoyotoken):
        # looking for user_profiles.txt
        self.profile = os.path.join(".","backend","user_profiles.txt")
        self.hoyo_token = hoyotoken
        self.hoyolab_id = hoyoid
        gs.set_cookie(ltuid = self.hoyolab_id, ltoken = self.hoyo_token)
        
    def show_users(self):
        self.profile_list = open(self.profile, 'r')
        users = {}
        user_count = 0
        for line in self.profile_list:
            find_user = line.split("	>> ingame_name:"); 
            if len(find_user) > 1:
                user_count += 1
                users[user_count] = find_user[1].strip()
        self.profile_list.close()
        return users

    def find_user(self, username):
        self.profile_list = open(self.profile, 'r')
        content = self.profile_list.readlines()
        uinfo = {}
        profile_id = None

        for line_number, lines in enumerate(content):
            if line_number < 2:
                users = lines.strip().split(": ")
                uinfo[users[0]] = users[1]
            elif line_number >= len(content) - 1:
                sys.exit(f"No user found for: '{username}'")
            else:
                user = lines.strip().split(">> ingame_name: ")
                if len(user) > 1 and username == user[1]:
                    uinfo['name'] = user[1]
                    profile_id = line_number
                elif len(user) > 1 and username != user[1]:
                    pass
                #get the matched user metadata
                if profile_id != None:
                    if line_number > profile_id and line_number <= profile_id + 2:
                        usermetadata = lines.strip().split(": ")
                        uinfo[usermetadata[0]] = usermetadata[1]
                    elif line_number > profile_id + 3:
                        break
            

        self.profile_list.close()
        return uinfo


    def add_user(self):
        #this doesnt work on accounts in China server
        all_user_account = gs.get_game_accounts(chinese=False)
        self.profile_list = open(self.profile, 'a')
        self.profile_list.truncate(0)
        self.profile_list.write(f"ltuid: {self.hoyolab_id}\nltoken: {self.hoyo_token}\n")
        for game_accounts in all_user_account:
            print(f"Adding {game_accounts['nickname']} ({game_accounts['uid']})")
            self.profile_list.write(f"\t>> ingame_name: {game_accounts['nickname']}\n")
            self.profile_list.write(f"\t\tlevel: {game_accounts['level']}\n")
            self.profile_list.write(f"\t\tuid: {game_accounts['uid']}\n")
        self.profile_list.close()


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
        content = rd.readlines()
        
        #Fetch Genshin impact infonotes
        get_current_uid = content[1].strip().split(": ")[1]
        ingame_info = gs.get_all_user_data(get_current_uid)
        rd.close()
        return ingame_info

    def update_resources(self):
        #Download image resources
        for characters in Genshin.ingame_info()['characters']:
            if not os.path.exists(f"chars/image/img_{characters['name']}.png"):
                img_data = requests.get(characters['image'])
                img = open(f"images/chars/image/img_{characters['name']}.png", 'wb')
                img.write(img_data.content)
                img.close()

            if not os.path.exists(f"chars/image/icon_{characters['name']}.png"):       
                icon_data = requests.get(characters['icon'])
                icon = open(f"images/chars/icons/icon_{characters['name']}.png", 'wb')
                icon.write(icon_data.content)
                icon.close()
        print("Successully updated image resources.")

        #Download files character data
        user_data = self.ingame_info()
        udata = open("others/data.json","w")
        json.dump(user_data,udata, indent=4)
        udata.close()
        print("Successully updated user data resources.")
        print('DONE!')

if __name__ == "__main__":
    Genshin = PlayerUser(69270783,"RFTYzxIugEIsan7EUeCguSSHld8cdvI4XPacp81i")
    #update current user
    # Genshin.choose_user()
    # a = Genshin.ingame_info()
    # print(a.keys())
    # dict_keys(['name', 'rarity', 'element', 'level', 'friendship', 'constellation', 'icon', 'image', 'id', 'collab', 'weapon', 'artifacts', 'constellations', 'outfits'])
    # print(Genshin.ingame_info()['stats'])
    # for chars in a['characters']:
    #     print(chars['name'],'\t\t\t' ,chars['level'])

    # for characters in Genshin.ingame_info()['characters']:
    #     #dict_keys(['name', 'rarity', 'element', 'level', 'friendship', 'constellation', 'icon', 'image', 'id', 'collab', 'weapon', 'artifacts', 'constellations', 'outfits'])
    #     print(characters['weapon'])

    Genshin.update_resources()