from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.users.models import Users


class Category(models.Model):
    category_name = models.CharField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name=_("category_name"),
    )

    def __str__(self):
        return self.category_name


class Posts(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name=_("title"),
        db_index=True,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='category',
    )

    author = models.ForeignKey(
        Users,
        on_delete=models.SET_NULL,
        null=True,
        related_name='author',
    )

    date_publication = models.DateTimeField(
        default=timezone.now,
    )

    text = models.TextField()

    image = models.ImageField(
        null=True,
        blank=True,
        upload_to='images'
    )

    allow_publication = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name_plural = _('Posts')
        verbose_name = _('Post')

    def __str__(self):
        return f"{self.title}-{self.author}"


class PostsComment(models.Model):
    author_comments = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='author_comments',
    )

    posts = models.ForeignKey(
        Posts,
        on_delete=models.SET_NULL,
        null=True,
        related_name='posts',
    )

    text = models.TextField()

    date_publication = models.DateTimeField(
        default=timezone.now,
    )

    def __str__(self):
        return f"{self.posts.title}-{self.author_comments}"
