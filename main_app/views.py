from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
# Create your views here.

def index(request):
    feature= featured.objects.all()
    car= carousel.objects.all()
    return render(request,'index.html', {'feature' : feature, 'car': car})

def mens(request):
    lux= occational.objects.all()
    form= formal.objects.all()
    cas= casual.objects.all()
    kds= kids.objects.all()

    return render (request, 'men.html', {'lux': lux, 'form': form, 'cas': cas,'kds':kds})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def occasion(request):
    lux= occational.objects.all()

    return render(request,'occasional.html',{'lux': lux})

def formals(request):
    form= formal.objects.all()

    return render(request,'formal.html',{'form': form})

def casuals(request):
    cas= casual.objects.all()

    return render(request,'casual.html',{'cas': cas})

def kid(request):
    kds= kids.objects.all()

    return render(request,'kids.html', {'kds':kds})

 
def product_detail(request, id, model_type):
    if model_type == 'featured':
            product = get_object_or_404(featured, id=id)
    elif model_type == 'car':
            product = get_object_or_404(carousel, id=id)
    elif model_type == 'lux':
            product = get_object_or_404(occational, id=id)
    elif model_type == 'form':
            product = get_object_or_404(formal, id=id)
    elif model_type == 'cas':
            product = get_object_or_404(casual, id=id)
    elif model_type == 'kds':
            product = get_object_or_404(kids, id=id)


    return render(request, 'product_details.html', {'product': product})

def search(request):
    query = request.GET.get('q')
    if query:
        q_objects = Q(tags__icontains=query)
        featured_results = featured.objects.filter(q_objects)
        carousel_results = carousel.objects.filter(q_objects)
        occational_results = occational.objects.filter(q_objects)
        formal_results = formal.objects.filter(q_objects)
        casual_results = casual.objects.filter(q_objects)
        kids_results = kids.objects.filter(q_objects)
        
        results = list(featured_results) + list(carousel_results) + list(occational_results) + \
                  list(formal_results) + list(casual_results) + list(kids_results)
    else:
        results = []
    
    return render(request, 'search_results.html', {'results': results, 'query': query})