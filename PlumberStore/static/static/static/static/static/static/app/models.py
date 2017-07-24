"""
Definition of models.
"""

from django.db import models

# Create your models here.
class GoodModel(models.Model):
    good_name = models.CharField(max_length = 128)
    description = models.CharField(max_length = 128)
    price = models.FloatField()
    image = models.ImageField(upload_to = 'goods_pic_folder', default = 'goods_pic_folder/no-img.jpg')
    def __str__(self):
        return self.good_name

class ReviewModel(models.Model):
    reviewer_name = models.CharField(max_length = 128)
    mail = models.CharField(max_length = 128)
    theme = models.FloatField()
    review = models.CharField(max_length = 512)
    validated = models.BooleanField()
    