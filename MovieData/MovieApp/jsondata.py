import json
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from ...models import Movie, Genre
from pathlib import Path


'''
Converting Data into other format
We load data from here to our databases
Command to upload the data : python manage.py jsondata
'''
class Command(BaseCommand):

    def handle(self, *args, **options):
        
        filepath = settings.BASE_DIR / '/imdb.json'
        with open(filepath, 'r') as f:
            raw_data = f.read()
            data = json.loads(raw_data)
            #print(data)
            dic = {}
            for movie_item in data:
                dic['name'] = movie_item.get('name')
                dic['popularity'] = movie_item.get('99popularity')
                dic['director'] = movie_item.get('director')
                dic['imdb_score'] = movie_item.get('imdb_score')
                movie, created = Movie.objects.get_or_create(**dic)
                genre_list = movie_item.get('genre')
                for name in genre_list:
                    name = name.strip()
                    genre, created = Genre.objects.get_or_create(name=name)
                    movie.genre.add(genre)
            
                movie.save()
                print ("Movie Name is " , movie)