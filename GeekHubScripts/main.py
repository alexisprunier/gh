# -*- coding: utf-8 -*-
import os, sys

sys.path.append('/home/alexis/Desktop/git/GeekHub')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")


from LesNumeriques import LesNumeriques
from PresseCitron import PresseCitron
from TomsGuide import TomsGuide
from Hardware import Hardware
from Gizmodo import Gizmodo
from ComptoirDuHardware import ComptoirDuHardware
from ZeroUnnet import ZeroUnnet

GLOBAL_nb_infos = 10


o_lesnums = LesNumeriques(nb_infos=GLOBAL_nb_infos)
o_pressecitron = PresseCitron(nb_infos=GLOBAL_nb_infos)
o_TomsGuide = TomsGuide(nb_infos=GLOBAL_nb_infos)
o_hardware = Hardware(nb_infos=GLOBAL_nb_infos)
o_gizmodo = Gizmodo(nb_infos=GLOBAL_nb_infos)
o_comptoir = ComptoirDuHardware(nb_infos=GLOBAL_nb_infos)
o_01net = ZeroUnnet(nb_infos=GLOBAL_nb_infos)