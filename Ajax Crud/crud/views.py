from django.shortcuts import render
from .models import Detail
from django.http import JsonResponse
from .forms import DetailForm

def index(request):
    form = DetailForm()
    detail = Detail.objects.all()
    context = {'form': form, 'detail':detail}
    return render(request, 'home.html', context)


def save_data(request):
    # detail = Detail.objects.all()
    print('okoko')
    if request.method == "POST":
        form = DetailForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            sid = request.POST.get('stuid')
            print(sid)
            if (sid == ''):
                dt = Detail(name=name, email=email, password=password)
            else:
                dt = Detail(id=sid, name=name, email=email, password=password)
            dt.save()
            all_detail = Detail.objects.values()
            all_detail_list = list(all_detail)
            return JsonResponse({'status':'save', 'all_detail':all_detail_list})
        else:
            return JsonResponse({'status':0})

    
def delete_data(request):
    if request.method == "POST":
        myid = request.POST.get('sid')
        dt = Detail.objects.get(pk=myid)
        dt.delete()
        all_detail = Detail.objects.values()
        all_detail_list = list(all_detail)
        return JsonResponse({'status':1, 'all_detail':all_detail_list})
    else:
        return JsonResponse({'status':0})

def update_data(request):
    if request.method == "POST":
        myid = request.POST.get('sid')
        dt = Detail.objects.get(pk=myid)
        return JsonResponse({'status':1, 'id':dt.id, 'name':dt.name, 'email':dt.email, 'password':dt.password})
    else:
        return JsonResponse({'status':0})
