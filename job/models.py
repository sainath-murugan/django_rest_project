from django.db import models
from django.utils import timezone
from rest_framework.reverse import reverse as api_reverse
from django.contrib.auth import get_user_model
import uuid

CustomUser = get_user_model()

class Jobs(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    user = models.ForeignKey(CustomUser, related_name='customer_user_job', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.title}"
    
    def get_absolute_api_url(self, request):
        return api_reverse('detail_view',kwargs={'id': str(self.id)},request=request)