from __future__ import unicode_literals

from django.db import models

class NoteManager(models.Model):
    note = models.CharField(max_length=255)
    description = models.TextField()
    