from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey(
        'auth.User',
        related_name='posts',
        on_delete=models.CASCADE
    )
    categories = models.ManyToManyField('Category')
    objects = models.Manager()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)
    objects = models.Manager()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'{self.owner} - {self.post}'


class Category(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    objects = models.Manager()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title
