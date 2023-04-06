# -*- coding: utf-8 -*-
import twitter
from twitter import *
from GeekHub.models import Twitter
from GeekHub import models
        
class Twitter :
        
    def __init__(self, sources, nb_infos):
        self.consumer_key = "KDJJd6V8mJdO1y48RRpA"
        self.secret_key = "MOnyneRlFrL96X5DsDAigaR8c76YGA3obcPjMwO0"
        self.access_token = "1093205246-RNmJpbAE273s1x1prqEeeTWN5juhO9D1mNRXdFB"
        self.access_token_secret = "tHj1MYyUJli9Qba0gHvKGI9cpAcLS8SNIKYh2FCRD0"
        self.get_infos(sources, nb_infos)
        
    def get_infos(self, sources, nb_infos):
    
        api = twitter.Api(consumer_key=self.consumer_key,
                          consumer_secret=self.secret_key,
                          access_token_key=self.access_token,
                          access_token_secret=self.access_token_secret)
        
        tweets = api.GetHomeTimeline()
        
        for tweet in tweets:
            try:
                #origine
                origin = tweet.GetUser().GetScreenName()
                #title
                title = tweet.GetText()
                #BDD
                bdd_article = models.Twitter(titre=title,origine=origin)
                bdd_article.save()
            except:
                pass