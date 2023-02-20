from django.urls import path,include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name="home"),
    path('home.html', views.home, name='home'),
    path('books.html', views.books, name="books"),
    path('booksB.html', views.booksB, name="booksB"),
    path('booksG.html', views.booksG, name="booksG"),
    path('booksH.html', views.booksH, name="booksH"),
    path('booksI.html', views.booksI, name="booksI"),
    path('booksJ.html', views.booksJ, name="booksJ"),
    path('booksK.html', views.booksK, name="booksK"),
    path('booksL.html', views.booksL, name="booksL"),
    path('booksM.html', views.booksM, name="booksM"),
    path('arrivals1.html', views.arrivals1, name="arrivals1"),
    path('arrivals2.html', views.arrivals2, name="arrivals2"),
    path('arrivals4.html', views.arrivals4, name="arrivals4"),
    path('cart.html', views.cart, name="cart"),
    path('signup.html', views.signup, name="signup"),
    path('signin.html', views.signin, name="signin"),
    path('heart.html', views.heart, name="heart"),
    path('checkout.html', views.checkout, name="checkout"),
    path('search',views.search,name="search"),
    # path('show_books/<books_id>.html',views.show_books,name="show_books")
    path('logout',views.slogout,name='slogout'),
    path('updateCart',views.updateCart,name='updateCart'),
    path('updateQuantity',views.updateQuantity,name='updateQuantity'),
    # path('deletefromcart',views.deletefromcart,name='deletefromcart'),
    # path('deletecartitem/<int:cartItem_id>',views.deletecartitem,name='deletecartitem'),
]
