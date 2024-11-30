from django.test import TestCase, Client
from django.urls import reverse
from user.models import User
from book.models import Book, Author, Category


class UserViewsTestCase(TestCase):
    from book.models import Author, Category

class UserViewsTestCase(TestCase):
    from book.models import Author, Category, Book
from publishing_house.models import PublishingHouse


class UserViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.other_user = User.objects.create_user(username="otheruser", password="password")

        # Создаем автора
        self.author = Author.objects.create(
            name="Test Author",
            date="2023-01-01T00:00:00Z",  # Укажите подходящий формат даты
            biography="This is a test biography.",
        )

        # Создаем категорию
        self.category = Category.objects.create(
            name="Fiction",
            description="Fictional books",
        )

        # Создаем издательство
        self.publishing_house = PublishingHouse.objects.create(
            name="Test Publishing House",
            address="123 Test Street",
        )

        # Создаем книгу
        self.book = Book.objects.create(
            title="Test Book",
            price=10.00,
            description="Test Description",
            publishing_house=self.publishing_house,
            author_name=self.author,
            category=self.category,
        )

        self.user.favorite_books.add(self.book)


    def test_register_view_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_post(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_logout_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_profile_view_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')
        self.assertIn(self.book, response.context['favorite_books'])

    def test_profile_view_unauthenticated(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    def test_update_profile_view_unauthenticated(self):
        response = self.client.get(reverse('update_profile', args=[self.user.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    def test_update_profile_view_post_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('update_profile', args=[self.user.pk]), {
            'username': 'updateduser'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('profile'))

    def test_update_profile_view_post_unauthenticated(self):
        response = self.client.post(reverse('update_profile', args=[self.user.pk]), {
            'username': 'updateduser'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
