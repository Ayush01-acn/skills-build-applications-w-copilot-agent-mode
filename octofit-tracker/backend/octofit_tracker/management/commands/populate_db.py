from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Users (superheroes)
        users = [
            User(email='tony@stark.com', name='Iron Man', team='marvel'),
            User(email='steve@rogers.com', name='Captain America', team='marvel'),
            User(email='bruce@wayne.com', name='Batman', team='dc'),
            User(email='clark@kent.com', name='Superman', team='dc'),
        ]
        for user in users:
            user.save()

        # Activities
        activities = [
            Activity(user='Iron Man', activity_type='run', duration=30),
            Activity(user='Captain America', activity_type='cycle', duration=45),
            Activity(user='Batman', activity_type='swim', duration=25),
            Activity(user='Superman', activity_type='fly', duration=60),
        ]
        for activity in activities:
            activity.save()

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        # Workouts
        workouts = [
            Workout(name='Super Strength', description='Lift heavy weights', suggested_for='dc'),
            Workout(name='Flight Training', description='Practice flying', suggested_for='dc'),
            Workout(name='Shield Throw', description='Throw and catch shield', suggested_for='marvel'),
            Workout(name='Tech Run', description='Run in Iron Man suit', suggested_for='marvel'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
