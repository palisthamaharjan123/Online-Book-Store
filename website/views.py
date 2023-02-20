from contextlib import nullcontext
from multiprocessing import context
from os import remove
from re import search
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, render
from website.models import Book, Cartitems, Order, RequestBook,Cart,Order
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
import json

#     if request.method == "POST":
#         user_email = request.POST['user-email']
#         password = request.POST['password']
#         name = request.POST['name']
#         return render(request, 'home.html',{'name': name})
#     else:
#         return render(request, 'home.html',{})

# def home(request):
#     if request.method == "POST":
#          requestbook = request.POST['requestbook']
#          return render(request,'home.html',{'requestbook':requestbook})
#     else:



def home(request):
    
    if request.user.is_authenticated:
         books = Book.objects.all()
         context = {'books':books}
         return render(request,'home.html', context)
    
    if request.method == 'POST':
        rname = request.POST['rname']
        bookrequest= request.POST['bookrequest']
        # if len(rname) < 2:
        #     return HttpResponse('error! your name is too short')
        # else:
        new_book = RequestBook(rname=rname,bookrequest=bookrequest)
        new_book.save()
        return redirect("home.html")
    else:
        return render(request,'home.html', {})
    
    
     
     
    
    

def books(request,Book_id=10):
    books = Book.objects.get(id = Book_id)
    context = {'books':books}
    return render(request, 'books.html',context)


def booksB(request,Book_id=2):
    books = Book.objects.get(id = Book_id)
    context = {'books':books}
    return render(request, 'booksB.html', context)


def booksG(request,Book_id=27):
    books = Book.objects.get(id = Book_id)
    context = {'books':books}
    return render(request, 'booksG.html', context)


def booksH(request,Book_id=4):
    books = Book.objects.get(id = Book_id)
    context = {'books':books}
    return render(request, 'booksH.html', context)


def booksI(request,Book_id=5):
    books = Book.objects.get(id = Book_id)
    context = {'books':books}
    return render(request, 'booksI.html', context)


def booksJ(request,Book_id=6):
    books = Book.objects.get(id = Book_id)
    context = {'books':books}
    return render(request, 'booksJ.html', context)


def booksK(request,Book_id=7):
    books = Book.objects.get(id = Book_id)
    context = {'books':books}
    return render(request, 'booksK.html', context)


def booksL(request,Book_id=8):
    books = Book.objects.get(id = Book_id)
    context = {'books':books}
    return render(request, 'booksL.html', context)


def booksM(request,Book_id=9):
    books = Book.objects.get(id = Book_id)
    context = {'books':books}
    return render(request, 'booksM.html', context)


def arrivals1(request,Book_id=11):
    books = Book.objects.get(id = Book_id)
    context = {'books':books}
    return render(request, 'arrivals1.html', context)


def arrivals2(request,Book_id=12):
    books = Book.objects.get(id = Book_id)
    context = {'books':books}
    return render(request, 'arrivals2.html', context)


def arrivals4(request,Book_id=13):
    books = Book.objects.get(id = Book_id)
    context = {'books':books}
    return render(request, 'arrivals4.html', context)



def signup(request):
   
     if request.method == "POST":
         cname = request.POST['cname']
         cemail = request.POST['cemail']
         cpassword = request.POST['cpassword']
         recpassword = request.POST['recpassword']
         caddress = request.POST['caddress']
         cphone = request.POST['cphone']
        #  return redirect('signup')
         if len(cname)>10:
             messages.error(request,"your username must be under 10 characters")
             return redirect('signup.html') 
         if len(cname)<3:
             messages.error(request,"your username must be more that 3 characters")
             return redirect('signup.html') 
         if not cname.isalnum():
             messages.error(request,"username should only contain letter and numbers")
             return redirect('signup.html')
         if cpassword!=recpassword:
             messages.error(request,"your password do not match")
             return redirect("signup.html")
         
    
        #create user
         myuser = User.objects.create_user(cname,cemail,cpassword)
         myuser.first_name = cname
         myuser.save()
         messages.success(request,"your account has been successfully created")
         return redirect("signup.html")
     else:
         return render(request, 'signup.html',{})
     
     
    

def signin(request):
    if request.method == "POST":
        lname = request.POST['lname']
        lpassword = request.POST['lpassword']
        
        user = authenticate(username=lname,password=lpassword)
        
        if user is not None:
            auth.login(request,user)
            messages.success(request,"successfully logged in")
            return redirect('home')
        else:
            messages.error(request,"invalid credentials,please try again")
            return redirect('home')
    return render(request, 'signin.html', {})

def slogout(request):
    logout(request)
    messages.success(request,"successfully logged out")
    return redirect('home')

def heart(request):
    return render(request, 'heart.html', {})


def checkout(request,cartItem_id=1):
    if request.method == "POST":
         address = request.POST['saddress']
         method = request.POST['smethod']
         number = request.POST['sphone']
         renumber = request.POST['resphone']
         user=request.user
         cart, created = Cart.objects.get_or_create(user = request.user, completed=False)
         total= cart.get_cart_total
        #  cartitems, created = Cartitems.objects.get_or_create(cart = cart)
        #  total = 0
        #  for item in cartitems:
        #      total = total+item.book.price*item.quantity
         new_order = Order(address=address,method=method,number=number,renumber=renumber,cart_id=cart,user_id=user,total=total)
         new_order.save()
         
    else:
        return render(request,'checkout.html', {})
    
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user = user, completed=False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total":0, "get_cart_quantity": 0}
    
        
    return render(request ,'checkout.html', {'cart':cart,'cartitems': cartitems })

    

def show_books(request, books_id):
    book = Book.objects.get(pk=books_id)
    return render(request, 'books.html',{'book':book})


def search(request):
    if request.method == 'GET':
        searched=request.GET['searched']
        data=Book.objects.filter(name__icontains=searched).order_by('-id')
        return render(request, 'search.html', {'data':data})
    else:
        return HttpResponse('sorry could not find that book')
        

def cart(request):
    
    if request.user.is_authenticated:
        user = request.user
        cart, created = Cart.objects.get_or_create(user = user, completed=False)
        cartitems = cart.cartitems_set.all()
    else:
        cartitems = []
        cart = {"get_cart_total":0, "get_cart_quantity": 0}
    
        
    return render(request ,'cart.html', {'cart':cart,'cartitems': cartitems })


def updateCart(request):
    data = json.loads(request.body)
    book_id = data["book_id"]
    action = data["action"]
    # quantity= data["quantity"]
    book = Book.objects.get(id=book_id)
    print(book)
    user = request.user
    cart, created = Cart.objects.get_or_create(user = user, completed=False)
    cartitems, created = Cartitems.objects.get_or_create(cart = cart, book=book)  
    
    if action == "add":
        cartitems.quantity += 1
        cartitems.save()
        
        
    return JsonResponse("Cart Updated", safe = False)

def updateQuantity(request):
    data = json.loads(request.body)
    quantityFieldValue = data['qfv']
    quantityFieldBook = data['qfp']
    book = Cartitems.objects.filter(book__name=quantityFieldBook).last()
    book.quantity = quantityFieldValue
    book.save()
    return JsonResponse("quantity updated",safe=False)


# def deletefromcart(request,book_id=1):
#     Cart.objects.filter(id=book_id).delete()
#     messages.success(request,"your item has been deleted")
#     return HttpResponseRedirect("/updateCart")

