from rest_framework.serializers import ModelSerializer
from .models import Folder,File,User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['name'] = user.first_name
        token['username'] = user.username


        return token


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')


class FolderSerializer(ModelSerializer):
    class Meta:
        model = Folder
        fields = ('id','name','created_at','user')


class FileSerializer(ModelSerializer):
    class Meta:
        model = File
        fields = ('id','name','folder','created_at','user')