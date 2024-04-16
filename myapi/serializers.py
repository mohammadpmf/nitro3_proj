from rest_framework import serializers

class ArtistSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    nick_name = serializers.CharField()
    birth_date = serializers.DateField()

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=256)
    year = serializers.IntegerField()
    runtime = serializers.IntegerField()
    runtime_minutes = serializers.SerializerMethodField()
    status = serializers.CharField()
    director = ArtistSerializer()
    country = serializers.CharField()
    plot = serializers.CharField()
    poster = serializers.ImageField()
    rating = serializers.DecimalField(max_digits=3, decimal_places=1)
    release_date = serializers.DateField()
    # genre = serializers.CharField()
    # cast = serializers.CharField()
    # datetime_created = serializers.CharField()
    # datetime_modified = serializers.CharField()

    def get_runtime_minutes(self, movie):
        return f"{movie.runtime} minutes"