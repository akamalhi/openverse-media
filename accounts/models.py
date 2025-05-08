from django.contrib.auth.models import AbstractUser
from django.db import models

# CustomUser extends AbstractUser which already includes:
# username, password, first_name, last_name, email, is_active, is_staff, etc.
# This class adds additional fields: email (unique), address, and phone.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.username
