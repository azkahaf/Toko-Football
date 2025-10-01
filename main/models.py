import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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
    product_views = models.PositiveIntegerField(default=0)
    id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_items_cheap(self):
        return self.price < 20
        
    def decrement_price(self):
        self.price -= 10
        self.save() 

    def increment_views(self):
        self.product_views += 1
        self.save()
        