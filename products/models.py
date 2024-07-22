from django.db import models

# Create your models here.
class Product(models.Model):
    SELLER_CHOICES = (
        ("SELLER 1", "SELLER 1"),
        ("SELLER 2", "SELLER 2"),
        ("SELLER 3", "SELLER 3"),
    )
    user=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image=models.ImageField(upload_to='product_images',null=True,blank=True)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=100, default="")
    seller = models.CharField(choices=SELLER_CHOICES, max_length=100, default="SELLER 1")

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100, default="")
    quantity = models.IntegerField(default=1)
    amount = models.IntegerField(default=0)
    amount_due = models.IntegerField(default=0)
    amount_paid = models.IntegerField(default=0)
    currency: models.CharField(max_length=10, default="INR")
    receipt = models.CharField(max_length=100, default="")
    status = models.CharField(max_length=100, default="created") # Pending, Completed, Cancelled
    created_at = models.DateTimeField(auto_now_add=True)

