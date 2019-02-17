from django.db import models

class DownVote(models.Model):
    post_id = models.TextField()
    user_profile = models.TextField()

