import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('shoes', 'Shoes'),
        ('ball', 'Ball'),
        ('goalkeeper gloves', 'Goalkeeper Gloves'),
        ('shaker', 'Shaker'),
        ('socks', 'Socks'),
        ('figure', 'Figure'),
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    @property
    def is_items_cheap(self):
        return self.price < 20
        
    def decrement_price(self):
        self.price -= 10
        self.save() 
        