from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce import HTMLField

# Create your models here.

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return f'{self.user.first_name}, {self.user.last_name}'

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"id": self.id})


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField()
    content = HTMLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def get_update_url(self):
        return reverse("blog-update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("blog-delete", kwargs={"id": self.id})

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"id": self.id})
    