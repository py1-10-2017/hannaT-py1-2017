from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    post = models.TextField()
    created_at = models.DateField(auto_now_add=	True)