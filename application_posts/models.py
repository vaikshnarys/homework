from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank = True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Orm(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank = True)
    counter = models.PositiveIntegerField(default=0)
    category = models.CharField(blank=True, null=True)
    time_crete = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title



class Comment(models.Model):
    text = models.TextField(blank=True)
    new = models.ForeignKey('Post', on_delete = models.CASCADE, related_name = 'comments')
    status = models.BooleanField(default=True)

















