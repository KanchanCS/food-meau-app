from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.ImageField(upload_to="images", default="https://cdn.pixabay.com/photo/2017/09/30/15/10/plate-2802332_640.jpg")
    
    def __str__(self):
        return self.item_name
    
    