from django.shortcuts import render

def index(request):
    a = int(request.GET.get('a', 0))
    b = int(request.GET.get('b', 0))
    c = int(request.GET.get('c', 0))
    
    somme = a + b + c
    maximum = max(a, b, c)
    
    return render(request, "index.html", {"somme": somme, "maximum": maximum})