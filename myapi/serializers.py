from rest_framework import serializers


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=256)
    year = serializers.IntegerField()
    # runtime = serializers.CharField()
    # status = serializers.CharField()
    # director = serializers.CharField()
    # country = serializers.CharField()
    # plot = serializers.CharField()
    # poster = serializers.CharField()
    # rating = serializers.CharField()
    # release_date = serializers.CharField()
    # genre = serializers.CharField()
    # cast = serializers.CharField()
    # datetime_created = serializers.CharField()
    # datetime_modified = serializers.CharField()