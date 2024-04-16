from rest_framework import serializers


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=256)
    year = serializers.IntegerField()
    runtime = serializers.IntegerField()
    status = serializers.CharField()
    director = serializers.CharField()
    country = serializers.CharField()
    plot = serializers.CharField()
    poster = serializers.ImageField()
    rating = serializers.DecimalField(max_digits=3, decimal_places=1)
    release_date = serializers.DateField()
    # genre = serializers.CharField()
    # cast = serializers.CharField()
    # datetime_created = serializers.CharField()
    # datetime_modified = serializers.CharField()