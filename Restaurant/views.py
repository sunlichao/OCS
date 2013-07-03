from django.shortcuts import render, get_object_or_404, HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from Restaurant.models import Menu, Restaurant
import bz2
import base64
import json

# Create your views here.


def detail(request, restaurant_name):


    #menu_list.extra(Restaurant.objects.all())
    #print menu_list


    try:
        restaurant_list=Restaurant.objects.get(name=restaurant_name)
    except Restaurant.DoesNotExist:
        return HttpResponse("The restaurant %s does not exist yet.  Create it?" % restaurant_name)
     #   "menu_list":menu.objects.all()


    menu_list = Menu.objects.filter(restaurant=restaurant_list._get_pk_val)

    context = {'menu_list':menu_list,
               'restaurant':restaurant_list}

    #print context

    return render(request, 'Restaurant/detail.html',context)

    #return HttpResponse("This is the page for %s." % restaurant_name)


def index(request):
    restaurant_list = Restaurant.objects.all()
    paginator = Paginator(restaurant_list, 3) # Show 25 contacts per page


    page = request.GET.get('page')
    try:
        restaurants = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        restaurants = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        restaurants = paginator.page(paginator.num_pages)

    return render(request,'Restaurant/index.html',{"restaurants":restaurants})

def order(request, restaurant_name):
    p = get_object_or_404(Restaurant,name=restaurant_name)
    try:
        selected_dishes = request.POST
        dishes = selected_dishes.copy()
        del dishes['csrfmiddlewaretoken']
        dish_String = []
        for pair in dishes:
            dish_pair = str(dishes[pair])
            dish_pair = dish_pair.replace(' ','-')
            dish_String.append(dish_pair)
            dish_String.append('+')
        dish_String = ''.join(dish_String)
        print dish_String
        dish_String=dish_String[:-1]


    except (KeyError,Menu.DoesNotExist):
        return render(request,"Restaurant/detail.html",{
            'Menu':p,
            'error_message':"You didn't select anything"
        })
    else:
        encoded_String = base64.b64encode(bz2.compress(dish_String))
        string = "/restaurant/",restaurant_name,"/checkout/",encoded_String,"/"
        returnString = ''.join(string)
        #print returnString
        return HttpResponseRedirect(returnString)
        #return HttpResponse(checkout(request,restaurant_name=restaurant_name,selected_dish=selected_dish[0].dish))

def checkout(request, restaurant_name, selected_dish ):
    decodedString = bz2.decompress(base64.b64decode(selected_dish))
    dish = decodedString.replace('-', ' ')
    return HttpResponse("The selected dish is %s from %s" % (dish, restaurant_name))