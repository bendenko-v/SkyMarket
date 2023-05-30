from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=100, null=False)
    price = models.PositiveIntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Ad')
        verbose_name_plural = _('Ads')
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
