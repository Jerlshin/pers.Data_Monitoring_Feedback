from django.db import models

class UserInput(models.Model):
    date = models.DateField(auto_now_add=True)
    read_bible = models.BooleanField(default=False)
    prayed = models.BooleanField(default=False)
    exercised = models.BooleanField(default=False)
    satisfied = models.BooleanField(default=False)
    hurt_someone = models.BooleanField(default=False)
    loved_someone = models.CharField(max_length=100)
    daily_summary = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.date}: {self.loved_someone}"


