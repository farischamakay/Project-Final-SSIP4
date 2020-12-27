from django.db import models

class Element(models.Model):
    element = models.CharField(max_length=50)

    class Meta:
        app_label = 'TierList'

    def __str__(self):
        return self.element