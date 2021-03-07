from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.views.generic.list import ListView
from .models import Category, Product
from django.views import View
from authenticationmodel.forms import CustomSignupForm
from .models import Placeorder as model_placeorder
from .forms import Placeorder as form_placeorder
# from .models import Placeorder

from .models import Comment
from .forms import commentForm

# paytm Integration
from django.views.decorators.csrf import csrf_exempt
from paytm import checksum
MERCHANT_KEY = 'JhfSHbmd_ZtZ0c7K'


class Index(View):

    def get(self, request, id=None):
        
        # request.session.flush()
        all_category = Category.get_all_categoty()

        if id == None:
            all_product = Product.get_all_product()
        else:
            all_product = Product.get_product_category_wise(id)

        cart = request.session.get('cart')
        if cart:
            k = cart.keys()
            nav_product = Product.get_product_in_cartdetail(k)
        else:
            nav_product = None

        context = {'all_category': all_category,
                   'all_product': all_product, 'nav_product': nav_product}
        return render(request, 'eshop/home.html', context)

    def post(self, request, id=None):
        # request.session.flush()
        # del request.session['cart']
        productid = request.POST.get('productid')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
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
        # print('Final Cart ***** ', cart)
        # print(cart)
        # request.session.flush()
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next)
        # return redirect('homepage')


class Preview(View):
    def get(self, request, id):
        get_product_detail = Product.objects.get(pk=id)

        cart = request.session.get('cart')
        if cart:
            k = cart.keys()
            nav_product = Product.get_product_in_cartdetail(k)
        else:
            nav_product = None

        # comment = Comment.objects.filter(parent=None).order_by('-timestamp')
        # form = commentForm()
        post = Product.objects.get(id=id)
        showcomment = Comment.objects.filter(postby=id).filter(parent=None)
        form = commentForm()

        context = {'get_product_detail': get_product_detail, 'nav_product': nav_product,
                   'post': post, 'form': form, 'comment': showcomment}
        return render(request, 'eshop/preview.html', context)

    def post(self, request, id):
        post = Product.objects.get(id=id)
        showcomment = Comment.objects.filter(postby=id).filter(parent=None)
        form = commentForm()

        form = commentForm(request.POST)
        form.instance.postby = post
        form.instance.commentBy = request.user
        parent = request.POST.get('parent')

        if parent:
            parentpost = Comment.objects.get(id=parent)
            form.instance.parent = parentpost

        if form.is_valid():
            form.save()
            return redirect('previewpage', id=post.id)

        context = {'post': post, 'form': form, 'comment': showcomment}
        return render(request, 'eshop/preview.html', context)


class Cart(View):

    def get(self, request):

        cart = request.session.get('cart')
        if cart:
            k = cart.keys()

            all_product = Product.get_product_in_cartdetail(k)
        else:
            all_product = None
        
        # cart = request.session.get('cart')
        if cart:
            k = cart.keys()
            nav_product = Product.get_product_in_cartdetail(k)
        else:
            nav_product = None

        context = {'all_product': all_product, 'nav_product':nav_product}
        return render(request, 'eshop/cart.html', context)

    def post(self, request):
        pass


class Myorder(View):

    def get(self, request):
        a = model_placeorder.get_order_by_customer(request.user)

        cart = request.session.get('cart')
        if cart:
            k = cart.keys()
            nav_product = Product.get_product_in_cartdetail(k)
        else:
            nav_product = None

        context = {'a': a, 'nav_product': nav_product}
        return render(request, 'eshop/myorder.html', context)

    def post(self, request):
        pass


class CheckOut(View):

    def get(self, request):
        cart = request.session.get('cart')
        k = cart.keys()

        all_product = Product.get_product_in_cartdetail(k)

        form = form_placeorder(instance=request.user)

        context = {'all_product': all_product, 'form': form}
        return render(request, 'eshop/checkout.html', context)

    def post(self, request):
        cart = request.session.get('cart')

        firstname = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('Add')
        city = request.POST.get('city')
        pin = request.POST.get('pin')
        amount = request.POST.get('amount')

        products = Product.get_product_in_cartdetail(list(cart.keys()))

        for pro in products:

            form = model_placeorder(firstname=firstname, price=pro.price, last_name=last_name,
                                    email=email, address=address, city=city, pin=pin, item=pro, customer=request.user,
                                    qty=cart.get(str(pro.id)))
            form.save()

        print("id", form.id)
        param_dict = {

            'MID': 'dyIWmp27954329407462',
            'ORDER_ID': str(form.id),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL': 'http://127.0.0.1:8000/handlerequest/',
        }

        context = {'param_dict': param_dict}
        
        request.session['cart'] = {}
        param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict, MERCHANT_KEY)
        
        return render(request, 'eshop/paytm.html', context)
        # return render(request, 'eshop/checkout.html', context)
        # return HttpResponse('add to cart')


def itempop(request, itemid):
    cart = request.session.get('cart')
    
    if cart:
        cart.pop(str(itemid))
        request.session['cart'] = cart
    else:
        request.session['cart'] = {}

    return redirect('cart')


@csrf_exempt
def handlerequest(request):
    form = request.POST
    print(form)
    responce_dict = {}
    for i in form.keys():
        responce_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            cs = form[i]

    verify = checksum.verify_checksum(responce_dict, MERCHANT_KEY, cs)
    if verify:
        if responce_dict['RESPCODE'] == '01':
            print('order success')
        else:
            print('order not success' + responce_dict['RESPMSG'])
    request.session['cart'] = {}
    
    return render(request, 'eshop/paymentstatus.html', {'responce': responce_dict})
