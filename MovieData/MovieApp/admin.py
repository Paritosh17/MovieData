from django.contrib import admin
from .models import Movie, Genre

'''
Model needs to be registered
'''

class GenreAdmin(admin.ModelAdmin):
	pass

class MovieAdmin(admin.ModelAdmin):
    dis = ['name', 'imdb_score', 'director', 'popularity']
    filt = ['genre']
    search = ['name', 'director']
    pass



admin.site.register(Movie, MovieAdmin)
admin.site.register(Genre, GenreAdmin)