from GeekHub.models import Article
import datetime
from django.db.models import Max


class Proxy():
    
    def init(self):
        pass
    
    def get_most_visited_site(self):
        
        site_visites = {}
        date = datetime.datetime.now() - datetime.timedelta(40)
        articles = Article.objects.filter(date__gt=date).all()
        
        for article in articles:
            if site_visites.has_key(article.origine):
                site_visites[article.origine][2] += article.visites
                site_visites[article.origine][3] += 1
            else:
                site_visites[article.origine] = [article.origine, article.lien, article.visites, 1]
                
        tabs = [site_visites[key] for key in site_visites.keys()] 
        tabs.sort(key=lambda x: x[2])

        return tabs[-1] + [tabs[-1][2] / tabs[-1][3]]
    
    def get_most_visited_article(self):
        
        date = datetime.datetime.now() - datetime.timedelta(40)
        articles = Article.objects.filter(date__gt=date).order_by('-visites')
        
        return articles[0]
                
        