from django.core.management.base import BaseCommand
from django.conf import settings
from django.db import connection
from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'users'

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'teams'

class Activity(models.Model):
    user_email = models.EmailField()
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'activities'

class Leaderboard(models.Model):
    team = models.CharField(max_length=50)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'leaderboard'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'
        db_table = 'workouts'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User(email='tony@stark.com', name='Tony Stark', team='Marvel'),
            User(email='steve@rogers.com', name='Steve Rogers', team='Marvel'),
            User(email='bruce@wayne.com', name='Bruce Wayne', team='DC'),
            User(email='clark@kent.com', name='Clark Kent', team='DC'),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user_email='tony@stark.com', type='Running', duration=30),
            Activity(user_email='steve@rogers.com', type='Cycling', duration=45),
            Activity(user_email='bruce@wayne.com', type='Swimming', duration=60),
            Activity(user_email='clark@kent.com', type='Yoga', duration=20),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=75)
        Leaderboard.objects.create(team='DC', points=80)

        # Create workouts
        workouts = [
            Workout(name='Super Strength', difficulty='Hard'),
            Workout(name='Flight Training', difficulty='Medium'),
            Workout(name='Shield Practice', difficulty='Easy'),
        ]
        Workout.objects.bulk_create(workouts)


        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
