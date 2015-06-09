from django.db import models
from django.contrib.auth.models import User


class Token_auth(models.Model):
    user = models.ForeignKey(User,
                             blank=False)
    token = models.CharField('Token',
                             max_length=100,
                             blank=False)
    date = models.DateTimeField(auto_now_add=True,
                                blank=True)
