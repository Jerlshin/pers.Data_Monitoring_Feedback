from django.db import models

class UserInput(models.Model):
    date = models.DateField(auto_now_add=True)
    
    read_bible = models.BooleanField(default=False)
    prayer_god = models.BooleanField(default=False)
    exercised_or_played = models.BooleanField(default=False)
    book_reading = models.BooleanField(default=False)
    studying_machine_learning = models.BooleanField(default=False)
    maintained_purity = models.BooleanField(default=False)
    cultivated_relationships = models.BooleanField(default=False)
    woke_up_at_5am = models.BooleanField(default=False)
    healthy_eating = models.BooleanField(default=False)
    hurt_someone = models.BooleanField(default=False)
    wasted_time = models.BooleanField(default=False)
    
    # char fields
    loved_someone = models.CharField(max_length=100)
    daily_summary = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.date}: {self.loved_someone}"

class Quote(models.Model):
    text = models.TextField(max_length=3000)
    
    def __str__(self):
        return self.text[:50] # Show first 50 characters of the quote in admin

