from rest_framework import serializers
from .models import Movie


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_users',)


# class WorldcupSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Worldcup
#         fields = '__all__'