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
from Facebook import Facebook

GLOBAL_nb_infos = 2

print "DEBUT Article"
o_lesnums = LesNumeriques(nb_infos=GLOBAL_nb_infos)
o_pressecitron = PresseCitron(nb_infos=GLOBAL_nb_infos)
o_TomsGuide = TomsGuide(nb_infos=GLOBAL_nb_infos)
o_hardware = Hardware(nb_infos=GLOBAL_nb_infos)
o_gizmodo = Gizmodo(nb_infos=GLOBAL_nb_infos)
o_comptoir = ComptoirDuHardware(nb_infos=GLOBAL_nb_infos)
o_01net = ZeroUnnet(nb_infos=GLOBAL_nb_infos)


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
  
    