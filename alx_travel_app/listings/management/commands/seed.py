from django.core.management.base import BaseCommand
from alx_travel_app.listings.models import Listing, Booking, Review
from django.contrib.auth.models import User
from datetime import date
import random

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **kwargs):
        # Create sample users
        users = [User.objects.create_user(username=f'user{i}', password='password') for i in range(1, 6)]

        # Create sample listings
        listings = [
            Listing.objects.create(
                title=f"Listing {i}",
                description=f"Description for Listing {i}",
                price_per_night=random.randint(50, 500),
                location=f"Location {i}",
                owner=users[random.randint(0, 4)]
            ) for i in range(1, 6)
        ]

        # Create sample bookings
        bookings = [
            Booking.objects.create(
                listing=listings[random.randint(0, 4)],
                user=users[random.randint(0, 4)],
                check_in_date=date.today(),
                check_out_date=date.today(),
                status=random.choice(['pending', 'confirmed', 'cancelled'])
            ) for _ in range(5)
        ]

        # Create sample reviews
        reviews = [
            Review.objects.create(
                listing=listings[random.randint(0, 4)],
                user=users[random.randint(0, 4)],
                rating=random.randint(1, 5),
                comment=f"Comment for review {i}",
            ) for i in range(1, 6)
        ]

        self.stdout.write(self.style.SUCCESS('Database seeded successfully'))
