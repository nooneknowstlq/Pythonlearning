from django.shortcuts import render
from .models import CmsSlider
from crm.models import Order
from crm.forms import OrderForm
from telebot.sendmessage import send_telegram
from products.models import ProductCategory, Product
from django.core.paginator import Paginator




def first_page(request):
    slider_list = CmsSlider.objects.all()
    form = OrderForm()
    context = {
        'slider_list': slider_list,
        'form': form,
    }
    return render(request, 'cms/index.html', context)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        send_telegram(tg_name=name, tg_phone=phone)
        return render(request, "cms/thanks.html", {"name": name})
    else:
        return render(request, "cms/thanks.html")


