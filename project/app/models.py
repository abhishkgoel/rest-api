from django.db import models

class Para(models.Model):
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title