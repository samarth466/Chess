from django.db import models
from authentication.models import User

# Create your models here.


class Base(models.Model):

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_author")
    content = models.TextField()
    publication_date = models.DateTimeField()

    class Meta:
        abstract = True


class Post(Base):

    title = models.CharField(max_length=200)
    comment_count = models.IntegerField(default=0, blank=True)

    class Meta:
        db_table = "Post"
        verbose_name = 'post'
        verbose_name_plural = 'posts'


class Comment(Base):

    post = models.ForeignKey(
        Post, on_delete=models.DO_NOTHING, related_name='comment')

    class Meta:
        db_table = "Comment"
        verbose_name = "comment"
        verbose_name_plural = "comments"
