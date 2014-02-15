# -*- coding: utf-8 -*-
import os, sys



sys.path.append('/root/git/gh/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from Functions import getNewsArticles, saveNews
from Facebook import Facebook
GLOBAL_nb_infos = 10
GLOBAL_bit_login="geekhub2k13"
GLOBAL_bit_apikey="R_f72dc24a911b6865b8cf2b4b9c8531b1"


print "DEBUT Article"
sources = {"Le Comptoir du Hardware":"http://www.comptoir-hardware.com/home.xml", 
          "FrAndroid":"http://feedpress.me/frandroid/",
          "Gizmodo":"http://www.gizmodo.fr/feed/",
          "Le Journal du Geek":'http://feeds2.feedburner.com/lejournaldugeek',
          "Korben":'http://feeds.feedburner.com/korbensblog-upgradeyourmind?format=xml',
          "Les Numériques":"http://feeds.feedburner.com/lesnumeriques/news/",
          "MacGeneration":"http://feed.macg.co/megaflux",
          "Presse Citron":"http://feeds2.feedburner.com/Pressecitron",
          "Tom's Guide":"http://www.tomsguide.fr/feeds/rss2/tom-s-guide-fr,20-0.xml",
          "01net":"http://rss.feedsportal.com/c/629/f/502199/index.rss"} #01net

for source, rss in sources.items() :
    print source
    
    linksNews = list(getNewsArticles(rss,nb_infos=GLOBAL_nb_infos))
    for link_article in linksNews :
        try :
            saveNews(source, link_article, bit_login=GLOBAL_bit_login, bit_apikey=GLOBAL_bit_apikey)
        except : pass
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
#Twitter
#o_twitter = Twitter("GeekHub2k13",GLOBAL_nb_infos)
    