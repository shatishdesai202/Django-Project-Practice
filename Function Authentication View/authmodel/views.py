from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
# Create your views here.
@login_required
def index(request):
    print(User.objects.filter(is_staff=True))
    return render(request, 'registration/profile.html')

@staff_member_required
def about(request):
    return render(request, 'registration/profile.html')

@permission_required('is_staff')
def permissionpage(request):
    return render(request, 'registration/profile.html')