from django.db import models

class Nation(models.Model):
    City = models.CharField(max_length=100)

    class Meta:
        app_label = 'TierList'

    def __str__(self):
        return self.City