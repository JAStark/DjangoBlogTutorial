from django.db import models
from django.utils import timezone

class Post(models.Model):   #  Inheriting Model class so that Django knows this will be saved in Database
    author = models.ForeignKey('auth.User')   #  This is a link to another model.
    title = models.CharField(max_length=200)  #  Define text with limited number of characters
    text = models.TextField()   #  For long texts without limit
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):     #  Our publish method.
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text
