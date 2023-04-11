from django.urls import path


from .views import paymentComplete

app_name = "checkout"

urlpatterns = [
    path('complete/', paymentComplete, name = 'complete'),
   
    
    
]

