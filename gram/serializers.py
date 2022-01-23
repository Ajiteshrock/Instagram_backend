from http import server
from sqlite3 import Cursor
from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model

class ObtainPairSerializer(TokenObtainPairSerializer):
   
    @classmethod
    def get_token(cls, user):
        token = super(ObtainPairSerializer, cls).get_token(user)
        token['username'] = user.email
        return token
    
    def validate(self,attrs):
        data = super(ObtainPairSerializer, self).validate(attrs)
        user_model = get_user_model()
        obj = user_model.objects.get(email = self.user.email)
        name = obj.name
        print("*****************************")
        data.update({'user': self.user.email})
        data.update({'name': name})
        return data


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True,write_only=True)
    age  = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = ('email','password','age','name')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Albums
        fields = "__all__"

class DraftSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drafts
        fields = "__all__"

class HashtagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hashtags
        fields = "__all__"