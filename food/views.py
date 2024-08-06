from django.shortcuts import HttpResponse, redirect, render

from .forms import ItemForm
from .models import Item
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
def index(requset):
    item_list = Item.objects.all()
    context = {
        'item_list':item_list,
    }
    return render(requset,'index.html',context)


class IndexClassView(ListView):
    model = Item;
    template_name = 'index.html'
    context_object_name = 'item_list'

def item(request):
    return HttpResponse("item page")


def detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item':item,
    }    
    return render(request, 'detail.html',context)

class FoodDetail(DetailView):
    model = Item
    template_name = 'detail.html'

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect("index")
    else:
        form=ItemForm()
    return render(request,'item-form.html',{'form':form})

def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST, instance=item)
    
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'item-form.html',{'form':form,'item':item})

def delete_item(request, id):
    item = Item.objects.get(id=id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'item-delete.html',{'item':item})


