from django.db import models

# Create your models here.


class weibo(models.Model):
    pub_datetime = models.DateTimeField('weibo published datetime')
    content = models.CharField(max_length=300)


class oauth(models.Model):
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=1000)
    statuses_count = models.BigIntegerField()
    friends_count = models.BigIntegerField()
    followers_count = models.BigIntegerField()
    verified = models.BooleanField()
    verified_type = models.IntegerField()

    auth_token = models.CharField(max_length=2000)
