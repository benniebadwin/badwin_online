from django.urls import path
from . import views
# subscribe
from django.urls import path
from . import views
# wishlist
from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import *

# coupon
from app.views import AddCouponView

# Paypal
from .views import paymentComplete
    



urlpatterns = [
    path('', views.index, name='index'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('update_profile/<int:id>/', views.update_profile, name='update_profile'),
    path('profile/', views.profile, name='profile'),
    path('shop/', views.shop, name='shop'),
    path('shop/category/<slug:category_slug>/', views.shop, name='products_by_category'),
    path('shop/category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('shop/submit_review/<int:product_id>/', views.submit_review, name='submit_review' ),
    path('cart/', views.cart, name='cart'),
    path('add_to_wishlist/<int:id>/', views.wishlist_product_toggle, name='wishlist_product_toggle'),
    path('checkout/', views.checkout, name='checkout'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('remove_cart/<int:product_id>/<int:cart_item_id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/<int:cart_item_id>/', views.remove_cart_item, name='remove_cart_item'),
    path('delete_cart/', views.delete_cart,name='delete_cart'),
    path('shop/search/', views.search, name='search'),
    path('place_order/', views.place_order, name='place_order'),
    path('payments/', views.payments, name='payments'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('userPayment/', views.userPayment, name='userPayment'),
    # path("<slug:slug>/", views.product_detail, name="product_detail"),
    # path('custom_404_page/', path.to.views.custom_404_page , name='custom_404_page'),
    # Wishlist
    path("wishlist", views.wishlist, name="wishlist"),

     # User dashboard
    path("dashboard/", views.dashboard, name="dashboard"),
    # path("<slug:slug>/", views.product_detail, name="product_detail1"),
    path("", views.user_orders, name="user_orders"),

    # subscribe
    path('subscribe/', Subscribe),
    path('contactus/',contactus),

    # Subscription
    # path('Newsletter/', Newsletter),

    # coupon
    path('add_coupon/', AddCouponView.as_view(), name='add-coupon'),

    # paypal
    path('complete/', paymentComplete, name = 'complete'),

    path("update_user_password/",views.update_user_password,name='update_user_password'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),



    
]
