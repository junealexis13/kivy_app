import re

if __name__ == "__main__":
    pass

with open("backend/current_userprofile.txt","r") as rd:
    content = rd.read()

    a = re.match(r"name:.*", content, re.MULTILINE)[0].replace("name: ","")
    print(a)