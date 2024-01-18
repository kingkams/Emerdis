from myuser.models import Assembly, People
from django.db import models
import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


class PeoplePosts(models.Model):
    CHOICES = (('Emergency', 'emergency'), ('Community Concern', 'community concern'))
    id = models.UUIDField(unique=True, primary_key=True, editable=False, default=uuid.uuid4())
    author = models.ForeignKey(People, on_delete=models.CASCADE)
    problem = models.TextField()
    category = models.CharField(max_length=50, choices=CHOICES, default=CHOICES[0])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='people/', null=True, blank=True)

    def __str__(self):
        return f"{self.author.first_name}"


class AssemblyPost(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, editable=False, default=uuid.uuid4())
    author = models.ForeignKey(Assembly, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=300)
    main_image = models.ImageField(upload_to='Assembly', null=True, blank=True)
    supporting_image1 = models.ImageField(upload_to='Assembly', null=True, blank=True)
    supporting_image2 = models.ImageField(upload_to='Assembly', null=True, blank=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



