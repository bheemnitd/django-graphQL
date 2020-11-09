from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.TextField(max_length=500)
    description = models.TextField(max_length=50000)
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.TextField(max_length=500)


class Comment(models.Model):
    post = models.ForeignKey(Post,  on_delete=models.CASCADE, null=False)
    text = models.TextField(max_length=5000)
    author = models.TextField(max_length=500)

