from rest_framework import serializers
from django.contrib.auth.models import User
from .models import NotesDb,TaskDb


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    class Meta:
        model= User
        fields = ["id", "username", "email", "password"]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        return user

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotesDb
        fields = ["id", "user", "title", "description", "created_at", "updated_at"]
        read_only_fields = ["user"]


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskDb
        fields = '__all__'
        read_only_fields = ['user', 'created_date']

