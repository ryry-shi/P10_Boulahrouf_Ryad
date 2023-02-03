from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .serializer import CommentSerializer, UserSerializer, ProjectSerializer, IssueSerializer, ContributorSerializer
from .models import User, Projects, Issues, Comments, Contributors


class UserAPIView(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, *args, **kwargs):
        users = get_object_or_404(self.queryset, users=self.kwargs["username"])
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)


    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

    def post(self, request, *args, **kwargs):
        users_data = request.data
        serializer = self.serializer_class(data=users_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectAPIView(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    queryset = Projects.objects.all()

    def get(self, *args, **kwargs):
        queryset = Projects.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        project = request.data
        serializer = self.serializer_class(data=project)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, project_id, *args, **kwargs):
        project_data = Projects.objects.get(pk=project_id)
        serializer = self.serializer_class(data=project_data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, project_id, *args, **kwargs):
        project = Projects.objects.get(pk=project_id)
        project.delete()
        return project

class IssueAPIView(viewsets.ModelViewSet):

    serializer_class = IssueSerializer
    queryset = Contributors.objects.all()

    def get(self, *args, **kwargs):
        queryset = Contributors.objects.all()
        serializer = self.serializer_class(data=queryset)
        return Response(serializer.data)

    # def post():

    def put(self, project_id, *args, **kwargs):
        issue_data = Issues.objects.get(pk=project_id)
        serializer = self.serializer_class(data=issue_data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, project_id, *args, **kwargs):
        issue = Issues.objects.get(pk=project_id)
        issue.delete()
        return issue


class ContributorAPIView(viewsets.ModelViewSet):

    serializer_class = ContributorSerializer
    queryset = Contributors.objects.all()


    def get(self, *arg, **kwargs):
        queryset = Contributors.objects.all()
        serializer = self.serializer_class(data=queryset)
        return Response(serializer.data)

    # # def post():

    # def put(self, project_id, *args, **kwargs):
    #     issue_data = Contributors.objects.get(pk=project_id)
    #     serializer = self.serializer_class(data=issue_data)
    #     if serializer.is_valid():
    #         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    # def delete(self, project_id, *args, **kwargs):
    #     issue = Contributors.objects.get(pk=project_id)
    #     issue.delete()
    #     return issue


class CommentAPIView(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
    queryset = Comments.objects.all()