import random
from faker import Faker

from django.db import transaction
from django.core.management.base import BaseCommand

from myapi.models import GenreMovie, GenreMusic, Artist, Movie, Serial, Music, Image
from myapi.factories import GenreMovieFactory, GenreMusicFactory, ArtistFactory, MovieFactory, SerialFactory, MusicFactory, ImageFactory

faker = Faker()

list_of_models = [GenreMovie, GenreMusic, Artist, Movie, Serial, Music, Image]

NUMBER_OF_GENREMOVIE = 20
NUMBER_OF_GENREMUSIC = 25
NUMBER_OF_ARTISTS = 700
NUMBER_OF_MOVIES = 200
NUMBER_OF_SERIES = 100
NUMBER_OF_MUSICS = 500
NUMBER_OF_IMAGES = 500

class Command(BaseCommand):
    help = "Generates fake data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = list_of_models
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...\n")

        # genre movies
        print(f"Adding {NUMBER_OF_GENREMOVIE} genre for movies ... ", end='')
        all_genre_movies = [GenreMovieFactory() for _ in range(NUMBER_OF_GENREMOVIE)]
        print('DONE')
        
        # genre musics
        print(f"Adding {NUMBER_OF_GENREMUSIC} genre for musics ... ", end='')
        all_genre_musics = [GenreMusicFactory() for _ in range(NUMBER_OF_GENREMUSIC)]
        print('DONE')

        # artists
        print(f"Adding {NUMBER_OF_ARTISTS} artists ... ", end='')
        all_artists = [ArtistFactory() for _ in range(NUMBER_OF_ARTISTS)]
        print('DONE')

        # movies
        print(f"Adding {NUMBER_OF_MOVIES} movies ...", end='')
        all_movies = list()
        for _ in range(NUMBER_OF_MOVIES):
            new_movie = MovieFactory(director_id=random.choice(all_artists).id)
            new_movie.genre.set(random.choices(all_genre_movies, k=random.randint(1, 4)))
            new_movie.cast.set(random.choices(all_artists, k=random.randint(1, 12)))
            all_movies.append(new_movie)
        print('DONE')

        # series
        print(f"Adding {NUMBER_OF_SERIES} series ...", end='')
        all_series = list()
        for _ in range(NUMBER_OF_SERIES):
            new_serial = SerialFactory(director_id=random.choice(all_artists).id)
            new_serial.genre.set(random.choices(all_genre_movies, k=random.randint(1, 4)))
            new_serial.cast.set(random.choices(all_artists, k=random.randint(1, 12)))
            all_series.append(new_serial)
        print('DONE')

        # music
        print(f"Adding {NUMBER_OF_MUSICS} music ...", end='')
        all_musics = list()
        for _ in range(NUMBER_OF_MUSICS):
            new_music = MusicFactory(main_singer_id=random.choice(all_artists).id)
            new_music.genre.set(random.choices(all_genre_musics, k=random.randint(1, 2)))
            new_music.other_singers.set(random.choices(all_artists, k=random.randint(0, 4)))
            all_musics.append(new_music)
        print('DONE')