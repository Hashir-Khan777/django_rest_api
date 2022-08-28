from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return {
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
