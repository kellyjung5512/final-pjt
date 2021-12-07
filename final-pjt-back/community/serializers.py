from rest_framework import serializers
from .models import Community, Comment

class CommunitySerializer(serializers.ModelSerializer):
    auth_user = serializers.SerializerMethodField()

    def get_auth_user(self, objects):
        return objects.user.username

    class Meta:
        model = Community
        fields = '__all__' 
        read_only_fields = ('user',)
       
class CommentSerializer(serializers.ModelSerializer):
    auth_user = serializers.SerializerMethodField()

    def get_auth_user(self, objects):
        return objects.user.username

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'community',)