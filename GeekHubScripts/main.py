# -*- coding: utf-8 -*-
import os, sys



sys.path.append('/root/git/gh/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from GeekHub import bitly
from GeekHub.models import Article
from LesNumeriques import LesNumeriques
from PresseCitron import PresseCitron
from TomsGuide import TomsGuide
from Hardware import Hardware
from Gizmodo import Gizmodo
from ComptoirDuHardware import ComptoirDuHardware
from ZeroUnnet import ZeroUnnet
from JournalDuGeek import JournalDuGeek
from Korben import Korben
from Facebook import Facebook
from FrAndroid import FrAndroid
from Dealabs import Dealabs
from MacGeneration import MacGeneration

GLOBAL_nb_infos = 10
GLOBAL_bit_login="geekhub2k13"
GLOBAL_bit_apikey="R_f72dc24a911b6865b8cf2b4b9c8531b1"

print "DEBUT Article"
print "Korben"
o_korben = Korben(nb_infos=GLOBAL_nb_infos, bit_login=GLOBAL_bit_login, bit_apikey=GLOBAL_bit_apikey)
print "Les Nums"
o_lesnums = LesNumeriques(nb_infos=GLOBAL_nb_infos, bit_login=GLOBAL_bit_login, bit_apikey=GLOBAL_bit_apikey)
print "Presse Citron"
o_pressecitron = PresseCitron(nb_infos=GLOBAL_nb_infos, bit_login=GLOBAL_bit_login, bit_apikey=GLOBAL_bit_apikey)
print "Tom's Guide"
o_TomsGuide = TomsGuide(nb_infos=GLOBAL_nb_infos, bit_login=GLOBAL_bit_login, bit_apikey=GLOBAL_bit_apikey)
print "Hardware"
o_hardware = Hardware(nb_infos=GLOBAL_nb_infos, bit_login=GLOBAL_bit_login, bit_apikey=GLOBAL_bit_apikey)
print "Gizmodo"
o_gizmodo = Gizmodo(nb_infos=GLOBAL_nb_infos, bit_login=GLOBAL_bit_login, bit_apikey=GLOBAL_bit_apikey)
print "Comptoir du hardware"
o_comptoir = ComptoirDuHardware(nb_infos=GLOBAL_nb_infos, bit_login=GLOBAL_bit_login, bit_apikey=GLOBAL_bit_apikey)
print "JDG"
o_jdg = JournalDuGeek(nb_infos=GLOBAL_nb_infos, bit_login=GLOBAL_bit_login, bit_apikey=GLOBAL_bit_apikey)
print "01net"
o_01net = ZeroUnnet(nb_infos=GLOBAL_nb_infos, bit_login=GLOBAL_bit_login, bit_apikey=GLOBAL_bit_apikey)
print "FrAndroid"
o_frandroid = FrAndroid(nb_infos=GLOBAL_nb_infos, bit_login=GLOBAL_bit_login, bit_apikey=GLOBAL_bit_apikey)
print "MacGeneration"
o_macg = MacGeneration(nb_infos=GLOBAL_nb_infos, bit_login=GLOBAL_bit_login, bit_apikey=GLOBAL_bit_apikey)
'''
print "Dealabs"
o_dealabs = Dealabs(nb_infos=GLOBAL_nb_infos, bit_login=GLOBAL_bit_login, bit_apikey=GLOBAL_bit_apikey)
'''


#FB
print "DEBUT Facebook"
sources = {"Materiel.net":320776853364, 
          "LDLC":121548574526465, 
          "Rue du Commerce":119794289202,
          "Top Achat":123427650425,
          "GrosBill": 312422015254,
          }
for source,id in sources.items() :
    print "Facebook: "+source
    o_facebook = Facebook("http://www.facebook.com/feeds/page.php?format=rss20&id="+str(id), source, GLOBAL_nb_infos)

    