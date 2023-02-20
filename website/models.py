from email.policy import default
import uuid
from django.db import models
from django.contrib.auth.models import User

# from website.views import cart

# Create your models here.
class Author(models.Model):
    author_id=models.AutoField
    name= models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    
class Book(models.Model):
    Book_id=models.AutoField
    name= models.CharField(max_length=200)
    author_id= models.ForeignKey(Author,on_delete=models.CASCADE,default="")
    description= models.TextField(default="")
    price= models.IntegerField()
    image= models.ImageField(upload_to="static\website\imh", default="")
    

    def __str__(self):
        return self.name
    
class RequestBook(models.Model):
    rname= models.CharField(max_length=200,default="")
    bookrequest =models.CharField(max_length=200,default="")
    
    def __str__(self):
            return self.rname +','+'    ' +self.bookrequest
        
    
    

    

    
class Cart(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     cart_id = models.UUIDField(default=uuid.uuid4,unique=True,editable=False)
     completed = models.BooleanField(default=False)
     
     @property
     def get_cart_total(self):
         cartitems = self.cartitems_set.all()
         total = sum([item.get_total for item in cartitems])
         return total
     
     @property
     def get_cart_quantity(self):
         cartitems = self.cartitems_set.all()
         total_quantity = sum([item.quantity for item in cartitems])
         return total_quantity
     
     def __str__(self):
            return str(self.id)+','+ str(self.user)

class Cartitems(models.Model):
    cartItem_id = models.AutoField
    cart =  models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
  
    @property
    def get_total(self):
        price = self.book.price
        quantity = self.quantity
        total = price * quantity
        

        return total
    
    def __str__(self):
        return self.book.name+","+"("+str(self.cart)+")"

 
    
class Order(models.Model):
    order_id=models.AutoField
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    address = models.CharField(max_length=100,default="")
    method = models.CharField(max_length=100,default="")
    number = models.IntegerField(default=0)
    renumber = models.IntegerField(default=0)
        
    

    def __str__(self):
        return str(self.user_id)+",("+str(self.cart_id)+"),"
  