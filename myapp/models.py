from django.db import models
from django.contrib.auth.models import User

# Proxy model - same database table as auth.User but shows under MYAPP in admin
class AppUser(User):
    class Meta:
        proxy = True
        verbose_name = 'App User'
        verbose_name_plural = 'App Users'
