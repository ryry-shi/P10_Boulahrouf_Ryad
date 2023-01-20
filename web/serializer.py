from .models import User, Projects, Contributors, Issues
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = User
        fields = ["username", "password", "last_name", "email"]

        def create(self, validated_data):
                user = User.objects.create(
                    username=validated_data["username"],
                    email=validated_data["email"],
                    first_name=validated_data["first_name"],
                    last_name=validated_data["last_name"],
                )
                user.set_password(validated_data["password"])
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

class IssueSerializer(serializers.ModelSerializer):

    class Meta:

        model = Issues
        fields = ["title","desc","tag","priority","status","project_id","author_user_id","assignee_user_id"]

        def create_issue(self, validate_data):
            project = Projects.objects.create(**validate_data)
            project.save()
            return project 