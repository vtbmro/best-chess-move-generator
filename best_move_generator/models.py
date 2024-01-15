from django.db import models
from django.contrib.auth.models import AbstractUser

# Note: the page doesn't need users to work but since one of the requi
# rements is that page uses at least one model here it is.

class User(AbstractUser):
    pass

