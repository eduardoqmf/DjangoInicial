from django.shortcuts import render


def home(request):
    # HttpResponse("Hello, world. You're at the home index.")
    return render(request, 'index.html', {})
