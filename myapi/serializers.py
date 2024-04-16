from rest_framework import serializers

from .models import Artist, Movie, Music, Serial


class GenreMovieSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=256)


class GenreMusicSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=256)


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'first_name', 'last_name', 'nick_name', 'birth_date']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'runtime', 'runtime_minutes',
                  'status', 'director', 'country', 'plot', 'poster',
                  'rating', 'release_date', 'genre', 'cast']
    
    runtime_minutes = serializers.SerializerMethodField()
    director = ArtistSerializer()
    genre = [GenreMovieSerializer()]
    cast = [ArtistSerializer()]
    # datetime_created = serializers.CharField()
    # datetime_modified = serializers.CharField()

    def get_runtime_minutes(self, movie):
        return f"{movie.runtime} minutes"
    

class SerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serial
        exclude = ['datetime_created', 'datetime_modified']

    director = ArtistSerializer()
    average_runtime_minutes = serializers.SerializerMethodField()
    genre = [GenreMovieSerializer()]
    cast = [ArtistSerializer()]

    def get_average_runtime_minutes(self, serial):
        return f"{serial.average_runtime} minutes"
    

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        exclude = ['datetime_created', 'datetime_modified']

    main_singer = ArtistSerializer()
    duration_seconds = serializers.SerializerMethodField()
    duration_minutes = serializers.SerializerMethodField()
    genre = [GenreMusicSerializer()]
    other_singers = [ArtistSerializer()]

    def get_duration_seconds(self, music):
        return f"{music.duration} seconds"
    
    def get_duration_minutes(self, music):
        t = music.duration
        m = t//60
        s = t%60
        return f"{m:02}:{s:02}"
    




# class ArtistSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     nick_name = serializers.CharField()
#     birth_date = serializers.DateField()


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=256)
#     year = serializers.IntegerField()
#     runtime = serializers.IntegerField()
#     runtime_minutes = serializers.SerializerMethodField()
#     status = serializers.CharField()
#     director = ArtistSerializer()
#     country = serializers.CharField()
#     plot = serializers.CharField()
#     poster = serializers.ImageField()
#     rating = serializers.DecimalField(max_digits=3, decimal_places=1)
#     release_date = serializers.DateField()
#     # genre = serializers.CharField()
#     # cast = serializers.CharField()
#     # datetime_created = serializers.CharField()
#     # datetime_modified = serializers.CharField()

#     def get_runtime_minutes(self, movie):
#         return f"{movie.runtime} minutes"
    

# class SerialSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField()
#     number_of_seasons = serializers.IntegerField()
#     number_of_episodes = serializers.IntegerField()
#     begin_year = serializers.IntegerField()
#     end_year = serializers.IntegerField()
#     average_runtime = serializers.IntegerField()
#     average_runtime_minutes = serializers.SerializerMethodField()
#     director = ArtistSerializer()
#     country = serializers.CharField()
#     plot = serializers.CharField()
#     poster = serializers.ImageField()
#     rating = serializers.DecimalField(max_digits=3, decimal_places=1)
#     start_release_date = serializers.DateField()
#     end_release_date = serializers.DateField()
#     # genre = serializers.CharField()
#     # cast = serializers.CharField()
#     # datetime_created = serializers.CharField()
#     # datetime_modified = serializers.CharField()

#     def get_average_runtime_minutes(self, serial):
#         return f"{serial.average_runtime} minutes"
    

# class MusicSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     year = serializers.IntegerField()
#     duration = serializers.IntegerField()
#     duration_seconds = serializers.SerializerMethodField()
#     duration_minutes = serializers.SerializerMethodField()
#     main_singer = ArtistSerializer()
#     file = serializers.FileField()
#     lyrics = serializers.CharField()
#     poster = serializers.ImageField()
#     release_date = serializers.DateField()
#     # genre = serializers.CharField()
#     # other_singers = serializers.CharField()
#     # datetime_created = serializers.CharField()
#     # datetime_modified = serializers.CharField()

#     def get_duration_seconds(self, music):
#         return f"{music.duration} seconds"
    
#     def get_duration_minutes(self, music):
#         t = music.duration
#         m = t//60
#         s = t%60
#         return f"{m:02}:{s:02}"
    