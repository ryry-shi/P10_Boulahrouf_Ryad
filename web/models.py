from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    # USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=50)


class Projects(models.Model):

    project_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="project")

class Contributors(models.Model):

    user_id = models.IntegerField()
    project_id = models.IntegerField()
    role = models.CharField(max_length=50)

class Issues(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    priority = models.CharField(max_length=50)
    project_id = models.IntegerField()
    status = models.CharField(max_length=50)
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="author_issues")
    assignee_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="assigne")
    created_time = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    comments = models.IntegerField()
    description = models.CharField(max_length=50)
    author_user_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="comment_user")
    issue_id = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="comment_issue")
    created_time = models.DateTimeField(auto_created=True)
