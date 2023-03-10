from .models import Comments, User, Projects, Contributors, Issues
from rest_framework import serializers
from django.contrib.auth.hashers import (
    make_password,
)

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = User
        fields = ["username", "password", "last_name", "email"]


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            last_name=validated_data["last_name"],
            password=make_password(validated_data["password"])
        )
        user.save()
        return user

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Projects
        fields = ["title", "description", "type", "author_user_id"]

    def create_projects(self, validate_data):
        project = Projects.objects.create(**validate_data)
        project.save()
        return project 

class ContributorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Contributors
        fields = ["role","user_id", "project_id"]

    def create_contributors(self, validate_data):
        user = Contributors.objects.create(**validate_data)
        user.save()
        return user

class IssueSerializer(serializers.ModelSerializer):

    class Meta:

        model = Issues
        fields = ["title","desc","tag","priority","status","author_user_id","assignee_user_id"]

        def create_issue(self, validate_data):
            project = Projects.objects.create(**validate_data)
            project.save()
            return project 


class CommentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Comments
        fields = ["comments", "issue_id", "author_user_id"]