from django.db import models

class Entry(models.Model):
    name = models.CharField(max_length=200)
    baker = models.CharField(max_length=200)

    def __str__(self):
        return "%s by %s" % (self.name, self.baker)

class TimeToVote(models.Model):
    timeToVote = models.BooleanField()

    def __str__(self):
        return "%b" % self.timeToVote
