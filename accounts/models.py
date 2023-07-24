from django.db import models
from django.contrib.auth.models import AbstractUser

# This is here to facilitate extensions to django standard user class
# which would be difficult to do later on. (after any migrations have been done)


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
