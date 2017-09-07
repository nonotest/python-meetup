from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Develop. This is a test change.")
