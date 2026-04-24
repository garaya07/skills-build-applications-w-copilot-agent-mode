from django.core.management.base import BaseCommand
from octofit_tracker.models import UserProfile, Team, Activity, Workout, Leaderboard
import datetime

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Create test users
        if not UserProfile.objects.filter(email='alice@example.com').exists():
            alice = UserProfile.objects.create(email='alice@example.com', name='Alice', team='Team Alpha')
            self.stdout.write(self.style.SUCCESS('Created user Alice'))
        else:
            alice = UserProfile.objects.get(email='alice@example.com')
            self.stdout.write(self.style.WARNING('User Alice already exists'))

        if not UserProfile.objects.filter(email='bob@example.com').exists():
            bob = UserProfile.objects.create(email='bob@example.com', name='Bob', team='Team Beta')
            self.stdout.write(self.style.SUCCESS('Created user Bob'))
        else:
            bob = UserProfile.objects.get(email='bob@example.com')
            self.stdout.write(self.style.WARNING('User Bob already exists'))

        # Create test teams
        if not Team.objects.filter(name='Team Alpha').exists():
            Team.objects.create(name='Team Alpha', description='The alpha team')
            self.stdout.write(self.style.SUCCESS('Created Team Alpha'))
        else:
            self.stdout.write(self.style.WARNING('Team Alpha already exists'))

        if not Team.objects.filter(name='Team Beta').exists():
            Team.objects.create(name='Team Beta', description='The beta team')
            self.stdout.write(self.style.SUCCESS('Created Team Beta'))
        else:
            self.stdout.write(self.style.WARNING('Team Beta already exists'))

        # Create test activities
        if not Activity.objects.filter(user=alice, activity_type='Running').exists():
            Activity.objects.create(user=alice, activity_type='Running', duration=30, date=datetime.date.today())
            self.stdout.write(self.style.SUCCESS('Created activity for Alice'))
        else:
            self.stdout.write(self.style.WARNING('Activity for Alice already exists'))

        # Create test workouts
        if not Workout.objects.filter(name='Morning Run').exists():
            Workout.objects.create(name='Morning Run', description='A light morning run', difficulty='Easy')
            self.stdout.write(self.style.SUCCESS('Created Morning Run workout'))
        else:
            self.stdout.write(self.style.WARNING('Morning Run workout already exists'))

        # Create test leaderboard entries
        if not Leaderboard.objects.filter(user=alice).exists():
            Leaderboard.objects.create(user=alice, score=100, rank=1)
            self.stdout.write(self.style.SUCCESS('Created leaderboard entry for Alice'))
        else:
            self.stdout.write(self.style.WARNING('Leaderboard entry for Alice already exists'))
