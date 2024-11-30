from django.test import TestCase, Client
from django.urls import reverse
from user.models import User
from .models import Book, Author, Category, Review
from publishing_house.models import PublishingHouse

class ViewsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = Client()

        self.category = Category.objects.create(name="Fiction", description="Fictional books")
        self.publishing_house = PublishingHouse.objects.create(name="Test House")
        self.author = Author.objects.create(
            name="Author Test",
            date="2024-01-01T00:00:00Z",
            biography="Test biography"
        )
        self.book = Book.objects.create(
            title="Test Book",
            price=10.99,
            description="Test description",
            review="Great book!",
            publishing_house=self.publishing_house,
            author_name=self.author,
            category=self.category
        )
        self.book.authors.add(self.author)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)

    def test_book_detail_view(self):
        response = self.client.get(reverse('book_detail', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)
        self.assertContains(response, self.book.description)

    def test_add_favorite_book_view(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('add_favorite_book', args=[self.book.id]))
        self.assertRedirects(response, reverse('book_detail', args=[self.book.id]))
        self.assertIn(self.book, self.user.favorite_books.all())

    def test_delete_favorite_book_view(self):
        self.client.login(username='testuser', password='password')
        self.user.favorite_books.add(self.book)
        response = self.client.post(reverse('delete_from_favorite_books', args=[self.book.id]))
        self.assertRedirects(response, reverse('profile'))
        self.assertNotIn(self.book, self.user.favorite_books.all())

    def test_add_favorite_book_view_unauthenticated(self):
        response = self.client.post(reverse('add_favorite_book', args=[self.book.id]))
        self.assertNotEqual(response.status_code, 200)  

    def test_delete_favorite_book_view_unauthenticated(self):
        response = self.client.post(reverse('delete_from_favorite_books', args=[self.book.id]))
        self.assertNotEqual(response.status_code, 200)  
