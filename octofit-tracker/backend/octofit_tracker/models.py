from djongo import models

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    team = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.username

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.JSONField(default=list)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.CharField(max_length=150)
    activity_type = models.CharField(max_length=100)
    duration = models.IntegerField()
    calories = models.IntegerField()
    timestamp = models.DateTimeField()
    def __str__(self):
        return f"{self.user} - {self.activity_type}"

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    score = models.IntegerField()
    def __str__(self):
        return f"{self.team}: {self.score}"

class Workout(models.Model):
    user = models.CharField(max_length=150)
    workout_type = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    date = models.DateField()
    def __str__(self):
        return f"{self.user} - {self.workout_type}"
