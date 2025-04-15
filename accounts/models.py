from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

#Adress
# class Address(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     country = models.CharField(max_length=50)
#     city = models.CharField(max_length=50)
#     street = models.CharField(max_length=100)
#     house_number = models.CharField(max_length=10)
#     zip_code = models.CharField(max_length=10)

#     def __str__(self):
#         return f"Address of {self.customer.first_name} {self.customer.last_name}"

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=255)

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=20)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)  # Image field for storing images
    stock = models.IntegerField()
    color = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class ProductType(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cart ID: {self.cart_id}, Customer: {self.customer.first_name} {self.customer.last_name}, Product: {self.product.name}"
    


class Address(models.Model):
    customer_id = models.IntegerField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"


class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)  # Assuming you're using Django's User model
    address = models.ForeignKey('Address', on_delete=models.CASCADE)  # ForeignKey to Address model
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default='Pending')
    
  

    def __str__(self):
        return f"Order {self.id} by {self.customer.username} - {self.status}"



class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Explicitly define the table name

    def __str__(self):
        return f"Item {self.product_id} for Order {self.order.id}"
    

class OrderDetails(models.Model):
    order_id = models.IntegerField() 
    customer_id = models.IntegerField()
    customer_email = models.CharField(max_length=255)
    full_address = models.CharField(max_length=255)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.order_id} - {self.product_name}"
    
class Checkout(models.Model):
    order_id = models.IntegerField() 
    customer_id = models.IntegerField()
    customer_email = models.CharField(max_length=255)
    full_address = models.CharField(max_length=255)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.order_id} - {self.product_name}"
    

