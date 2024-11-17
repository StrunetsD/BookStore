import os
import django
import random
from faker import Faker
from django.core.management.base import BaseCommand
from book.models import Author, Category, Book, Review
from publishing_house.models import PublishingHouse
from user.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with fake data'

    def handle(self, *args, **kwargs):
        self.populate()

    def populate(self):
        categories = []
        for _ in range(5):  
            category = Category.objects.create(
                name=fake.word().capitalize(),
                description=fake.text(max_nb_chars=200)
            )
            categories.append(category)

        authors = []
        for _ in range(10): 
            author = Author.objects.create(
                name=fake.name(),
                date=fake.date_time_this_decade(),
                biography=fake.text(max_nb_chars=500)
            )
            authors.append(author)

       
        publishing_houses = PublishingHouse.objects.all()  
        for _ in range(20):  
            book = Book.objects.create(
                title=fake.sentence(nb_words=4),
                price=random.uniform(5.0, 100.0),
                image='', 
                description=fake.text(max_nb_chars=1000),
                review=fake.text(max_nb_chars=500),
                publishing_house=random.choice(publishing_houses),
                author_name=random.choice(authors),
                category=random.choice(categories)
            )

        users = []
        for _ in range(5):  
            user = User.objects.create_user(
                username=fake.user_name(),
                password='password123', 
                email=fake.email()
            )
            users.append(user)

        books = Book.objects.all()
        for _ in range(30):  
            Review.objects.create(
                book=random.choice(books),
                user=random.choice(users),
                content=fake.text(max_nb_chars=300),
                rating=random.randint(1, 5)
            )

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))