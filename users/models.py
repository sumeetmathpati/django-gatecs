from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    GENDER_TYPE = (
        ('m', "Male"),
        ('f', "Female"),
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_TYPE, null=True, blank=True)

    def __str__(self):
        return self.user.username
