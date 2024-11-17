from django.db import models
from django.core.validators import MinValueValidator
from .validators import ReviewValidator
from publishing_house.models import PublishingHouse
from user.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(null = False)
    biography = models.TextField()
    books = models.ManyToManyField('Book', related_name ='authors', blank = True )

    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length = 150)
    price = models.DecimalField(validators=[MinValueValidator(1)], decimal_places=2, max_digits=10)
    image = models.ImageField(blank=True)
    description = models.TextField()
    review = models.TextField(null = True)
    publishing_house = models.ForeignKey(PublishingHouse, null = False, on_delete=models.CASCADE)
    author_name = models.ForeignKey(Author, null = False, max_length = 50, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE )

    def __str__(self):
        return self.title



class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField()
    rating = models.PositiveIntegerField(validators=[ReviewValidator()])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Review for {self.book.title} by {self.user.username}'

    class Meta:
        ordering = ['-created_at']