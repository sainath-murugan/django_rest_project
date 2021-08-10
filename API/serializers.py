from rest_framework import serializers
from job.models import Jobs
from django.contrib.auth import get_user_model


CustomUser = get_user_model()

class JobSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    posted_by = serializers.SerializerMethodField(read_only=True)
    class Meta:
        fields = [
            'url',
            'title',
            'description', 
            'date_created',
            'posted_by']
        read_only_fields = [
            'url',
            'date_created',
            'posted_by']
        model = Jobs

    def get_url(self, object):
        url = self.context.get('request')
        return object.get_absolute_api_url(request=url)

    def get_posted_by(self, object):
        return object.user.username

class UserSerializer(serializers.ModelSerializer):
    jobs_posted_by_him = serializers.SerializerMethodField(read_only=True)

    class Meta:
        fields = [
            'id',
            'username',
            'email',
            'jobs_posted_by_him'
        ]
        model = CustomUser
    
    def get_jobs_posted_by_him(self, object):
        list_ = []
        url = self.context.get('request')
        for items in object.customer_user_job.all():
            list_.append(items.get_absolute_api_url(request=url))
        return list_
