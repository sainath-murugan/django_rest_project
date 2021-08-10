from django.shortcuts import render
from job.models import Jobs
from .serializers import JobSerializer, UserSerializer
from rest_framework import generics, mixins, permissions
from .permissions import IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import get_user_model


CustomUser = get_user_model()

class JobList(mixins.CreateModelMixin,generics.ListAPIView):
    
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    pagination_class = PageNumberPagination
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    
   
    
    def post(self, request):
        return self.create(request)

    def perform_create(self, serializer):  
        serializer.save(user=self.request.user)

class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer
    permission_classes = [
        permissions.IsAuthenticated,
        IsOwnerOrReadOnly,
    ]

class UserDetails(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer