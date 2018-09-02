from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Music Is ON !</h1>")
