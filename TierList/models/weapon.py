from django.db import models

class Weapon(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        app_label = 'TierList'

    def __str__(self):
        return f'{self.name}'