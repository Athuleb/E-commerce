from django.shortcuts import render




def demo(request):
    return render (request, 'index.html')

def home(request):
    return render(request,'home/home.html')

def shop(request):
    return render(request,'shop/shop.html')

def deals(request):
    return render(request,'deals/deals.html')

def contact(request):
    return render(request,'contact/contact.html')
