from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='testuser').exists():
            User.objects.create_user(username='testuser', password='testpass')
            self.stdout.write(self.style.SUCCESS('Created test user'))
        else:
            self.stdout.write(self.style.WARNING('Test user already exists'))
        # Add more test data creation as needed
from django.core.management.base import BaseCommand
from octofit_tracker.models import User  # Adjust imports as needed for your models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Example: Create test users
        if not User.objects.filter(username='testuser').exists():
            User.objects.create_user(username='testuser', password='testpass')
            self.stdout.write(self.style.SUCCESS('Created test user'))
        else:
            self.stdout.write(self.style.WARNING('Test user already exists'))
        # Add more test data creation as needed
