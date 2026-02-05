from rest_framework import serializers

# User Serializer
class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=30, required=False)
    last_name = serializers.CharField(max_length=30, required=False)
    team = serializers.CharField(max_length=100, required=False)

# Team Serializer
class TeamSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    members = serializers.ListField(child=serializers.CharField(max_length=150))
    score = serializers.IntegerField(default=0)

# Activity Serializer
class ActivitySerializer(serializers.Serializer):
    user = serializers.CharField(max_length=150)
    activity_type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
    calories = serializers.IntegerField()
    timestamp = serializers.DateTimeField()

# Leaderboard Serializer
class LeaderboardSerializer(serializers.Serializer):
    team = serializers.CharField(max_length=100)
    score = serializers.IntegerField()

# Workout Serializer
class WorkoutSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=150)
    workout_type = serializers.CharField(max_length=100)
    details = serializers.CharField(max_length=500)
    date = serializers.DateField()
