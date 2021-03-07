from django.urls import path, include
from .views import CustomLoginView, CustomSignup, CustomLogout, CustomPasswordChangeView

urlpatterns = [

    path('login/', CustomLoginView.as_view(), name="loginpage"),
    path('signup/', CustomSignup.as_view(), name="signuppage"),
    path('logout/', CustomLogout.as_view(), name="logoutpage"),
    path('changepassword/', CustomPasswordChangeView.as_view(), name="changepassword"),

]
