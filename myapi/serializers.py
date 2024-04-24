from rest_framework import serializers

from .models import Artist, GenreMovie, GenreMusic, Movie, Music, Serial, Staff


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'first_name', 'last_name', 'nick_name', 'birth_date']


class GenreMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreMovie
        fields = ['id', 'title']


class GenreMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreMusic
        fields = ['id', 'title']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'year', 'runtime', 'runtime_minutes',
                  'status', 'director', 'director_info', 'country', 'plot', 'poster',
                  'rating', 'release_date', 'genre', 'cast']
    
    runtime_minutes = serializers.SerializerMethodField()
    director = serializers.PrimaryKeyRelatedField(
        queryset = Artist.objects.all()
    )
    director_info = ArtistSerializer(source='director', read_only=True)
    genre = GenreMovieSerializer(many=True, read_only=True)
    cast = ArtistSerializer(many=True, read_only=True)

    def get_runtime_minutes(self, movie):
        return f"{movie.runtime} minutes"
    
    def validate(self, data):
        ALAKI_YEAR = 1945
        if data['year']==ALAKI_YEAR:
            raise serializers.ValidationError(f'The year {ALAKI_YEAR} was after WW2 and no movies released in {ALAKI_YEAR}!')
        return data
    
    # اگر تابع update رو بنویسیم، مطابق چیزی که ما نوشتیم عمل میکنه. اگه ننویسیم از دیفالت خودش استفاده میکنه.
    # def update(self, instance: Movie, validated_data):
    #     instance.plot = validated_data.get('plot', "اگه پلات ارسال نشده بود این رو بنویس :دی هر چیز دیگه ای رو هم میشه تغییر داد. نمونه نوشتم که داشته باشیم.")
    #     instance.save()
    #     return instance

class SerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serial
        exclude = ['datetime_created', 'datetime_modified']

    average_runtime_minutes = serializers.SerializerMethodField()
    director = serializers.PrimaryKeyRelatedField(
        queryset = Artist.objects.all()
    )
    director_info = ArtistSerializer(source='director', read_only=True)
    genre = GenreMovieSerializer(many=True, read_only=True)
    cast = ArtistSerializer(many=True, read_only=True)

    def get_average_runtime_minutes(self, serial):
        return f"{serial.average_runtime} minutes"
    

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        exclude = ['datetime_created', 'datetime_modified']

    duration_seconds = serializers.SerializerMethodField()
    duration_minutes = serializers.SerializerMethodField()
    main_singer = serializers.PrimaryKeyRelatedField(
        queryset = Artist.objects.all()
    )
    main_singer_info = ArtistSerializer(source='main_singer', read_only=True)
    genre = GenreMovieSerializer(many=True, read_only=True)
    other_singers = ArtistSerializer(many=True, read_only=True)

    def get_duration_seconds(self, music):
        return f"{music.duration} seconds"
    
    def get_duration_minutes(self, music):
        t = music.duration
        m = t//60
        s = t%60
        return f"{m:02}:{s:02}"
    

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['user', 'username', 'email', 'full_name',  'phone_number']
        read_only_fields = ['user']


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
    