from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Post(models.Model):
    server = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField('タイトル', max_length=50)
    description = models.CharField('説明・紹介', max_length=100)
    thumbnail = models.ImageField('サムネイル', upload_to='post_images/')
    tweeturl = models.URLField('ツイートURL')
    favorited_weight = models.IntegerField('いいねの倍率', validators=[MinValueValidator(0), MaxValueValidator(100)])
    retweeted_weight = models.IntegerField('リツイートの倍率', validators=[MinValueValidator(0), MaxValueValidator(100)])
    commented_weight = models.IntegerField('コメントの倍率', validators=[MinValueValidator(0), MaxValueValidator(100)])
    content = models.TextField('紹介文')