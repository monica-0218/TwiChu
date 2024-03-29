# Generated by Django 3.1.4 on 2020-12-07 11:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('description', models.CharField(max_length=100, verbose_name='説明・紹介')),
                ('thumbnail', models.ImageField(upload_to='post_images/', verbose_name='サムネイル')),
                ('tweeturl', models.URLField(verbose_name='ツイートURL')),
                ('favorited_weight', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='いいねの倍率')),
                ('retweeted_weight', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='リツイートの倍率')),
                ('commented_weight', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='コメントの倍率')),
                ('content', models.TextField(verbose_name='紹介文')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
