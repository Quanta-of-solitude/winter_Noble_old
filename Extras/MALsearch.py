from bs4 import BeautifulSoup as parse
import requests
'''
For MyAnimeList, searching animes/manga/OVA using name instead of IDs

'''

__author__ = "Nub"

class MAL:
    '''a MYANIMELIST PARSER'''
    def __init__(self):
        self.name = "MAL SEARCH"

    def asearch(self, query:str = None):

        '''Getting the Result List'''

        try:
            if query == None:
                print("Missing Anime Name!")
                return

            anime_names = []
            text = query.lower()
            text = text.replace(' ', '+')
            link_anime = "https://myanimelist.net/anime.php?q="+text+"&type=0&score=0&status=0&p=0&r=0&sm=0&sd=0&sy=0&em=0&ed=0&ey=0&c[]=a&c[]=b&c[]=c&c[]=f&gx=0"
            r = requests.get(link_anime)
            s = parse(r.content, 'lxml')
            data_names = s.find_all("a", {"class": "hoverinfo_trigger fw-b fl-l"})
            refined = "None"
            for x in data_names:
                names = x.text
                anime_names.append("⭐ "+names)
            refined = '\n'.join(anime_names[:7])
            #print("Top 7 Search Results:\n\n"+refined)
            return refined
        except Exception as e:
            print(e)

    def adata(self, query:str = None):

        '''Getting the links to the selected result'''

        try:
            if query == None:
                print("Missing Name!")
                return

            anime_links = []
            anime_names = []
            query = query.lower()
            text = query.replace(' ', '+')
            link_anime = "https://myanimelist.net/anime.php?q="+text+"&type=0&score=0&status=0&p=0&r=0&sm=0&sd=0&sy=0&em=0&ed=0&ey=0&c[]=a&c[]=b&c[]=c&c[]=f&gx=0"
            r = requests.get(link_anime)
            s = parse(r.content, 'lxml')
            data_links = s.find_all("a", {"class": "hoverinfo_trigger fw-b fl-l"})
            for x in data_links:
                names = x.text.lower()
                links = x["href"]
                anime_links.append(links)
                anime_names.append(names)
            anime_names = anime_names[:7]
            anime_links = anime_links[:7]
            #print(anime_names)
            link_found = "None"
            if query in anime_names:
                n = anime_names.index("{}".format(query))
                #print(n)
                link_found = anime_links[n]
            return link_found
        except Exception as e:
            print(e)

if __name__ == "__main__":
    MAL()
