from django.shortcuts import render

def Platform(request):
    return render(request, 'platform.html')
def Games(request):
    return render(request, 'games.html', {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]})
def Cart(request):
    return render(request, 'cart.html')
# Create your views here.
