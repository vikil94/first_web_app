from django.http import HttpResponse
from django.shortcuts import render
from random import randint





def home_page(request):
    context = {'name': 'Vikil Naik'}
    response = render(request, 'index.html', context)
    return HttpResponse(response)

def portfolio_page(request):
    image_urls = []
    for i in range(5):
        random_number = randint(0,100)
        image_urls.append("https://picsum.photos/400/600/?image={}".format(random_number))
    context = {'gallery_images': image_urls}
    response = render(request, 'gallery.html', context)
    return HttpResponse(response)

def about_me_page(request):
    context = {'skills': ['coding', 'writing', 'public speakiing'],
                'interests': ['golf', 'liverpoolfc', 'Toronto Raptors']}
    response = render(request, 'about_me.html', context)
    return HttpResponse(response)

def favourites_page(request):
    context = {'fave_links': 'https://www.reddit.com/r/liverpoolfc'}
    response = render(request, 'fave_link.html', context)
    return HttpResponse(response)
