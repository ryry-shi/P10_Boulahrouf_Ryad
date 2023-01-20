from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializer import CommentSerializer, UserSerializer, ProjectSerializer, IssueSerializer
from .models import User, Projects, Issues


class UserAPIView(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, *args, **kwargs):
        queryset = User.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

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
    queryset = Issues.objects.all()

    def get(self, request, *arg, **kwargs):
        queryset = Issues.objects.all()
        serializer = self.serializer_class(data=queryset)
        return Response(serializer.data)

    def put(self, project_id, *args, **kwargs):
        issue_data = Issues.objects.get(pk=project_id)
        serializer = self.serializer_class(data=issue_data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, project_id, *args, **kwargs):
        issue = Issues.objects.get(pk=project_id)
        issue.delete()
        return issue

class CommentAPIView(viewsets.ModelViewSet):

    serializer_class = CommentSerializer
