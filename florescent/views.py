from django.shortcuts import render

def index(request):
    return render(request, 'app.html', {
        'title': 'Home',
    })


def gallery(request):
    return render(request, 'app.html', {
        'title': 'Gallery'
    })