from django.db import models

# Create your models here.
class IceCream(models.Model):
    name = models.CharField(max_length=100)
    flavor = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/icecream_images/', null=True, blank=True)  # ImageField added

    def __str__(self):
        return self.name

    # class Order(models.Model):
    #     order_id = models.AutoField(primary_key=True)
    #     address = models.CharField(max_length=255)
    #     date_of_order = models.DateTimeField(auto_now_add=True)
    #     ice_cream = models.ForeignKey(IceCream, on_delete=models.CASCADE)
    #     user = models.ForeignKey(User, on_delete=models.CASCADE)
    #     quantity = models.IntegerField()
    #     def __str__(self):
    #         return f"Order {self.order_id} by {self.user.username}"
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=150)
 
    def __str__(self):
        return self.username
    
