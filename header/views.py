from django.shortcuts import render


# Create your views here.
def homeView(request):
    print(request.user.is_authenticated)
    return render(request, 'home.html', {})


def aboutView(request):
    return render(request, 'about.html', {})


def contactView(request):
    return render(request, 'contact.html', {})
