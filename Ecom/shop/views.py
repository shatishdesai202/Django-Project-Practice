from django.shortcuts import render
from django.views import View
from .models import Category, Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class Index(View):
    def get(self, request):
        # request.session.flush()
        category = Category.objects.all()
        product = Product.objects.all()
        context = {'all_category': category, 'all_product': product}
        return render(request, 'shop/index.html', context)

    @csrf_exempt
    def post(self, request):
        if request.method == "POST":
            # productid = request.POST['proid']
            # print(type(productid))
            productid = request.POST.get('proid')
            # print(type(pid))
            cart = request.session.get('cart')
            remove = request.POST.get('remove')
            print('remove--->', remove)
            if cart:
                
                qty = cart.get(productid)
                
                if qty:
                    if remove:
                        if qty == 1:
                            cart.pop(productid)
                        else:
                            cart[productid] = qty - 1
                    else:
                        cart[productid] = qty + 1
                else:
                    cart[productid] = 1
            else:
                # print('else part')
                cart = {}
                cart[productid] = 1
                # print('else ---> ', cart)

            request.session['cart'] = cart
            
            count = cart.get(productid)

            print('cart----->',cart)
            print('count----->',count)
            # productid = None
            return JsonResponse({'status': '1', 'count':count, 'pid':productid})
        else:
            return JsonResponse({'status': 0})
