from django.shortcuts import render

def Platform(request):
    return render(request, 'platform.html')
def Games(request):
    return render(request, 'games.html')
def Cart(request):
    return render(request, 'cart.html')
# Create your views here.
