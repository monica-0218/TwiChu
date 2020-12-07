from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings

# 中間モデル
class FriendShip(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='follow_friendships')
    follow = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='follower_friendships')

    class Meta:
        unique_together = ('follower', 'follow')

# カスタムユーザー
class CustomUser(AbstractUser):
    follows = models.ManyToManyField(
        settings.AUTH_USER_MODEL, verbose_name='フォロー中のユーザー', through='FriendShip',
        related_name='+', through_fields=('follower', 'follow')
    )
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, verbose_name='フォローされているユーザー', through='FriendShip', 
        related_name='+', through_fields=('follow', 'follower')
    )
    
    class Meta(AbstractUser.Meta):
        db_table = 'custom_user'