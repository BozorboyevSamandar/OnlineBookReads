from users.models import CustomUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    isbn = models.CharField(max_length=17)
    picture = models.ImageField(default='default-book.jpg')

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    bio = models.TextField()

    @property
    def full_name(self):
        return self.first_name, self.last_name


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class BookReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField()
    stars = models.IntegerField(
        validators=[MinValueValidator(1),
                    MaxValueValidator(5)
                    ])
