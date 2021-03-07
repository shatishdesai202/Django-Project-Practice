from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    # path('', TemplateView.as_view(template_name="profilemodel/profile.html"), name="profilepage")
    path('', login_required(views.ChangeProfile.as_view()), name="profilepage")
]
