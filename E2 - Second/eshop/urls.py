from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
# from .views import CategoryListView


urlpatterns = [
    path('', views.Index.as_view(), name="homepage"),
    path('<int:id>/', views.Index.as_view(), name="filterhomepage"),
    path('preview/<int:id>', views.Preview.as_view(), name="previewpage"),    
    path('cart', login_required(views.Cart.as_view()), name="cart"), 
    path('checkout/', login_required(views.CheckOut.as_view()), name='checkout'),   
    path('myorder/', login_required(views.Myorder.as_view()), name='myorder'), 
    path('handlerequest/', views.handlerequest, name="handlerequest"),
    path('itempop/<int:itemid>', views.itempop, name="itempop") 
]
