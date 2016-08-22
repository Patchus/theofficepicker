import random
import os
import webbrowser
import sys

the_office_seasons = [{'season':1,'episodes':6,'start_url':70069628},
                      {'season':2,'episodes':22,'start_url':70069633},
                      {'season':3,'episodes':25,'start_url':70080635},
                      {'season':4,'episodes':19,'start_url':70108689},
                      {'season':5,'episodes':28,'start_url':70126223},
                      {'season':6,'episodes':26,'start_url':70151942},
                      {'season':7,'episodes':27,'start_url':70189006},
                      {'season':8,'episodes':24,'start_url':70210965},
                      {'season':9,'episodes':25,'start_url':70286845}]

try:
    not_allowed = sys.argv[1]
except:
    print 'Cool All Episodes'
    not_allowed = []

def create_collection():
    the_office_collection = []
    episode_number = 0
    for season in xrange(1,len(the_office_seasons)):
        for episode in xrange(1,the_office_seasons[season]['episodes']):
            episode_number += 1
            the_office_collection.append({'season':season,
                                      'episode':episode,
                                      'number': episode_number,
                                      'url':the_office_seasons[season]['start_url']})
    return the_office_collection

def remove_unwanted(collection,unwanted):
    to_remove = []
    for ep in xrange(1,len(collection)):
        if collection[ep]['season'] in unwanted:            
            to_remove.append(collection[ep])
            
    return [x for x in collection if x not in to_remove]

if __name__ == '__main__':
    episodes = create_collection()
    clean = remove_unwanted(episodes,not_allowed)
    chosen = clean[random.randrange(len(clean))]
    url = 'https://www.netflix.com/watch/{}'
    webbrowser.open_new_tab(url.format(chosen['url']+chosen['episode']-1))
