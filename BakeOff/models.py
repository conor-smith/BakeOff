from django.db import models

class Entry(models.Model):
    name = models.CharField(max_length=200)
    baker = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " by " + self.baker
