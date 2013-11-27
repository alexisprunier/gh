# -*- coding: utf-8 -*-
import os, sys

sys.path.append('/root/git/gh/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")


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

print "DEBUT Article"
print "Korben"
try :
    o_korben = Korben(nb_infos=GLOBAL_nb_infos)
except : pass
print "Les Nums"
try :
    o_lesnums = LesNumeriques(nb_infos=GLOBAL_nb_infos)
except : pass
print "Presse Citron"
try :
    o_pressecitron = PresseCitron(nb_infos=GLOBAL_nb_infos)
except : pass
print "Tom's Guide"
try :
    o_TomsGuide = TomsGuide(nb_infos=GLOBAL_nb_infos)
except : pass
print "Hardware"
try :
    o_hardware = Hardware(nb_infos=GLOBAL_nb_infos)
except : pass
print "Gizmodo"
try :
    o_gizmodo = Gizmodo(nb_infos=GLOBAL_nb_infos)
except : pass
print "Comptoir du hardware"
try :
    o_comptoir = ComptoirDuHardware(nb_infos=GLOBAL_nb_infos)
except : pass
print "JDG"
try :
    o_jdg = JournalDuGeek(nb_infos=GLOBAL_nb_infos)
except : pass
print "01net"
try :
    o_01net = ZeroUnnet(nb_infos=GLOBAL_nb_infos)
except : pass
print "FrAndroid"
try :
    o_frandroid = FrAndroid(nb_infos=GLOBAL_nb_infos)
except : pass
print "Dealabs"
try :
    o_dealabs = Dealabs(nb_infos=GLOBAL_nb_infos)
except : pass
print "MacGeneration"
try :
    o_macg = MacGeneration(nb_infos=GLOBAL_nb_infos)
except : pass


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

    